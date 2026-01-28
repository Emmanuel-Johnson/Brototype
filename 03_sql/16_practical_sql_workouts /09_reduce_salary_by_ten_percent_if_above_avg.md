## Reduce Salary by 10% If Salary Is Above Average (PostgreSQL)

### ✅ Update Query

```sql
UPDATE employees
SET salary = salary * 0.9
WHERE salary > (
  SELECT AVG(salary)
  FROM employees
);
```

---

## 🧠 Explanation (Interview‑Ready)

* `AVG(salary)` → calculates the **average salary**
* The **subquery runs once**
* Only employees earning **above average** are updated
* `salary * 0.9` → reduces salary by **10%**

---

## 🔍 Check Affected Rows Before Updating (Good Practice)

```sql
SELECT *
FROM employees
WHERE salary > (
  SELECT AVG(salary)
  FROM employees
);
```

---

## ⚠️ Important Notes

* `AVG()` **ignores NULL values** automatically
* This update is **safe in PostgreSQL** (no restriction on updating and selecting from the same table, unlike MySQL)
