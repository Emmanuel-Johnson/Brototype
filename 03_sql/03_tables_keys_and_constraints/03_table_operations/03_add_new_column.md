# ALTER TABLE – Add & Drop Columns in PostgreSQL

The `ALTER TABLE` command is used to **modify the structure** of an existing table.

---

## 1️⃣ Add New Column

```sql
ALTER TABLE users
ADD COLUMN age INT;
```

✔ Adds a new column  
✔ Existing rows get `NULL` (by default)

---

## 2️⃣ Add New Column with DEFAULT Value

```sql
ALTER TABLE users
ADD COLUMN is_active BOOLEAN DEFAULT true;
```

### What happens here?
- Existing rows → `is_active = true`
- New inserts without value → `true`
- No need to update old rows manually

---

## 3️⃣ Add Column + DEFAULT + NOT NULL (Safe Way)

```sql
ALTER TABLE users
ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL;
```

✔ Works safely because `DEFAULT` fills existing rows  
✔ Avoids `NOT NULL` constraint errors

---

## 4️⃣ Drop Column

```sql
ALTER TABLE users
DROP COLUMN age;
```

⚠️ **Warning**
- Data is permanently removed
- Cannot be rolled back unless inside a transaction

---

## 5️⃣ Drop Column (IF EXISTS)

```sql
ALTER TABLE users
DROP COLUMN IF EXISTS age;
```

✔ Prevents error if column doesn’t exist

---

## 🔑 Interview Notes (Remember These)

- New columns are `NULL` by default
- `DEFAULT` affects:
  - Existing rows (at column creation time)
  - Future inserts
- `DROP COLUMN` is **irreversible**
- You can add **multiple columns** in one query

---

## 6️⃣ Multiple Operations Together

```sql
ALTER TABLE users
ADD COLUMN phone VARCHAR(15),
ADD COLUMN status TEXT DEFAULT 'active',
DROP COLUMN age;
```

✔ Multiple `ADD` / `DROP` operations can be done in a single statement

---