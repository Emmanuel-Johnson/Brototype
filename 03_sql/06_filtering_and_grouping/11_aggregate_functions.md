## 🔹 What are aggregate functions?

Aggregate functions take multiple rows and return one value.

They are usually used with `GROUP BY`, but can also work on the whole
table.

------------------------------------------------------------------------

## 🧮 The Big Five Aggregates

### 1️⃣ COUNT()

Counts rows.

**Count all rows**

``` sql
SELECT COUNT(*)
FROM employees;
```

✔ Includes NULLs\
✔ Fastest & safest

**Count non-NULL values**

``` sql
SELECT COUNT(email)
FROM employees;
```

✔ Ignores NULLs in `email`

**Count unique values**

``` sql
SELECT COUNT(DISTINCT department)
FROM employees;
```

------------------------------------------------------------------------

### 2️⃣ SUM()

Adds numeric values.

``` sql
SELECT SUM(salary)
FROM employees;
```

✔ Ignores NULLs\
❌ Works only on numeric columns

**With GROUP BY**

``` sql
SELECT department, SUM(salary)
FROM employees
GROUP BY department;
```

------------------------------------------------------------------------

### 3️⃣ AVG()

Returns average value.

``` sql
SELECT AVG(salary)
FROM employees;
```

✔ Ignores NULLs\
✔ Returns numeric (often decimal)

**Rounded average**

``` sql
SELECT ROUND(AVG(salary), 2)
FROM employees;
```

------------------------------------------------------------------------

### 4️⃣ MIN()

Smallest value.

``` sql
SELECT MIN(salary)
FROM employees;
```

✔ Works with: - numbers - dates - text (lexicographical)

------------------------------------------------------------------------

### 5️⃣ MAX()

Largest value.

``` sql
SELECT MAX(salary)
FROM employees;
```

✔ Same behavior as `MIN()`

------------------------------------------------------------------------

## 🔗 Aggregates + GROUP BY (most common)

``` sql
SELECT department,
       COUNT(*)    AS total_employees,
       AVG(salary) AS avg_salary,
       MIN(salary) AS min_salary,
       MAX(salary) AS max_salary
FROM employees
GROUP BY department;
```

------------------------------------------------------------------------

## 🧠 NULL behavior (VERY IMPORTANT)

  Function     NULL handling
  ------------ ---------------
  COUNT(\*)    counts rows
  COUNT(col)   ignores NULL
  SUM()        ignores NULL
  AVG()        ignores NULL
  MIN()        ignores NULL
  MAX()        ignores NULL

📌 If all values are NULL, result = **NULL** (except `COUNT(*)`)

------------------------------------------------------------------------

## 🔥 Aggregates + WHERE vs HAVING

**WHERE** → before grouping

``` sql
WHERE active = true
```

**HAVING** → after grouping

``` sql
HAVING AVG(salary) > 50000;
```

------------------------------------------------------------------------

## ⚠️ Common mistakes (interview traps)

❌ Using aggregates in WHERE

``` sql
WHERE COUNT(*) > 5;
```

✅ Correct

``` sql
HAVING COUNT(*) > 5;
```

❌ Selecting non-grouped column

``` sql
SELECT department, salary, COUNT(*)
FROM employees
GROUP BY department;
```

------------------------------------------------------------------------

## 🧪 Aggregates with JOIN

``` sql
SELECT d.name, COUNT(e.id)
FROM departments d
LEFT JOIN employees e
ON d.id = e.department_id
GROUP BY d.name;
```

✔ Preserves departments with zero employees

------------------------------------------------------------------------

## 🧠 Execution order reminder

    FROM / JOIN
    → WHERE
    → GROUP BY
    → HAVING
    → SELECT
    → ORDER BY
    → LIMIT

------------------------------------------------------------------------

## 🧠 Interview rules to memorize

-   Aggregates collapse rows into one value\
-   Use `GROUP BY` for per-category aggregates\
-   `COUNT(*) ≠ COUNT(column)`\
-   Aggregates ignore NULLs (mostly)\
-   Use `HAVING` for aggregate filters

------------------------------------------------------------------------

## ✅ One-line summary

**Aggregate functions summarize data --- COUNT counts, SUM adds, AVG
averages, MIN/MAX find extremes.**