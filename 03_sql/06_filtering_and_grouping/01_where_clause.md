# 🔍 What is the WHERE clause?

The **WHERE clause** filters rows **after FROM/JOIN** but **before SELECT output**.

```sql
SELECT columns
FROM table
WHERE condition;
```

👉 Only rows where the condition is **TRUE** are returned.

---

## 🧱 Basic Examples

### 1️⃣ Simple condition

```sql
SELECT *
FROM employees
WHERE salary > 50000;
```

---

### 2️⃣ Multiple conditions (AND, OR)

```sql
SELECT *
FROM employees
WHERE department = 'IT'
AND salary >= 60000;
```

```sql
SELECT *
FROM employees
WHERE department = 'HR'
OR department = 'Finance';
```

---

## 3️⃣ Comparison Operators

| Operator  | Meaning     |
| --------- | ----------- |
| =         | equal       |
| != or <>  | not equal   |
| > < >= <= | comparisons |

```sql
SELECT *
FROM products
WHERE price != 100;
```

---

## ⚠️ NULL Handling (VERY IMPORTANT)

### ❌ This does NOT work

```sql
WHERE column = NULL;
```

### ✅ Correct way

```sql
WHERE column IS NULL;
WHERE column IS NOT NULL;
```

---

## 🔥 IS DISTINCT FROM (PostgreSQL Special)

Handles `NULL` **safely**.

```sql
WHERE column IS DISTINCT FROM 'XL';
```

Rules:

* `NULL ≠ 'XL'` ✅
* `NULL ≠ NULL` ❌ (treated as equal)

👉 Much safer than `!=`

---

## 🧮 BETWEEN, IN, LIKE

### BETWEEN

```sql
WHERE salary BETWEEN 30000 AND 60000;
```

---

### IN

```sql
WHERE department IN ('IT', 'HR', 'Finance');
```

---

### LIKE (Pattern Matching)

```sql
WHERE name LIKE 'A%';   -- starts with A
WHERE name LIKE '%son'; -- ends with son
```

Case-insensitive (PostgreSQL):

```sql
WHERE name ILIKE 'a%';
```

---

## 🔗 WHERE with JOINs (Common Confusion Area)

### INNER JOIN → WHERE is safe

```sql
SELECT u.name, o.id
FROM users u
INNER JOIN orders o
ON u.id = o.user_id
WHERE o.status = 'PAID';
```

---

### ⚠️ LEFT JOIN + WHERE = Danger Zone

```sql
SELECT u.name, o.id
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
WHERE o.status = 'PAID';
```

🔴 This **kills unmatched rows** → becomes an **INNER JOIN**

---

### ✅ Correct Way

```sql
SELECT u.name, o.id
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
AND o.status = 'PAID';
```

📌 **Rule to remember**

> Conditions on the **right table** of a LEFT JOIN go in **ON**, not WHERE.

---

## 🧠 Order of Execution (Mental Model)

```
FROM
→ JOIN / ON
→ WHERE
→ SELECT
→ ORDER BY
→ LIMIT
```

---

## 🧪 Common Interview Patterns

### Find rows with no match

```sql
SELECT u.name
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
WHERE o.id IS NULL;
```

---

### Filter after aggregation → use HAVING (not WHERE)

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

---

## ✅ One-line Summary

* WHERE filters rows
* ON defines join matching
* WHERE + LEFT JOIN can silently turn into INNER JOIN
* Use `IS NULL`, not `= NULL`
* Prefer `IS DISTINCT FROM` over `!=`
