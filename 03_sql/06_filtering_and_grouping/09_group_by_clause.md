# 🔹 GROUP BY in PostgreSQL

## What is GROUP BY?

`GROUP BY` groups rows that have the **same values** in one or more columns,
so you can apply **aggregate functions** to each group.

```sql
SELECT column, AGG_FUNCTION(column)
FROM table
GROUP BY column;
```

---

## 🔢 Common Aggregate Functions

| Function | What it does   |
| -------- | -------------- |
| COUNT()  | number of rows |
| SUM()    | total          |
| AVG()    | average        |
| MIN()    | minimum        |
| MAX()    | maximum        |

---

## 1️⃣ Basic Example

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

✔ One row per department
✔ Count of employees in each department

---

## 2️⃣ RULE (Very Important 🔥)

Every column in `SELECT` must be **either**:

* in `GROUP BY`, **or**
* inside an aggregate function

### ❌ Wrong

```sql
SELECT department, salary
FROM employees
GROUP BY department;
```

### ✅ Correct

```sql
SELECT department, AVG(salary)
FROM employees
GROUP BY department;
```

---

## 3️⃣ GROUP BY Multiple Columns

```sql
SELECT department, role, COUNT(*)
FROM employees
GROUP BY department, role;
```

✔ Groups by **(department, role)** combination

---

## 4️⃣ GROUP BY with WHERE

`WHERE` filters rows **before** grouping.

```sql
SELECT department, COUNT(*)
FROM employees
WHERE active = true
GROUP BY department;
```

---

## 5️⃣ GROUP BY with HAVING

`HAVING` filters **after** grouping.

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

📌 **Rule**

> Use `WHERE` for rows, `HAVING` for groups.

---

## 6️⃣ GROUP BY with JOIN

```sql
SELECT d.name, COUNT(e.id)
FROM departments d
LEFT JOIN employees e
ON d.id = e.department_id
GROUP BY d.name;
```

✔ Works correctly
✔ `LEFT JOIN` is preserved

---

## 7️⃣ GROUP BY + DISTINCT

Often redundant.

```sql
SELECT department
FROM employees
GROUP BY department;
```

Same as:

```sql
SELECT DISTINCT department
FROM employees;
```

---

## 8️⃣ GROUP BY Expressions

```sql
SELECT DATE(order_date) AS day, COUNT(*)
FROM orders
GROUP BY DATE(order_date);
```

📌 Expression in `SELECT` must **match** `GROUP BY`

---

## 9️⃣ GROUP BY Positional Numbers (Avoid)

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY 1;
```

⚠️ Works, but hurts readability

---

## 🧠 NULL Behavior in GROUP BY

```sql
SELECT manager_id, COUNT(*)
FROM employees
GROUP BY manager_id;
```

✔ All `NULL`s form **one group**

---

## 🧠 Execution Order (Mental Model)

```
FROM / JOIN
→ WHERE
→ GROUP BY
→ HAVING
→ SELECT
→ ORDER BY
→ LIMIT
```

---

## 🧠 Interview Rules to Memorize

* `GROUP BY` creates groups
* Aggregates work **per group**
* `WHERE` filters rows, `HAVING` filters groups
* All non-aggregates must be in `GROUP BY`
* `NULL`s form one group

---

## ✅ One-Line Summary

`GROUP BY` lets you **summarize data by categories** using aggregate functions.
