# EXISTS, ANY, ALL --- PostgreSQL Made Simple 🚀

These three are **subquery operators**. They're used when you want to
compare a value with the result of another query.

------------------------------------------------------------------------

## 1️⃣ EXISTS

### 👉 What it does

`EXISTS` checks whether a subquery returns **at least one row**.

-   Returns **TRUE** → if subquery has any row\
-   Returns **FALSE** → if subquery has no rows\
-   It does **NOT care about values**, only row existence

### ✅ Syntax

``` sql
SELECT *
FROM employees e
WHERE EXISTS (
    SELECT 1
    FROM departments d
    WHERE d.id = e.department_id
);
```

### 🧠 Meaning (plain English)

> "Give me employees who belong to a department that exists"

✔ Stops as soon as one row is found (very fast)\
✔ Commonly used with **correlated subqueries**

------------------------------------------------------------------------

## 2️⃣ ANY

### 👉 What it does

`ANY` compares a value with **each value** returned by a subquery.

-   Condition is **TRUE if it matches at least one value**

### ✅ Syntax

``` sql
value operator ANY (subquery)
```

### 📌 Example

``` sql
SELECT *
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department = 'HR'
);
```

### 🧠 Meaning

> "Employees whose salary is greater than at least one HR employee's
> salary"

If HR salaries = `(30000, 40000, 50000)`\
✔ `salary > ANY` → `salary > 30000`

### ⚠️ Important notes

-   `= ANY` works like `IN`

``` sql
salary = ANY (SELECT salary FROM employees);
```

Same as:

``` sql
salary IN (SELECT salary FROM employees);
```

-   If subquery returns **only NULL** → result is **UNKNOWN**

------------------------------------------------------------------------

## 3️⃣ ALL

### 👉 What it does

`ALL` compares a value with **every value** returned by a subquery.

-   Condition is **TRUE only if it satisfies all comparisons**

### ✅ Syntax

``` sql
value operator ALL (subquery)
```

### 📌 Example

``` sql
SELECT *
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department = 'HR'
);
```

### 🧠 Meaning

> "Employees whose salary is greater than every HR employee's salary"

If HR salaries = `(30000, 40000, 50000)`\
✔ `salary > ALL` → `salary > 50000`

### ⚠️ Special cases

-   If subquery returns **no rows**:
    -   `> ALL` → **TRUE**
    -   `< ALL` → **TRUE**
-   If subquery contains **NULL** → result may become **UNKNOWN**

------------------------------------------------------------------------

## 🔥 Quick Comparison Table

  Operator   Meaning              Passes when
  ---------- -------------------- --------------------------------
  EXISTS     Any row exists       Subquery returns ≥ 1 row
  ANY        At least one match   Condition true for one value
  ALL        All must match       Condition true for every value

------------------------------------------------------------------------

## 🧠 Mental shortcut (exam‑friendly)

-   **EXISTS** → *Does it exist?*\
-   **ANY** → *At least one*\
-   **ALL** → *Every single one*