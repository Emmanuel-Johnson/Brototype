# 🔹 HAVING in PostgreSQL

## What is HAVING?

`HAVING` is used to **filter groups**, not individual rows.

It works **after `GROUP BY`** and is mainly used with **aggregate functions**.

```sql
SELECT column, AGG_FUNC(column)
FROM table
GROUP BY column
HAVING condition;
```

---

## 🧠 Key Difference (Memorize This)

| Clause | Filters         |
| ------ | --------------- |
| WHERE  | individual rows |
| HAVING | grouped results |

---

## 1️⃣ Basic Example

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

✔ Groups employees by department
✔ Keeps only departments with **more than 5 employees**

---

## 2️⃣ Why WHERE Won’t Work Here

### ❌ Wrong

```sql
WHERE COUNT(*) > 5;
```

Why?

* `WHERE` runs **before grouping**
* Aggregate results **don’t exist yet**

---

## 3️⃣ WHERE + HAVING Together (Very Common)

```sql
SELECT department, COUNT(*)
FROM employees
WHERE active = true
GROUP BY department
HAVING COUNT(*) >= 3;
```

* `WHERE` → filters rows (`active = true`)
* `HAVING` → filters groups (`COUNT >= 3`)

---

## 4️⃣ HAVING Without GROUP BY (Yes, but Rare)

```sql
SELECT COUNT(*)
FROM employees
HAVING COUNT(*) > 100;
```

✔ Valid
✔ Treats the **entire table as one group**

---

## 5️⃣ HAVING with Multiple Conditions

```sql
HAVING COUNT(*) > 5
AND AVG(salary) > 50000;
```

---

## 6️⃣ HAVING with JOIN

```sql
SELECT d.name, COUNT(e.id)
FROM departments d
LEFT JOIN employees e
ON d.id = e.department_id
GROUP BY d.name
HAVING COUNT(e.id) > 0;
```

✔ Departments with **at least one employee**

---

## 7️⃣ HAVING with Expressions

```sql
SELECT department, ROUND(AVG(salary)) AS avg_salary
FROM employees
GROUP BY department
HAVING ROUND(AVG(salary)) > 60000;
```

---

## ⚠️ Common Mistakes (Exam Gold 🥇)

### ❌ Using HAVING instead of WHERE

```sql
HAVING department = 'IT';
```

✔ Works
❌ Bad practice — no aggregation

### ✅ Correct

```sql
WHERE department = 'IT';
```

---

### ❌ Filtering Non-Aggregates in HAVING

```sql
HAVING salary > 50000;
```

❌ Invalid (`salary` is not grouped)

---

## 🧠 Execution Order (Remember This)

```
FROM / JOIN
→ WHERE
→ GROUP BY
→ HAVING
→ SELECT
→ ORDER BY
→ LIMIT
```

---

## 🧠 Interview Rules to Memorize

* `HAVING` filters **groups**
* `WHERE` filters **rows**
* Aggregates belong in `HAVING`, not `WHERE`
* You can use `WHERE` and `HAVING` together
* `HAVING` can exist **without** `GROUP BY`

---

## ✅ One-Line Summary

Use `HAVING` **when your condition involves an aggregate function**.

<br>
<br>
<br>

# 🔹 SELECT vs WHERE vs HAVING — Column Rules

### They apply only when a query has GROUP BY (or aggregates).

| Clause | Rule                                              |
| ------ | ------------------------------------------------- |
| SELECT | Must be a `GROUP BY` column **or** an aggregate   |
| HAVING | Must be a `GROUP BY` column **or** an aggregate   |
| WHERE  | Can use **any column** (❌ aggregates not allowed) |

---

## 🧠 How to Remember

* **WHERE** → filters **rows** → no aggregates exist yet
* **GROUP BY** → forms groups
* **HAVING** → filters **groups** → aggregates allowed
* **SELECT** → can only show grouped columns or aggregates

---

## ✅ Quick Examples

### Valid

```sql
SELECT department, COUNT(*)
FROM employees
WHERE active = true
GROUP BY department
HAVING COUNT(*) > 5;
```

### Invalid

```sql
SELECT department, salary
FROM employees
GROUP BY department;  -- ❌ salary not grouped or aggregated
```

---

## ✅ One-Line Summary

> WHERE filters rows, GROUP BY defines groups, HAVING filters groups, and SELECT can only show grouped columns or aggregates.
