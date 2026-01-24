# 🔹 BETWEEN in PostgreSQL

## What is BETWEEN?

`BETWEEN` checks whether a value falls **within a range (inclusive)**.

```sql
WHERE column BETWEEN lower AND upper;
```

Equivalent to:

```sql
WHERE column >= lower
AND column <= upper;
```

---

## 1️⃣ Numeric Example

```sql
SELECT *
FROM employees
WHERE salary BETWEEN 30000 AND 60000;
```

✔ Includes **30000** and **60000**

---

## 2️⃣ Date Example (Very Common)

```sql
SELECT *
FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-01-31';
```

✔ Includes both dates

---

## ⚠️ Timestamp Trap (Interview Favorite)

```sql
WHERE created_at BETWEEN '2025-01-01' AND '2025-01-31';
```

❌ This **excludes**:

```
2025-01-31 10:30:00
```

Why?

```
'2025-01-31' = 2025-01-31 00:00:00
```

---

## ✅ Correct Timestamp Range (Best Practice)

```sql
WHERE created_at >= '2025-01-01'
AND created_at <  '2025-02-01';
```

📌 **Rule**

> For timestamps, prefer `>= start` AND `< next_day`

---

## 3️⃣ Text / String Example

PostgreSQL compares strings **lexicographically**.

```sql
WHERE name BETWEEN 'A' AND 'M';
```

✔ Includes names starting with A–M
⚠️ Result depends on **collation**

👉 Rarely used in production

---

## 4️⃣ NOT BETWEEN

```sql
SELECT *
FROM employees
WHERE salary NOT BETWEEN 30000 AND 60000;
```

Equivalent to:

```sql
WHERE salary < 30000
OR salary > 60000;
```

---

## ⚠️ BETWEEN + NULL

```sql
WHERE bonus BETWEEN 1000 AND 5000;
```

❌ If `bonus` is `NULL` → row is excluded

Because:

```
NULL BETWEEN x AND y → UNKNOWN
```

---

## 5️⃣ BETWEEN in JOIN

```sql
SELECT *
FROM orders o
JOIN promotions p
ON o.order_date BETWEEN p.start_date AND p.end_date;
```

---

## 6️⃣ BETWEEN in CASE

```sql
SELECT name,
       CASE
         WHEN salary BETWEEN 0 AND 30000 THEN 'Low'
         WHEN salary BETWEEN 30001 AND 60000 THEN 'Medium'
         ELSE 'High'
       END AS salary_level
FROM employees;
```

---

## 🧠 Interview Rules to Remember

### 🔑 Rule 1

`BETWEEN` is **inclusive** on both ends

---

### 🔑 Rule 2

`BETWEEN` is just syntax sugar for `>=` and `<=`

---

### 🔑 Rule 3

Avoid `BETWEEN` with **timestamps**

Use:

```sql
>= start AND < end
```

---

### 🔑 Rule 4

Order matters:

```sql
BETWEEN 10 AND 5  -- returns no rows
```

---

## ✅ Quick Cheat Sheet

```
BETWEEN a AND b      -- a <= x <= b
NOT BETWEEN a AND b  -- x < a OR x > b
```

---

## ✅ One-line Summary

Use `BETWEEN` for clean inclusive ranges — but **never blindly with timestamps**.
