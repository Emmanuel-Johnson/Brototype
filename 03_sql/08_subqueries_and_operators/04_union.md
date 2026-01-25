# UNION & UNION ALL --- PostgreSQL Made Simple 🚀

`UNION` and `UNION ALL` are **set operators** used to combine the
results of multiple `SELECT` queries.

------------------------------------------------------------------------

## 1️⃣ UNION

### 👉 What it does

`UNION`:

-   Merges result sets
-   Removes duplicate rows (like `DISTINCT`)
-   Keeps **only unique rows**

### ✅ Basic Syntax

``` sql
SELECT column1, column2
FROM table1
UNION
SELECT column1, column2
FROM table2;
```

------------------------------------------------------------------------

### 📌 RULES (Very Important 🔥)

#### 1️⃣ Same number of columns

``` sql
-- ❌ Invalid
SELECT id, name FROM users
UNION
SELECT id FROM admins;
```

✔ Both `SELECT`s must return the **same column count**

------------------------------------------------------------------------

#### 2️⃣ Compatible data types

``` sql
-- ❌ Invalid
SELECT id FROM users
UNION
SELECT name FROM products;
```

❌ `id` (int) and `name` (text) → not compatible\
✔ Data types must be the same or **implicitly castable**

------------------------------------------------------------------------

#### 3️⃣ Column names come from the FIRST SELECT

``` sql
SELECT id AS emp_id FROM employees
UNION
SELECT id FROM managers;
```

✔ Result column name → `emp_id`

------------------------------------------------------------------------

#### 4️⃣ ORDER BY only at the END

``` sql
-- ❌ Invalid
SELECT name FROM a ORDER BY name
UNION
SELECT name FROM b;
```

``` sql
-- ✅ Correct
SELECT name FROM a
UNION
SELECT name FROM b
ORDER BY name;
```

------------------------------------------------------------------------

#### 5️⃣ DISTINCT is automatic

``` sql
SELECT name FROM a
UNION
SELECT name FROM b;
```

✔ Duplicates removed automatically\
❌ Writing `UNION DISTINCT` is pointless (default behavior)

------------------------------------------------------------------------

#### 6️⃣ NULL handling

-   `UNION` treats `NULL = NULL`
-   Duplicate `NULL` rows are removed

------------------------------------------------------------------------

## 2️⃣ UNION ALL

### 👉 What it does

`UNION ALL`:

-   Keeps **all rows**
-   Does **NOT remove duplicates**
-   Faster than `UNION`

### ✅ Syntax

``` sql
SELECT column1 FROM table1
UNION ALL
SELECT column1 FROM table2;
```

------------------------------------------------------------------------

### 🧠 Example

If:

    table1 → A, B, C
    table2 → B, C, D

**UNION result**

    A, B, C, D

**UNION ALL result**

    A, B, C, B, C, D

------------------------------------------------------------------------

### ⚡ Performance Difference

  Operator    Duplicate removal   Speed
  ----------- ------------------- --------
  UNION       Yes                 Slower
  UNION ALL   No                  Faster

------------------------------------------------------------------------

### 👉 Use UNION ALL when:

-   You don't care about duplicates
-   You know results are already unique

------------------------------------------------------------------------

## ⚠️ LIMITATIONS

❌ Cannot use: - `WHERE` across combined results (use subquery) -
Different column counts - Incompatible data types

✔ To filter combined results:

``` sql
SELECT *
FROM (
    SELECT name FROM a
    UNION
    SELECT name FROM b
) t
WHERE name LIKE 'A%';
```

------------------------------------------------------------------------

## 🔥 Exam / Interview One‑Liners

-   `UNION` removes duplicates\
-   `UNION ALL` keeps duplicates\
-   Column count & data types must match\
-   `ORDER BY` goes at the end\
-   Column names come from the first `SELECT`