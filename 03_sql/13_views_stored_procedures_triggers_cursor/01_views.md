## 1️⃣ What is a SQL View?

A **view** is a virtual table based on the result of a SQL query.

-   It does **not store data** (most of the time)
-   It stores **only the query**
-   When you query a view → the DB runs the underlying query

**Think of it like:**

> A saved `SELECT` statement with a table-like name

``` sql
SELECT * FROM employee_view;
```

------------------------------------------------------------------------

## 2️⃣ Creating a View

### Basic Syntax

``` sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

### Example

``` sql
CREATE VIEW emp_basic AS
SELECT emp_id, emp_name, dept_id
FROM employee;
```

``` sql
SELECT * FROM emp_basic;
```

------------------------------------------------------------------------

## Creating or Replacing a View

``` sql
CREATE OR REPLACE VIEW emp_basic AS
SELECT emp_id, emp_name
FROM employee;
```

✔ Replaces the view if it already exists\
✔ Avoids `ERROR: view already exists`

------------------------------------------------------------------------

## Dropping a View

``` sql
DROP VIEW emp_basic;
```

------------------------------------------------------------------------

## 3️⃣ Updating Through Views 🚨

👉 **Not all views are updatable**

### ✅ Updatable View (Simple View)

A view is updatable if: - Based on **one table** - ❌ No `JOIN` - ❌ No
`GROUP BY` - ❌ No aggregate functions (`COUNT`, `SUM`) - ❌ No
`DISTINCT` - ❌ No subqueries

#### Example

``` sql
CREATE VIEW emp_names AS
SELECT emp_id, emp_name
FROM employee;
```

``` sql
UPDATE emp_names
SET emp_name = 'Rahul'
WHERE emp_id = 1;
```

✔ This updates the **employee** table

------------------------------------------------------------------------

### ❌ Non-Updatable View

``` sql
CREATE VIEW emp_dept AS
SELECT e.emp_name, d.dept_name
FROM employee e
JOIN department d ON e.dept_id = d.dept_id;
```

❌ Cannot update because: - Uses `JOIN` - Data comes from multiple
tables

------------------------------------------------------------------------

## WITH CHECK OPTION

Prevents updates that violate the view condition.

``` sql
CREATE VIEW it_emps AS
SELECT * FROM employee
WHERE dept_id = 10
WITH CHECK OPTION;
```

❌ This will fail:

``` sql
UPDATE it_emps
SET dept_id = 20
WHERE emp_id = 5;
```

------------------------------------------------------------------------

## 4️⃣ Types of Views

### 🔹 Simple View

-   One table
-   Often updatable

### 🔹 Complex View

-   Multiple tables
-   Aggregates / joins
-   Not updatable

### 🔹 Materialized View (Concept)

-   Stores data physically
-   Faster reads
-   Needs refresh\
    *(Used in PostgreSQL, Oracle)*

------------------------------------------------------------------------

## 5️⃣ Use Cases of Views 💡

### 🔐 1. Security

Expose only required columns

``` sql
CREATE VIEW emp_public AS
SELECT emp_id, emp_name
FROM employee;
```

Users don't see salary 👀

------------------------------------------------------------------------

### 🧹 2. Simplicity

Hide complex joins

``` sql
SELECT * FROM emp_dept_view;
```

Instead of writing joins every time

------------------------------------------------------------------------

### 🔄 3. Data Abstraction

Underlying table changes → view stays same\
*(Helps logical data independence 🔥)*

------------------------------------------------------------------------

### 📊 4. Reporting

-   Predefined queries for reports

------------------------------------------------------------------------

### ♻ 5. Reusability

-   Write once, use everywhere

------------------------------------------------------------------------

## 6️⃣ Views vs Tables (Quick)

  Table              View
  ------------------ ----------------
  Stores data        Stores query
  Uses disk          Mostly virtual
  Slower to change   Easy to modify