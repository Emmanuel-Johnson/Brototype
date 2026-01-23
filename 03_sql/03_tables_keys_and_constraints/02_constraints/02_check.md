# CHECK Constraint in PostgreSQL

A **CHECK** constraint ensures that values in a column (or columns) satisfy a specific condition.

👉 If the condition evaluates to **FALSE**, the `INSERT` or `UPDATE` is rejected.

---

## 🔹 Basic Syntax

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    age INT CHECK (age >= 18)
);
```

✔️ Allowed: `age = 18`, `25`, `60`  
❌ Not allowed: `age = 10`

---

## 🔹 CHECK with Multiple Conditions

```sql
salary NUMERIC CHECK (salary > 0 AND salary <= 1000000)
```

Both conditions **must be true**.

---

## 🔹 CHECK on Multiple Columns (Table-level)

```sql
CREATE TABLE orders (
    price NUMERIC,
    quantity INT,
    CHECK (price > 0 AND quantity > 0)
);
```

✔️ You can reference **more than one column**.

---

## 🔹 CHECK vs NOT NULL (Very Common Interview Question)

| Feature              | NOT NULL | CHECK |
|---------------------|----------|-------|
| Prevents NULL       | ✅ Yes   | ❌ No (unless specified) |
| Validates conditions| ❌ No    | ✅ Yes |
| Allows logic        | ❌ No    | ✅ Yes |
| Column required     | ✅ Yes   | ❌ No |

### Example

```sql
age INT CHECK (age >= 18)
```

➡️ `NULL` is still allowed ❗  

To block `NULL` values:

```sql
age INT NOT NULL CHECK (age >= 18)
```

---

## 🔹 CHECK with ENUM-like Behavior

```sql
status TEXT CHECK (status IN ('active', 'inactive', 'blocked'))
```

✔️ Great alternative to `ENUM` in many cases.

---

## 🔹 Adding CHECK to an Existing Table

```sql
ALTER TABLE employees
ADD CONSTRAINT age_check CHECK (age >= 18);
```

---

## 🔹 Removing a CHECK Constraint

```sql
ALTER TABLE employees
DROP CONSTRAINT age_check;
```

---

## 🔹 CHECK Constraint Error Example

```sql
INSERT INTO employees (age)
VALUES (15);
```

❌ **Error**

```text
new row for relation "employees" violates check constraint "age_check"
```

---

## 🔹 Important Interview Points ⭐

- `CHECK` enforces **business rules**
- Works at **database level** (safer than app-only validation)
- Can reference **multiple columns**
- Allows `NULL` unless combined with `NOT NULL`
- Evaluated on `INSERT` and `UPDATE`

---

## 🔑 One-liner to remember

- **NOT NULL** → value must exist  
- **CHECK** → value must be valid  