# Stored Procedures -- Complete Notes

## 1️⃣ What is a Stored Procedure?

A **stored procedure** is a named block of SQL code stored in the
database that can:

-   Contain multiple SQL statements
-   Accept parameters
-   Include logic (`IF`, `LOOP`, `WHILE`)
-   Be reused many times

📌 **In short:**

> A stored program that runs inside the database

------------------------------------------------------------------------

## 2️⃣ Creating Stored Procedures

⚠️ Syntax depends on the database. Below is **generic SQL + PostgreSQL
style**.

### 🔹 Basic Stored Procedure (No Parameters)

``` sql
CREATE PROCEDURE get_all_employees()
LANGUAGE SQL
AS $$
    SELECT * FROM employee;
$$;
```

------------------------------------------------------------------------

### 🔹 Stored Procedure with Parameters

``` sql
CREATE PROCEDURE get_emp_by_dept(IN d_id INT)
LANGUAGE SQL
AS $$
    SELECT * FROM employee
    WHERE dept_id = d_id;
$$;
```

------------------------------------------------------------------------

### 🔹 Stored Procedure with Logic

``` sql
CREATE PROCEDURE increase_salary(
    IN emp INT,
    IN inc NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employee
    SET salary = salary + inc
    WHERE emp_id = emp;
END;
$$;
```

------------------------------------------------------------------------

## 3️⃣ Calling Stored Procedures

### ✅ PostgreSQL / MySQL

``` sql
CALL get_all_employees();
CALL get_emp_by_dept(10);
```

### ❌ Invalid Usage

``` sql
SELECT * FROM get_all_employees(); -- ❌
```

📌 `SELECT` works for **functions**, not procedures.

------------------------------------------------------------------------

## 4️⃣ Stored Procedure vs Function

  Stored Procedure              Function
  ----------------------------- -------------------------
  May or may not return value   Must return a value
  Called using `CALL`           Called using `SELECT`
  Can handle transactions       Usually no transactions
  Used for actions              Used for calculations

------------------------------------------------------------------------

## 5️⃣ Use Cases of Stored Procedures 💡

### 🚀 1. Performance

-   Compiled once
-   Faster execution
-   Reduced SQL parsing

------------------------------------------------------------------------

### 🔐 2. Security

Users execute the procedure without direct table access

``` sql
GRANT EXECUTE ON PROCEDURE increase_salary TO hr_user;
```

------------------------------------------------------------------------

### 🔁 3. Reusability

-   Centralized business logic
-   Write once, call everywhere

------------------------------------------------------------------------

### 🧠 4. Business Logic in Database

-   Salary rules
-   Validation
-   Complex workflows

------------------------------------------------------------------------

### 🌐 5. Reduced Network Traffic

-   One `CALL` instead of many queries

------------------------------------------------------------------------

## 6️⃣ When NOT to Use Stored Procedures ❌

-   Heavy UI logic
-   Frequently changing logic
-   Database-vendor-independent applications

------------------------------------------------------------------------

## 7️⃣ Exam-Friendly One-Liners 📝

-   Stored procedure is **precompiled SQL code**
-   Executed using **CALL**
-   Improves **performance and security**
-   Supports **parameters and control flow**