# 🔹 DISTINCT in PostgreSQL

## What is DISTINCT?

`DISTINCT` removes **duplicate rows** from the result set.

```sql
SELECT DISTINCT column
FROM table;
```

📌 PostgreSQL checks the **entire selected row**, not just one column (unless you select only one column).

---

## 1️⃣ DISTINCT on One Column

```sql
SELECT DISTINCT department
FROM employees;
```

✔ Returns each department **once**

---

## 2️⃣ DISTINCT on Multiple Columns

```sql
SELECT DISTINCT department, role
FROM employees;
```

✔ Returns unique **(department, role)** combinations

📌 If **either column differs**, the row is considered unique

---

## 3️⃣ DISTINCT with NULL

```sql
SELECT DISTINCT manager_id
FROM employees;
```

✔ `NULL` appears **only once**

Because:

> All `NULL`s are considered **equal** for `DISTINCT`

---

## 4️⃣ DISTINCT vs GROUP BY (Very Important)

These are equivalent:

```sql
SELECT DISTINCT department
FROM employees;
```

```sql
SELECT department
FROM employees
GROUP BY department;
```

---

### When GROUP BY is Required

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

👉 Use `GROUP BY` when **aggregating**

---

## 5️⃣ DISTINCT with Expressions

```sql
SELECT DISTINCT LOWER(email)
FROM users;
```

✔ Removes duplicates **after applying the expression**

---

## 6️⃣ DISTINCT + ORDER BY

```sql
SELECT DISTINCT department
FROM employees
ORDER BY department;
```

✔ Valid

---

### ⚠️ DISTINCT + ORDER BY Trap

```sql
SELECT DISTINCT department
FROM employees
ORDER BY salary;  -- ❌ ERROR
```

❌ `ORDER BY` columns must appear in `SELECT` when using `DISTINCT`

---

## 🔥 PostgreSQL-Only: DISTINCT ON

This is **huge** for interviews and real projects.

### Syntax

```sql
SELECT DISTINCT ON (column)
       column, other_columns
FROM table
ORDER BY column, sort_column;
```

---

### Example: Latest Order per User

```sql
SELECT DISTINCT ON (user_id)
       user_id, order_id, order_date
FROM orders
ORDER BY user_id, order_date DESC;
```

✔ One row per `user_id`
✔ Picks the **latest order** because of `ORDER BY`

📌 **ORDER BY decides which row survives** per group

---

## ⚠️ DISTINCT ON Rules (Memorize)

* `DISTINCT ON (x)` columns must come **first** in `ORDER BY`
* `ORDER BY` controls **which row you keep**
* PostgreSQL-only (not standard SQL)

---

## 7️⃣ DISTINCT in Aggregates

```sql
SELECT COUNT(DISTINCT department)
FROM employees;
```

✔ Counts unique departments

```sql
SELECT SUM(DISTINCT salary)
FROM employees;
```

✔ Sums unique salaries

---

## 🧠 Performance Note

* `DISTINCT` requires **sorting or hashing**
* Can be expensive on large datasets
* Indexes can help, but don’t always save you

---

## 🧠 Interview Rules to Remember

* `DISTINCT` removes duplicate rows
* `NULL` appears once
* `DISTINCT ON + ORDER BY` is PostgreSQL magic
* `DISTINCT ≠ GROUP BY` (but often similar)
* `ORDER BY` columns must be in `SELECT`

---

## ✅ One-Line Summary

`DISTINCT` removes duplicates, and `DISTINCT ON` lets you choose **which duplicate survives**.
