# 🔹 IN / NOT IN in PostgreSQL

## What is IN / NOT IN?

They let you compare **one value against multiple values**.

Instead of:

```sql
WHERE department = 'IT'
   OR department = 'HR'
   OR department = 'Finance';
```

Use:

```sql
WHERE department IN ('IT', 'HR', 'Finance');
```

✔ Cleaner
✔ Easier to read
✔ Same result

---

## 1️⃣ IN — Match Any Value

### Basic syntax

```sql
WHERE column IN (value1, value2, value3);
```

### Example

```sql
SELECT *
FROM employees
WHERE department IN ('IT', 'HR');
```

✔ Returns rows where department is **IT or HR**

---

## 2️⃣ NOT IN — Exclude Values

```sql
SELECT *
FROM employees
WHERE department NOT IN ('HR', 'Finance');
```

✔ Returns employees **not** in HR or Finance

---

## ⚠️ BIG TRAP: NOT IN + NULL

### Example data

```
department
----------
IT
HR
NULL
```

### Query

```sql
WHERE department NOT IN ('HR');
```

### ❌ Result

* IT ❌ (unexpected)
* NULL ❌ (very surprising)

### Why?

```
NULL NOT IN ('HR') → UNKNOWN
```

📌 `WHERE` keeps **only TRUE** rows.

---

## ✅ SAFE Alternatives (Very Important)

### 🔥 Best: IS DISTINCT FROM

```sql
WHERE department IS DISTINCT FROM 'HR';
```

✔ Handles `NULL` correctly

---

### Or explicitly handle NULL

```sql
WHERE department NOT IN ('HR')
OR department IS NULL;
```

---

## 3️⃣ IN with Subquery (Very Common)

```sql
SELECT name
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'Bangalore'
);
```

---

## ⚠️ Subquery NULL Problem (NOT IN)

```sql
WHERE id NOT IN (
    SELECT manager_id
    FROM employees
);
```

❌ If `manager_id` contains `NULL` → **returns NOTHING**

---

## ✅ Correct Way: NOT EXISTS

```sql
SELECT e.name
FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM employees m
    WHERE m.manager_id = e.id
);
```

📌 **Interview Rule**

> Use `NOT EXISTS`, not `NOT IN`, when `NULL` is possible.

---

## 4️⃣ IN vs EXISTS (Quick Intuition)

| IN                  | EXISTS           |
| ------------------- | ---------------- |
| Compares values     | Checks existence |
| Simple lists        | Correlated logic |
| Can break with NULL | NULL-safe        |

👉 PostgreSQL optimizer is smart — performance is usually similar.

---

## 5️⃣ IN with Expressions

```sql
WHERE EXTRACT(YEAR FROM joining_date) IN (2023, 2024, 2025);
```

---

## 6️⃣ IN with Enums / Constants

```sql
WHERE status IN ('ACTIVE', 'PENDING');
```

---

## 🧠 Interview Cheat Rules

✅ Use `IN` when:

* Matching against a known list
* Subquery cannot return `NULL` (or you control it)

❌ Avoid `NOT IN` when:

* Subquery might return `NULL`

✅ Prefer:

* `NOT EXISTS`
* `IS DISTINCT FROM`

---

## ✅ One-line Summary

* `IN` = multiple ORs
* `NOT IN + NULL` = danger
* Subquery + `NOT IN` ❌
* `NOT EXISTS` = safe
* `IS DISTINCT FROM` = PostgreSQL superpower
