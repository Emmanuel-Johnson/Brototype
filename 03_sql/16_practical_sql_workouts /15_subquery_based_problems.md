## SQL Subqueries – Complete Interview Guide

---

## 🔹 What a Subquery Is (One‑Liner)

A **subquery** is a query inside another query, used to return values needed by the outer query.

---

## 1️⃣ Single‑Row Subquery

**Employees earning more than average salary**

```sql
SELECT *
FROM employees
WHERE salary > (
  SELECT AVG(salary)
  FROM employees
);
```

---

## 2️⃣ Multi‑Row Subquery (`IN`)

**Customers who placed at least one order**

```sql
SELECT *
FROM customers
WHERE customer_id IN (
  SELECT customer_id
  FROM orders
);
```

---

## 3️⃣ Subquery with `NOT IN`

**Customers who never placed an order**

```sql
SELECT *
FROM customers
WHERE customer_id NOT IN (
  SELECT customer_id
  FROM orders
);
```

### ⚠️ Interview Trap: `NOT IN` + `NULL`

`NOT IN` fails if the subquery returns `NULL`.

### ✅ Safe Version

```sql
SELECT *
FROM customers
WHERE customer_id NOT IN (
  SELECT customer_id
  FROM orders
  WHERE customer_id IS NOT NULL
);
```

---

## 4️⃣ Correlated Subquery

**Employees earning more than department average**

```sql
SELECT *
FROM employees e
WHERE salary > (
  SELECT AVG(salary)
  FROM employees
  WHERE department = e.department
);
```

📌 Subquery runs **once per row** of the outer query.

---

## 5️⃣ Subquery in `SELECT`

**Show customer with total orders**

```sql
SELECT
  c.customer_id,
  c.name,
  (
    SELECT COUNT(*)
    FROM orders o
    WHERE o.customer_id = c.customer_id
  ) AS total_orders
FROM customers c;
```

---

## 6️⃣ Subquery in `FROM` (Derived Table)

**Departments with average salary above company average**

```sql
SELECT *
FROM (
  SELECT department, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department
) d
WHERE avg_salary > (
  SELECT AVG(salary)
  FROM employees
);
```

---

## 7️⃣ `EXISTS` Subquery ⭐ (Very Important)

**Customers who have orders**

```sql
SELECT *
FROM customers c
WHERE EXISTS (
  SELECT 1
  FROM orders o
  WHERE o.customer_id = c.customer_id
);
```

🔹 Faster and safer than `IN` in many cases.

---

## 🧠 Interview Gold Rules

### Subquery Types

* Single‑row
* Multi‑row
* Correlated

### Key Rules

* `EXISTS` checks **presence**, not values
* Prefer `EXISTS` over `IN` for **large datasets**
* Avoid `NOT IN` when `NULL`s are possible
