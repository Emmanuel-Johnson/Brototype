# Triggers -- Complete Notes

## 1️⃣ What is a Trigger?

A **trigger** is a special stored program that automatically executes
when a specific event occurs on a table.

📌 **Trigger fires on:** - INSERT - UPDATE - DELETE

📌 **Trigger timing:** - BEFORE - AFTER

👉 You don't call a trigger --- the database does it automatically.

**Exam-friendly definition:**

> A trigger is a database object that automatically executes in response
> to certain events on a table.

------------------------------------------------------------------------

## 2️⃣ BEFORE Trigger ⏳

A **BEFORE trigger** runs before the actual DML operation happens.

### ✅ Why use a BEFORE trigger?

-   Validate data
-   Modify values before insert/update
-   Prevent invalid operations

### Example: BEFORE INSERT Trigger

``` sql
CREATE OR REPLACE FUNCTION check_salary()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.salary < 0 THEN
        RAISE EXCEPTION 'Salary cannot be negative';
    END IF;
    RETURN NEW;
END;
$$;
```

``` sql
CREATE TRIGGER before_salary_insert
BEFORE INSERT ON employee
FOR EACH ROW
EXECUTE FUNCTION check_salary();
```

📌 If salary is negative → insert fails ❌

------------------------------------------------------------------------

## 3️⃣ AFTER Trigger ⏱️

An **AFTER trigger** runs after the DML operation is completed
successfully.

### ✅ Why use an AFTER trigger?

-   Logging
-   Auditing
-   Updating another table
-   Notifications

### Example: AFTER INSERT Trigger (Audit Log)

``` sql
CREATE OR REPLACE FUNCTION log_employee()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO emp_log(emp_id, action, action_time)
    VALUES (NEW.emp_id, 'INSERT', NOW());
    RETURN NEW;
END;
$$;
```

``` sql
CREATE TRIGGER after_emp_insert
AFTER INSERT ON employee
FOR EACH ROW
EXECUTE FUNCTION log_employee();
```

📌 Insert happens → log is written ✔

------------------------------------------------------------------------

## 4️⃣ BEFORE vs AFTER Triggers (Very Important)

  BEFORE Trigger        AFTER Trigger
  --------------------- ------------------------------
  Runs before DML       Runs after DML
  Can modify NEW        Cannot modify NEW
  Used for validation   Used for logging
  Can stop operation    Cannot stop completed action

------------------------------------------------------------------------

## 5️⃣ Use Cases of Triggers 💡

### 🔐 1. Data Validation

-   Salary \> 0
-   Age ≥ 18

### 🧾 2. Auditing / Logging

-   Track who changed what and when

### 🔄 3. Maintain Derived Data

-   Auto-update totals
-   Sync related tables

### 🚫 4. Enforcing Business Rules

-   Prevent deleting important records
-   Restrict updates

### 🤖 5. Automation

-   Auto timestamp
-   Auto status update

------------------------------------------------------------------------

## 6️⃣ Important Exam Points 📝

-   Triggers are event-driven
-   Automatically executed
-   Associated with tables
-   Cannot be called explicitly
-   Use carefully (can hurt performance)

------------------------------------------------------------------------

## 7️⃣ Trigger Types (Quick)

-   Row-level trigger → FOR EACH ROW
-   Statement-level trigger → once per statement