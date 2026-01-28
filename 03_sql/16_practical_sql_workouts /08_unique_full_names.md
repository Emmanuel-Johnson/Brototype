## Unique Full Names (PostgreSQL)

### ✅ Using `DISTINCT`

```sql
SELECT DISTINCT
  first_name || ' ' || last_name AS full_name
FROM students;
```

This removes duplicate **full name combinations**.

---

### ✅ Better (Safer) Version Using `GROUP BY`

```sql
SELECT
  first_name || ' ' || last_name AS full_name
FROM students
GROUP BY first_name, last_name;
```

👉 **Preferred in interviews**, especially when asked why `DISTINCT` may fail later when adding extra columns.

---

## ⚠️ Important Notes

* `DISTINCT` works on the **entire selected row**
* If two students have the same first & last name → they appear **once**
* Use **`student_id`** if you want **unique students**, not just unique names

---

### 🔤 Case‑Insensitive Unique Full Names

```sql
SELECT DISTINCT
  LOWER(first_name || ' ' || last_name) AS full_name
FROM students;
```

This treats `John Doe` and `john doe` as the same name.
