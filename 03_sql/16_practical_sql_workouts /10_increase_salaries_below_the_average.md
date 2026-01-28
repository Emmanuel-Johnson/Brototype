## Increase Salary by 10% If Salary Is Below Average (PostgreSQL)

### ✅ Update Query

```sql
UPDATE employees
SET salary = salary * 1.10
WHERE salary < (
  SELECT AVG(salary)
  FROM employees
);
```

---

## 🧠 Explanation (Quick & Interview‑Ready)

* `AVG(salary)` → finds the **average salary**
* Employees earning **below average** get a **10% increase**
* `salary * 1.10` → adds **10%** to the salary

---

## 🔍 Always Preview Before Updating (Best Practice)

```sql
SELECT *
FROM employees
WHERE salary < (
  SELECT AVG(salary)
  FROM employees
);
```

---

## ⚠️ Common Interview Follow‑Ups

* **What if salary is `NULL`?** → Ignored by `AVG()` automatically
* **What if everyone has the same salary?** → No rows are updated
* **How to round values?**

```sql
UPDATE employees
SET salary = ROUND(salary * 1.10, 2)
WHERE salary < (
  SELECT AVG(salary)
  FROM employees
);
```
