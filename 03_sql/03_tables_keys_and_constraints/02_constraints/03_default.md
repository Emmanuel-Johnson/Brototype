# DEFAULT Constraint in PostgreSQL

**DEFAULT** is used to automatically assign a value to a column when no value is provided during `INSERT`.

👉 It does **not** restrict values like `CHECK`  
👉 It does **not** prevent `NULL` unless combined with `NOT NULL`

---

## 🔹 Basic Syntax

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    is_active BOOLEAN DEFAULT true
);
```

If you run:

```sql
INSERT INTO users DEFAULT VALUES;
```

✔️ `is_active` → `true`

---

## 🔹 DEFAULT with NOT NULL (Very Common)

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    price NUMERIC NOT NULL DEFAULT 0
);
```

- If `price` is omitted → `0`
- If `price = NULL` → ❌ error (because of `NOT NULL`)

---

## 🔹 DEFAULT vs NULL (Important Concept)

```sql
INSERT INTO users (is_active) VALUES (NULL);
```

❌ `DEFAULT` will **NOT** apply here  

✔️ `DEFAULT` applies **only when the column is omitted**, not when `NULL` is explicitly given.

---

## 🔹 DEFAULT with Functions

```sql
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
```

Other common ones:

- `NOW()`
- `CURRENT_DATE`
- `gen_random_uuid()` (with extension)

---

## 🔹 DEFAULT with Foreign Key (Allowed)

```sql
role_id INT DEFAULT 1 REFERENCES roles(id)
```

✔️ Valid as long as `1` exists in `roles`.

---

## 🔹 Adding DEFAULT to Existing Column

```sql
ALTER TABLE users
ALTER COLUMN country SET DEFAULT 'India';
```

⚠️ This affects **future inserts only**.

---

## 🔹 Removing DEFAULT

```sql
ALTER TABLE users
ALTER COLUMN country DROP DEFAULT;
```

---

## 🔹 DEFAULT vs CHECK vs NOT NULL

| Feature              | DEFAULT | NOT NULL | CHECK |
|---------------------|---------|----------|-------|
| Auto value          | ✅ Yes  | ❌ No    | ❌ No |
| Prevents NULL       | ❌ No   | ✅ Yes   | ❌ No |
| Validates logic     | ❌ No   | ❌ No    | ✅ Yes |
| Applied when omitted| ✅ Yes  | ❌ No    | ❌ No |

---

## 🔹 Common Real-World Defaults

```sql
is_active BOOLEAN DEFAULT true
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
quantity INT DEFAULT 1
status TEXT DEFAULT 'pending'
```

---

## 🔹 Interview One-Liners ⭐

- `DEFAULT` works only when column is **missing**
- `DEFAULT` does **not override NULL**
- `DEFAULT` does **not validate data**
- Often combined with `NOT NULL`

---

## 🔑 Memory Trick

**DEFAULT fills, NOT NULL forces, CHECK validates**