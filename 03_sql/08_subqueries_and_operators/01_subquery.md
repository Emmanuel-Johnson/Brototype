# 🔹 Subqueries in PostgreSQL

A **subquery** is a query inside another query.

Think of it like:

> **First get this result → then use it in the main query**

```sql
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

👉 Inner query runs first
👉 Its result is used by the outer query

---

## 1️⃣ Types of Subqueries (Very Important)

### 🔹 A. Scalar Subquery (Returns ONE value)

Used with `=`, `>`, `<`, `>=`, `<=`

```sql
SELECT name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

✔ Inner query returns **one value**
✔ Very common in **exams & interviews**

---

### 🔹 B. Row Subquery (Returns ONE row, multiple columns)

```sql
SELECT *
FROM employees
WHERE (department_id, salary) = (
    SELECT department_id, MAX(salary)
    FROM employees
    GROUP BY department_id
    LIMIT 1
);
```

✔ Less common
✔ Mostly for **advanced use cases**

---

### 🔹 C. Table Subquery (Returns multiple rows)

Used with `IN`, `ANY`, `ALL`, `EXISTS`

```sql
SELECT name
FROM employees
WHERE department_id IN (
    SELECT id
    FROM departments
    WHERE location = 'India'
);
```

✔ **Most frequently used** type

---

## 2️⃣ Subqueries with IN / ANY / ALL

### 🔹 IN (Most Common)

```sql
SELECT name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM employees
    WHERE salary > 60000
);
```

✔ Matches **any value** in the list

---

### 🔹 ANY

```sql
SELECT name
FROM employees
WHERE salary > ANY (
    SELECT salary
    FROM employees
    WHERE department_id = 3
);
```

✔ Greater than **at least one** value

---

### 🔹 ALL

```sql
SELECT name
FROM employees
WHERE salary > ALL (
    SELECT salary
    FROM employees
    WHERE department_id = 3
);
```

✔ Greater than **every value**

---

## 3️⃣ Correlated Subquery (Advanced 🔥)

A **correlated subquery** depends on the outer query.

```sql
SELECT name, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);
```

🧠 Inner query runs **once per row**
🧠 Powerful but can be **slower** if not optimized

---

## 4️⃣ EXISTS vs IN (INTERVIEW GOLD ⭐)

### 🔹 EXISTS

```sql
SELECT d.name
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.id
);
```

✔ Stops on **first match**
✔ Faster for **large datasets**

---

### 🔹 IN (Comparison)

```sql
SELECT name
FROM departments
WHERE id IN (
    SELECT department_id
    FROM employees
);
```

⚠ Can be slower
⚠ `NULL` values can cause surprises

---

## 5️⃣ Subquery in SELECT Clause (Advanced)

```sql
SELECT
    name,
    (SELECT COUNT(*)
     FROM employees e2
     WHERE e2.department_id = e.department_id) AS dept_count
FROM employees e;
```

✔ Runs **per row**
✔ Use carefully (can be expensive)

---

## 6️⃣ Subquery in FROM Clause (Derived Table)

```sql
SELECT department_id, avg_salary
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) t
WHERE avg_salary > 50000;
```

✔ Acts like a **temporary table**
✔ Very clean & readable

---

## 7️⃣ Subquery vs JOIN (VERY Important)

| Use Case                  | Prefer   |
| ------------------------- | -------- |
| Simple filtering          | Subquery |
| Reporting / multi columns | JOIN     |
| Performance-critical      | JOIN     |
| Existence check           | EXISTS   |

👉 **Rule of Thumb:**
If you need columns from both tables → **JOIN**
If you need only filtering → **Subquery**

---

## 8️⃣ Common Mistakes ❌

❌ Subquery returns multiple rows with `=`
❌ Forgetting correlated reference
❌ Using `IN` with `NULL` values
❌ Overusing subqueries instead of JOINs

---

## 9️⃣ One-Line Definition (Exam Ready 📝)

> **A subquery is a query nested inside another query whose result is used by the outer query.**

---

✅ Perfect for **PostgreSQL interviews & quick revision**
