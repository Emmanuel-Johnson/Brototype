# 🔢 Comparison Operators in PostgreSQL

## Operator Overview

| Operator | Meaning               | Notes                  |
| -------- | --------------------- | ---------------------- |
| =        | equal to              | most common            |
| !=       | not equal to          | PostgreSQL supports it |
| <>       | not equal to          | SQL-standard           |
| <        | less than             |                        |
| >        | greater than          |                        |
| <=       | less than or equal    |                        |
| >=       | greater than or equal |                        |

---

## 1️⃣ Equal To (`=`)

```sql
SELECT *
FROM employees
WHERE department = 'IT';
```

✔ Works for numbers, text, dates
❌ Does **NOT** work with `NULL`

---

## 2️⃣ Not Equal (`!=` and `<>`)

Both are **identical** in PostgreSQL.

```sql
WHERE salary != 50000;
```

```sql
WHERE salary <> 50000;
```

📌 Prefer `<>` in interviews (ANSI SQL).
`!=` is perfectly fine in daily work.

---

## ⚠️ NULL + Comparison = Trap

```sql
WHERE bonus != 1000;
```

❌ Rows where `bonus` is `NULL` are **NOT returned**

Because:

```
NULL != 1000 → UNKNOWN
```

---

## 🔥 PostgreSQL-Safe Alternative

### IS DISTINCT FROM

```sql
WHERE bonus IS DISTINCT FROM 1000;
```

✔ Returns rows where:

* `bonus ≠ 1000`
* `bonus IS NULL`

---

### IS NOT DISTINCT FROM

```sql
WHERE bonus IS NOT DISTINCT FROM 1000;
```

✔ Matches:

* `bonus = 1000`
* `NULL = NULL`

---

## 3️⃣ Greater / Less Than

```sql
WHERE salary > 60000;
WHERE salary < 30000;
```

---

## 4️⃣ Greater / Less Than or Equal

```sql
WHERE joining_date >= '2024-01-01';
WHERE age <= 30;
```

---

## 5️⃣ Date Comparisons (Very Common)

```sql
WHERE order_date > CURRENT_DATE;
```

```sql
WHERE created_at >= NOW() - INTERVAL '7 days';
```

---

## 6️⃣ String Comparisons

PostgreSQL compares strings **lexicographically**.

```sql
WHERE name > 'M';
```

📌 Result depends on **collation**

```sql
SHOW LC_COLLATE;
```

---

## 7️⃣ Comparison in JOIN Conditions

```sql
SELECT e.name, m.name
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.id;
```

👉 Any comparison operator can be used inside `ON`.

---

## 8️⃣ Comparison in CASE Expressions

```sql
SELECT name,
       CASE
         WHEN salary >= 80000 THEN 'High'
         WHEN salary >= 50000 THEN 'Medium'
         ELSE 'Low'
       END AS salary_level
FROM employees;
```

---

## 🧠 Interview-Grade Rules to Remember

### 🔑 Rule 1

`=` and `!=` do **not** work with `NULL`

Use:

* `IS NULL`
* `IS NOT NULL`
* `IS DISTINCT FROM`

---

### 🔑 Rule 2

`!=` and `<>` are the **same** in PostgreSQL

---

### 🔑 Rule 3

Comparisons return:

* `TRUE`
* `FALSE`
* `UNKNOWN`

Only **TRUE** rows survive `WHERE`.

---

## ✅ Quick Cheat Sheet

```
=    equal
!=   not equal
<>   not equal (standard)
<    less than
>    greater than
<=   less than or equal
>=   greater than or equal
IS DISTINCT FROM   -- NULL-safe not equal
```
