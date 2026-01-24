## 🔗 What is a RIGHT JOIN?

A **RIGHT JOIN** returns:

- **ALL rows from the RIGHT table**
- Matching rows from the LEFT table
- `NULL`s when there is **no match**

### 🧠 Visual Idea
```
LEFT TABLE ⟖ RIGHT TABLE
(all right rows stay)
```

---

## 1️⃣ Basic RIGHT JOIN Syntax

```sql
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

📌 The **right table** is the **second table** in the query.

---

## 2️⃣ Example: Users and Orders

### Tables
- `users(id, name)`
- `orders(id, user_id, order_date)`

### Query

```sql
SELECT u.name, o.order_date
FROM users u
RIGHT JOIN orders o
ON u.id = o.user_id;
```

### Result
- **All orders appear**
- Orders without a matching user → `u.name = NULL`

---

## 3️⃣ RIGHT JOIN = LEFT JOIN (Rewritten)

💡 Very important for interviews 👇

```sql
SELECT u.name, o.order_date
FROM orders o
LEFT JOIN users u
ON u.id = o.user_id;
```

✔ Same result  
✔ Easier to read  
✔ Preferred in real-world projects  

📌 This is why **RIGHT JOIN is rarely used** in production.

---

## 4️⃣ RIGHT JOIN + WHERE (⚠️ Same Trap)

### ❌ Wrong

```sql
WHERE u.name = 'John'
```

🔴 This removes rows where `u.name` is `NULL`  
➡ Turns the query into an **INNER JOIN**

---

### ✅ Correct

```sql
ON u.id = o.user_id
AND u.name = 'John'
```

📌 Put conditions on the **optional table inside `ON`**

---

## 5️⃣ Find Rows With No Match (Right Side)

### Orders without users

```sql
SELECT o.id
FROM users u
RIGHT JOIN orders o
ON u.id = o.user_id
WHERE u.id IS NULL;
```

✔ Finds orders that **do not belong to any user**

---

## 🆚 RIGHT JOIN vs LEFT JOIN

| RIGHT JOIN | LEFT JOIN |
|-----------|-----------|
| Keeps right table | Keeps left table |
| Less common | Very common |
| Same logic | Preferred style |

---

## 🔑 Interview Key Points

- `RIGHT JOIN` = **reverse LEFT JOIN**
- Rarely used in production
- Can always be rewritten as `LEFT JOIN`
- `WHERE` clause can **break** the join

---

## 🧠 Mental Model

**“Show me everything from the right table, even if the left side doesn’t exist.”**