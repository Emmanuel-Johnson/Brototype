# ON DELETE / ON UPDATE (Referential Actions) in PostgreSQL

Referential actions are used **only with FOREIGN KEY** constraints to define what happens to child rows when a parent row is **deleted or updated**.

```sql
FOREIGN KEY (child_col)
REFERENCES parent_table(parent_col)
ON DELETE action
ON UPDATE action;
```

---

## 🔹 1. CASCADE

### ➤ ON DELETE CASCADE

Deletes child rows automatically when the parent row is deleted.

```sql
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE
```

🧨 Delete parent → related child rows are deleted

### ➤ ON UPDATE CASCADE

Automatically updates child foreign key values when the parent key changes.

```sql
ON UPDATE CASCADE
```

---

## 🔹 2. SET NULL

### ➤ ON DELETE SET NULL

Sets the foreign key column to `NULL`.

```sql
ON DELETE SET NULL
```

⚠️ Foreign key column **must allow NULL**

### ➤ ON UPDATE SET NULL

Sets the foreign key to `NULL` when the parent key is updated.

---

## 🔹 3. SET DEFAULT

### ➤ ON DELETE SET DEFAULT

Sets the foreign key to its default value.

```sql
ON DELETE SET DEFAULT
```

⚠️ Column must have a `DEFAULT` value  
⚠️ That default value **must exist in the parent table**

---

## 🔹 4. RESTRICT

### ➤ ON DELETE RESTRICT

Prevents delete or update if related child rows exist.

```sql
ON DELETE RESTRICT
```

❌ Parent cannot be deleted while child exists  
⏱ Checked **immediately**

---

## 🔹 5. NO ACTION (Default)

```sql
ON DELETE NO ACTION
```

- Same logical effect as `RESTRICT`
- Checked at **end of statement**
- **Default behavior in PostgreSQL**

---

## 🔹 RESTRICT vs NO ACTION (Interview Favorite)

| Feature                | RESTRICT | NO ACTION |
|------------------------|----------|-----------|
| Default                | ❌ No    | ✅ Yes    |
| Check timing           | Immediate| End of statement |
| Allows deferred checks | ❌ No    | ✅ Yes    |
| Result                 | Blocks operation | Blocks operation |

📌 In most real-world cases → they behave the same.

---

## 🔹 Full Example

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT,
    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
    ON UPDATE SET NULL
);
```

---

## 🔹 When to Use What (Real Projects)

| Scenario                     | Best Choice |
|------------------------------|-------------|
| Strong ownership             | CASCADE     |
| Optional relationship        | SET NULL    |
| Fallback record              | SET DEFAULT |
| Financial / critical data    | RESTRICT / NO ACTION |

---

## 🔹 Interview One-Liners ⭐

- Referential actions work **only with FOREIGN KEY**
- `CASCADE` propagates changes
- `SET NULL` requires nullable column
- `SET DEFAULT` requires valid default
- `NO ACTION` is PostgreSQL default
- `RESTRICT` checks immediately

---

## 🔑 Memory Trick

- **CASCADE** → follow parent  
- **SET NULL** → break link  
- **SET DEFAULT** → fallback  
- **RESTRICT / NO ACTION** → block  