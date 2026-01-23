# NOT NULL in PostgreSQL

**NOT NULL** is a constraint in PostgreSQL that ensures a column cannot store `NULL` values.

### In simple words:
👉 Every row **must have a value** for that column.

---

## 🔹 Basic Syntax

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100)
);
```

- `username` → **cannot be NULL**
- `email` → **can be NULL** (default behavior)

---

## 🔹 Why NOT NULL is Important

- Ensures mandatory data  
- Prevents incomplete records  
- Improves data integrity  
- Often used with **Primary Keys** and important fields  

---

## 🔹 NOT NULL vs PRIMARY KEY

| Feature              | NOT NULL | PRIMARY KEY |
|---------------------|----------|-------------|
| Allows NULL         | ❌ No    | ❌ No       |
| Allows duplicates   | ✅ Yes   | ❌ No       |
| One per table       | ❌ No    | ✅ Yes      |
| Enforces uniqueness | ❌ No    | ✅ Yes      |

📌 **Primary Key = NOT NULL + UNIQUE**

---

## 🔹 Adding NOT NULL to an Existing Column

```sql
ALTER TABLE users
ALTER COLUMN email SET NOT NULL;
```

⚠️ This will **fail** if the column already contains `NULL` values.

### Fix first

```sql
UPDATE users
SET email = 'unknown@example.com'
WHERE email IS NULL;
```

Then apply `NOT NULL`.

---

## 🔹 Removing NOT NULL

```sql
ALTER TABLE users
ALTER COLUMN email DROP NOT NULL;
```

---

## 🔹 NOT NULL with DEFAULT

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    price NUMERIC NOT NULL DEFAULT 0
);
```

- If `price` is not provided → PostgreSQL inserts `0`
- But `NULL` is still **not allowed**

---

## 🔹 Important Interview Points ⭐

- Columns are **nullable by default**
- `NOT NULL` is a **column-level constraint**
- `NOT NULL` is **not the same as UNIQUE**
- A table can have **multiple NOT NULL columns**
- `NOT NULL` **cannot be deferred** (always checked immediately)

---

## 🔹 Quick Example (Error)

```sql
INSERT INTO users (email)
VALUES ('test@example.com');
```

❌ **Error**

```text
null value in column "username" violates not-null constraint
```