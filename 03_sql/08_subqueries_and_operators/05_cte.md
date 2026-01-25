# WITH Clause & CTE (Common Table Expression) --- PostgreSQL 🧩

Think of a **CTE** as a temporary named result set that exists only for
one query.\
The `WITH` clause is how you define it.

------------------------------------------------------------------------

## 1️⃣ What is WITH / CTE?

### 👉 Definition

A **CTE (Common Table Expression)**:

-   Is defined using the `WITH` clause\
-   Acts like a temporary table\
-   Improves **readability**, **reusability**, and **debugging**

### ✅ Basic Syntax

``` sql
WITH cte_name AS (
    SELECT columns
    FROM table
    WHERE condition
)
SELECT *
FROM cte_name;
```

------------------------------------------------------------------------

## 2️⃣ Simple Example

``` sql
WITH high_salary_emps AS (
    SELECT id, name, salary
    FROM employees
    WHERE salary > 50000
)
SELECT name, salary
FROM high_salary_emps;
```

### 🧠 Meaning

First create a temporary result `high_salary_emps`,\
then query from it like a table.

------------------------------------------------------------------------

## 3️⃣ Why use CTE? (Very important 🔥)

### ✔ Readability

**Without CTE (messy):**

``` sql
SELECT dept, AVG(salary)
FROM employees
WHERE dept IN (
    SELECT dept
    FROM employees
    WHERE salary > 50000
)
GROUP BY dept;
```

**With CTE (clean):**

``` sql
WITH rich_emps AS (
    SELECT dept
    FROM employees
    WHERE salary > 50000
)
SELECT dept, AVG(salary)
FROM employees
WHERE dept IN (SELECT dept FROM rich_emps)
GROUP BY dept;
```

------------------------------------------------------------------------

### ✔ Reuse same subquery multiple times

``` sql
WITH stats AS (
    SELECT dept, COUNT(*) cnt
    FROM employees
    GROUP BY dept
)
SELECT *
FROM stats
WHERE cnt > 5;
```

------------------------------------------------------------------------

### ✔ Easier debugging

You can run the CTE query alone to test it.

------------------------------------------------------------------------

## 4️⃣ Multiple CTEs

``` sql
WITH dept_count AS (
    SELECT department_id, COUNT(*) cnt
    FROM employees
    GROUP BY department_id
),
high_dept AS (
    SELECT department_id
    FROM dept_count
    WHERE cnt > 5
)
SELECT *
FROM employees
WHERE department_id IN (SELECT department_id FROM high_dept);
```

✔ CTEs are evaluated **top to bottom**

------------------------------------------------------------------------

## 5️⃣ CTE vs Subquery

  Feature       CTE         Subquery
  ------------- ----------- -----------
  Readability   ✅ High     ❌ Low
  Reusability   ✅ Yes      ❌ No
  Debugging     ✅ Easy     ❌ Hard
  Scope         One query   One query

------------------------------------------------------------------------

## 6️⃣ Recursive CTE (advanced but important 💡)

Used for **hierarchical data** (tree, parent-child).

### Example: Employee--Manager hierarchy

``` sql
WITH RECURSIVE emp_tree AS (
    -- anchor
    SELECT id, name, manager_id
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- recursive
    SELECT e.id, e.name, e.manager_id
    FROM employees e
    JOIN emp_tree t
      ON e.manager_id = t.id
)
SELECT * FROM emp_tree;
```

### 🧠 Meaning

-   Start from top-level managers\
-   Keep joining employees under them

------------------------------------------------------------------------

## 7️⃣ Important Rules & Notes ⚠️

✔ CTE exists only during query execution\
✔ Cannot create index on a CTE\
✔ Column names can be specified

``` sql
WITH cte_name(col1, col2) AS (...)
```

✔ In PostgreSQL: - Before **PG 12** → CTEs were **optimization
fences** - From **PG 12+** → Planner can inline CTEs (better
performance)

------------------------------------------------------------------------

## 🔥 Interview One-Liners

-   CTE = temporary named result\
-   `WITH` defines a CTE\
-   Improves readability & reuse\
-   Recursive CTE handles hierarchy