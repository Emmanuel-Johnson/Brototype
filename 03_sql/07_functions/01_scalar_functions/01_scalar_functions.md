# 🔹 Scalar Functions in PostgreSQL

Scalar functions operate on **one row at a time** and return **one value per row**.

---

## 1️⃣ String Functions

Used to manipulate `TEXT / VARCHAR` values.

| Function      | Purpose              | Example                             |
| ------------- | -------------------- | ----------------------------------- |
| `UPPER()`     | Convert to uppercase | `UPPER('sql') → 'SQL'`              |
| `LOWER()`     | Convert to lowercase | `LOWER('SQL') → 'sql'`              |
| `LENGTH()`    | String length        | `LENGTH('Postgres') → 8`            |
| `SUBSTRING()` | Extract part         | `SUBSTRING('abcdef', 2, 3) → 'bcd'` |
| `CONCAT()`    | Join strings         | `CONCAT('Hello', ' ', 'SQL')`       |
| `TRIM()`      | Remove spaces        | `TRIM(' hi ') → 'hi'`               |
| `REPLACE()`   | Replace text         | `REPLACE('a-b', '-', ':')`          |

---

## 2️⃣ Numeric Functions

Used for mathematical calculations.

| Function    | Purpose            | Example                |
| ----------- | ------------------ | ---------------------- |
| `ABS()`     | Absolute value     | `ABS(-10) → 10`        |
| `ROUND()`   | Round number       | `ROUND(4.56, 1) → 4.6` |
| `CEILING()` | Round up           | `CEILING(4.2) → 5`     |
| `FLOOR()`   | Round down         | `FLOOR(4.8) → 4`       |
| `POWER()`   | Exponent           | `POWER(2, 3) → 8`      |
| `MOD()`     | Remainder          | `MOD(10, 3) → 1`       |
| `RANDOM()`  | Random value (0–1) | `RANDOM()`             |

✔ Works with `INT`, `DECIMAL`, `NUMERIC`, `FLOAT`

---

## 3️⃣ Date / Time Functions

Used to work with dates, times, and timestamps.

| Function       | Purpose                  | Example                     |
| -------------- | ------------------------ | --------------------------- |
| `CURRENT_DATE` | Today’s date             | `2026-01-25`                |
| `CURRENT_TIME` | Current time             | —                           |
| `NOW()`        | Current timestamp        | —                           |
| `AGE()`        | Difference between dates | `AGE(NOW(), '2000-01-01')`  |
| `EXTRACT()`    | Get part of date         | `EXTRACT(YEAR FROM NOW())`  |
| `DATE_PART()`  | Same as extract          | `DATE_PART('month', NOW())` |

---

## 4️⃣ NULL Handling Functions

Used to handle missing (`NULL`) values.

| Function      | Purpose              | Example                     |
| ------------- | -------------------- | --------------------------- |
| `COALESCE()`  | First non-NULL value | `COALESCE(NULL, 5, 10) → 5` |
| `NULLIF()`    | Return NULL if equal | `NULLIF(5, 5) → NULL`       |
| `IS NULL`     | Check NULL           | `salary IS NULL`            |
| `IS NOT NULL` | Check non-NULL       | `salary IS NOT NULL`        |

🔥 **`COALESCE()` is extremely important for interviews**

---

## 5️⃣ Conditional Functions

Used for logic and conditions.

| Function     | Purpose           | Example                 |
| ------------ | ----------------- | ----------------------- |
| `CASE`       | Conditional logic | See below               |
| `GREATEST()` | Largest value     | `GREATEST(3, 7, 2) → 7` |
| `LEAST()`    | Smallest value    | `LEAST(3, 7, 2) → 2`    |

### CASE Example

```sql
SELECT
  salary,
  CASE
    WHEN salary > 50000 THEN 'High'
    ELSE 'Low'
  END AS salary_level
FROM employees;
```

✔ Evaluated **row by row**

---

## 6️⃣ Type Conversion Functions

Used to convert data types.

| Function      | Purpose              | Example                               |
| ------------- | -------------------- | ------------------------------------- |
| `CAST()`      | Convert type         | `CAST('123' AS INT)`                  |
| `::`          | PostgreSQL shorthand | `'123'::INT`                          |
| `TO_CHAR()`   | Date/number → text   | `TO_CHAR(NOW(), 'YYYY-MM-DD')`        |
| `TO_DATE()`   | Text → date          | `TO_DATE('2026-01-25', 'YYYY-MM-DD')` |
| `TO_NUMBER()` | Text → number        | `TO_NUMBER('123.45', '999.99')`       |

---

## 🧠 Quick Interview Line

> **Scalar functions operate on each row individually and return one value per row, unlike aggregate functions which operate on multiple rows.**

---

✅ Perfect for **PostgreSQL interviews & quick revision**
