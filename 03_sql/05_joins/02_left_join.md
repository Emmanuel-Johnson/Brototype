## 🔗 What is a LEFT JOIN?

A **LEFT JOIN** returns:

- **ALL rows from the LEFT table**
- Matching rows from the RIGHT table
- `NULL`s when there is **no match**

### 🧠 Visual Idea
```
LEFT TABLE ⟕ RIGHT TABLE
(all left rows stay)
```

---

## 1️⃣ Basic LEFT JOIN Syntax

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

---

## 2️⃣ Example: Users and Orders

### Tables
- `users(id, name)`
- `orders(id, user_id, order_date)`

### Query

```sql
SELECT u.name, o.order_date
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id;
```

### Result
- Users **with orders** → show order data
- Users **without orders** → order columns = `NULL`

✔ This is the **key difference** from `INNER JOIN`

---

## 3️⃣ LEFT JOIN + WHERE (⚠️ Common Trap)

### ❌ Wrong

```sql
SELECT u.name, o.order_date
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
WHERE o.order_date >= '2025-01-01';
```

🔴 This turns it into an **INNER JOIN**  
(because `NULL >= date` is false)

---

### ✅ Correct Way

```sql
SELECT u.name, o.order_date
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
AND o.order_date >= '2025-01-01';
```

📌 Put conditions on the **right table inside `ON`**

---

## 4️⃣ Find Rows With NO Match (Very Important)

### Users with no orders

```sql
SELECT u.name
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
WHERE o.id IS NULL;
```

🔥 Extremely common **interview question**

---

## 5️⃣ LEFT JOIN with Multiple Tables

```sql
SELECT u.name, o.id, p.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
LEFT JOIN payments p ON o.id = p.order_id;
```

✔ Keeps **all users**, even if they have:
- no orders
- orders but no payments

---

## 🆚 LEFT JOIN vs INNER JOIN (Quick)

| LEFT JOIN | INNER JOIN |
|----------|-----------|
| Keeps all left rows | Keeps only matching rows |
| Shows `NULL`s | No `NULL`s |
| Used to find missing data | Used for strict matches |

---

## 🔑 Interview Key Points

- `LEFT JOIN` ≠ `INNER JOIN`
- `WHERE` on right table can **break LEFT JOIN**
- `IS NULL` → find missing relationships
- Most common JOIN after `INNER JOIN`

---

## 🧠 Mental Model

**“Show me everything from the left table, even if the right side doesn’t exist.”**