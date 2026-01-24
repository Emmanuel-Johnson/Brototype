## 🔗 What is an INNER JOIN?

An **INNER JOIN** returns **only the rows that have matching values in both tables**.

If there is **no match**, the row is **excluded**.

### 🧠 Visual Idea
```
Table A ∩ Table B
(only common rows)
```

---

## 1️⃣ Basic INNER JOIN Syntax

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

📌 `INNER` is optional  
➡ `JOIN` alone means **INNER JOIN**

---

## 2️⃣ Example: Users and Orders

### Tables
- `users(id, name)`
- `orders(id, user_id, order_date)`

### Query

```sql
SELECT users.name, orders.order_date
FROM users
INNER JOIN orders
ON users.id = orders.user_id;
```

### Result
✔ Users who **have orders**  
❌ Users with **no orders** → excluded  
❌ Orders without **valid users** → excluded  

---

## 3️⃣ Using Table Aliases (Recommended)

```sql
SELECT u.name, o.order_date
FROM users u
INNER JOIN orders o
ON u.id = o.user_id;
```

✔ Cleaner  
✔ Easier to read  
✔ Interview‑friendly  

---

## 4️⃣ INNER JOIN with WHERE Clause

```sql
SELECT u.name, o.order_date
FROM users u
JOIN orders o
ON u.id = o.user_id
WHERE o.order_date >= '2025-01-01';
```

📌 `ON` → defines **join condition**  
📌 `WHERE` → filters the **final result**

---

## 5️⃣ INNER JOIN with Multiple Tables

```sql
SELECT s.name, c.title
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id;
```

✔ Very common in **Many‑to‑Many** relationships

---

## ❌ Common Mistakes

- ❌ Forgetting the `ON` condition
- ❌ Using `WHERE` instead of `ON` for join logic
- ❌ Expecting unmatched rows to appear

---

## 🔑 Interview Key Points

- `JOIN` = `INNER JOIN`
- Returns **only matching rows**
- Most commonly used JOIN
- Works with **PK–FK relationships**

---

## 🆚 INNER JOIN vs LEFT JOIN (Quick)

| INNER JOIN | LEFT JOIN |
|-----------|-----------|
| Only matching rows | All left + matching right |
| Excludes NULL matches | Includes NULL matches |
| Most restrictive | More inclusive |

---

## 🧪 Mental Model

**“Show me records that exist in both tables.”**