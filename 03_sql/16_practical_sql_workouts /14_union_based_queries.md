## UNION vs UNION ALL (PostgreSQL)

---

## 🔹 What `UNION` Does (Quick Rules)

* Combines results of **two or more `SELECT` queries**
* **Column count and data types must match**
* `UNION` → **removes duplicates**
* `UNION ALL` → **keeps duplicates** (faster)

---

## 1️⃣ Basic `UNION`

**Get all employee and student names**

```sql
SELECT name
FROM employees
UNION
SELECT name
FROM students;
```

---

## 2️⃣ `UNION ALL`

**Include duplicates**

```sql
SELECT name
FROM employees
UNION ALL
SELECT name
FROM students;
```

---

## 3️⃣ `UNION` with Different Column Names

**Combine customers and suppliers**

```sql
SELECT customer_name AS name, city
FROM customers
UNION
SELECT supplier_name AS name, city
FROM suppliers;
```

---

## 4️⃣ `UNION` with Constants (Very Common Interview Case)

**Identify source table**

```sql
SELECT name, 'Employee' AS source
FROM employees
UNION
SELECT name, 'Student' AS source
FROM students;
```

---

## 5️⃣ `UNION` with `WHERE` Conditions

**Active employees + final year students**

```sql
SELECT name
FROM employees
WHERE status = 'ACTIVE'
UNION
SELECT name
FROM students
WHERE year = 4;
```

---

## 6️⃣ `UNION` with `ORDER BY` (Important Rule ⚠️)

```sql
SELECT name
FROM employees
UNION
SELECT name
FROM students
ORDER BY name;
```

📌 `ORDER BY` applies to the **final combined result only**

---

## 7️⃣ `UNION` with Aggregate Data

**Total employees per department + total students per course**

```sql
SELECT department AS category, COUNT(*) AS total
FROM employees
GROUP BY department
UNION
SELECT course AS category, COUNT(*) AS total
FROM students
GROUP BY course;
```

---

## 🧠 Interview Notes (Say This Confidently)

* Use `UNION ALL` when duplicates **don’t matter** (better performance)
* `UNION` performs **`DISTINCT` internally**
* `ORDER BY` is used **only once**, at the end
* Column names don’t need to match — only **positions and data types** matter
