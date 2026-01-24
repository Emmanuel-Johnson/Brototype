## 🔗 What is a FULL JOIN?

A **FULL JOIN** (also called **FULL OUTER JOIN**) returns:

- **ALL rows from BOTH tables**
- Matching rows where possible
- `NULL`s where there is **no match on either side**

### 🧠 Visual Idea
```
LEFT TABLE ⟗ RIGHT TABLE
(everything from both)
```

---

## 1️⃣ Basic FULL JOIN Syntax

```sql
SELECT columns
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

📌 `OUTER` is optional in PostgreSQL  
➡ `FULL JOIN` = `FULL OUTER JOIN`

---

## 2️⃣ Example: Users and Orders

### Tables
- `users(id, name)`
- `orders(id, user_id, order_date)`

### Query

```sql
SELECT u.name, o.order_date
FROM users u
FULL JOIN orders o
ON u.id = o.user_id;
```

### Result

| Scenario | Output |
|--------|--------|
| User with orders | Normal joined row |
| User with no orders | Order columns = `NULL` |
| Order with no user | User columns = `NULL` |

---

## 3️⃣ Find Unmatched Rows on BOTH Sides (Very Common)

### Users with no orders **OR** orders with no users

```sql
SELECT u.name, o.id
FROM users u
FULL JOIN orders o
ON u.id = o.user_id
WHERE u.id IS NULL
   OR o.id IS NULL;
```

🔥 **Classic interview query**

---

## 4️⃣ FULL JOIN vs UNION (Interview Trick)

A **FULL JOIN** is conceptually like:

```
LEFT JOIN
+ RIGHT JOIN
```

But:
- Matching rows are **merged**
- Rows are **not duplicated** like `UNION`

---

## 5️⃣ FULL JOIN + WHERE (⚠️ Same Trap Again)

### ❌ Wrong

```sql
WHERE o.order_date >= '2025-01-01'
```

🔴 This removes `NULL` rows  
➡ Breaks the FULL JOIN

---

### ✅ Correct

```sql
ON u.id = o.user_id
AND o.order_date >= '2025-01-01'
```

📌 Put conditions on the **optional side inside `ON`**

---

## 🆚 FULL JOIN vs Other JOINs

| JOIN | What it returns |
|----|-----------------|
| INNER JOIN | Only matching rows |
| LEFT JOIN | All left + matches |
| RIGHT JOIN | All right + matches |
| FULL JOIN | Everything |

---

## 🔑 Interview Key Points

- FULL JOIN keeps **both tables fully**
- Shows **missing relationships on either side**
- Supported in **PostgreSQL ✅**
- ❌ Not supported in MySQL
- `WHERE` clause can **break** it

---

## 🧠 Mental Model

**“I don’t want to lose any row from either table.”**