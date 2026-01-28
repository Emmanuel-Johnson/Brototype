## Update Rows Where ID Is Even (PostgreSQL)

### ✅ Update Query

```sql
UPDATE employees
SET salary = salary * 1.10
WHERE id % 2 = 0;
```

👉 `id % 2 = 0` → selects **even IDs**

---

## 🔍 Always Preview Before Updating (Best Practice)

```sql
SELECT *
FROM employees
WHERE id % 2 = 0;
```

---

## 🧠 Interview Notes

* `%` → **modulo operator** (returns remainder)
* Works for **any numeric column**
* For **odd IDs** → `id % 2 = 1`

---

## 🔁 Example Variations

### Set a Fixed Value

```sql
UPDATE employees
SET status = 'ACTIVE'
WHERE id % 2 = 0;
```

### Using a Primary Key Other Than `id`

```sql
UPDATE employees
SET salary = salary * 1.10
WHERE employee_id % 2 = 0;
```
