# 🔹 NULL in PostgreSQL

## What is NULL?

`NULL` means **unknown / missing / not available**.

It is **NOT**:

* `0`
* empty string `''`
* `FALSE`

---

## ❌ What You Must NEVER Do

```sql
WHERE column = NULL;
WHERE column != NULL;
```

These **always fail**.

Because:

```
column = NULL → UNKNOWN
```

📌 `WHERE` keeps **only TRUE** rows.

---

## ✅ Correct Way: IS NULL

```sql
SELECT *
FROM employees
WHERE manager_id IS NULL;
```

✔ Finds employees **without a manager**

---

## ✅ Correct Way: IS NOT NULL

```sql
SELECT *
FROM employees
WHERE email IS NOT NULL;
```

✔ Finds employees **with an email**

---

## 🧠 Why IS NULL Works

* `IS NULL` is **not** a comparison operator
* It is a **predicate designed specifically for NULL checking**

---

## 🔗 NULL with JOINs (VERY Important)

### Find Rows with NO Match (Classic Pattern)

```sql
SELECT u.name
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
WHERE o.id IS NULL;
```

✔ Users with **no orders**

---

### ❌ Common Mistake

```sql
WHERE o.id = NULL;
```

Always wrong ❌

---

## ⚠️ NULL and Logical Operators

| Expression    | Result  |
| ------------- | ------- |
| NULL = NULL   | UNKNOWN |
| NULL <> NULL  | UNKNOWN |
| NULL AND TRUE | UNKNOWN |
| NULL OR TRUE  | TRUE    |
| NOT NULL      | UNKNOWN |

📌 Only **TRUE** survives `WHERE`.

---

## 🔥 PostgreSQL Superpower: IS DISTINCT FROM

```sql
WHERE column IS DISTINCT FROM 10;
```

✔ TRUE when:

* value ≠ 10
* value IS NULL

---

### Opposite: IS NOT DISTINCT FROM

```sql
WHERE column IS NOT DISTINCT FROM 10;
```

✔ TRUE when:

* value = 10
* value IS NULL

---

## 🧪 NULL in Aggregates

```sql
SELECT COUNT(bonus) FROM employees;
```

✔ Counts **only non-NULL** values

```sql
SELECT COUNT(*) FROM employees;
```

✔ Counts **all rows**

---

## 🧮 NULL Handling Functions

### COALESCE

```sql
SELECT COALESCE(bonus, 0) FROM employees;
```

✔ Replaces `NULL` with `0`

---

### NULLIF

```sql
SELECT NULLIF(score, 0);
```

✔ Returns `NULL` if `score = 0`

---

## 🧠 Interview Rules to Memorize

### 🔑 Rule 1

Use `IS NULL` / `IS NOT NULL`, **never** `= NULL`

---

### 🔑 Rule 2

`NULL` breaks:

* `=`
* `!=`
* `IN`
* `NOT IN`

---

### 🔑 Rule 3

`LEFT JOIN + IS NULL` = find missing rows

---

## ✅ One-Line Summary

`NULL` means **unknown** — compare it only with `IS NULL` or `IS NOT NULL`.
