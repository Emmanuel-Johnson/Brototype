## Number of Employees in the Engineering Department (PostgreSQL)

### ✅ Simple Case (Department in Same Table)

```sql
SELECT COUNT(*) AS employee_count
FROM employees
WHERE department = 'Engineering';
```

---

### 🧠 If Department Is in a Separate Table

```sql
SELECT COUNT(*) AS employee_count
FROM employees e
JOIN departments d
  ON e.department_id = d.department_id
WHERE d.department_name = 'Engineering';
```

---

## ⚠️ Interview Notes

* `COUNT(*)` → counts **all rows** (including rows with `NULL` values)
* `COUNT(column)` → **ignores NULL values** in that column
* String comparison in PostgreSQL is **case‑sensitive**

  * `'engineering' ≠ 'Engineering'`

---

### ✅ Case‑Insensitive Version

```sql
WHERE LOWER(department) = 'engineering';
```
