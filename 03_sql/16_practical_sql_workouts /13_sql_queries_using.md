## SQL Interview Essentials – Joins, Functions, Aggregates

---

## 1️⃣ Multiple JOINs

**Find customer name, order amount, and shipping city**

```sql
SELECT
  c.first_name || ' ' || c.last_name AS customer_name,
  o.order_id,
  o.amount,
  s.city
FROM customers c
JOIN orders o
  ON c.customer_id = o.customer_id
JOIN shipping s
  ON o.order_id = s.order_id;
```

---

## 2️⃣ String Functions

### Names starting with ‘A’ (uppercase output)

```sql
SELECT
  UPPER(name) AS employee_name
FROM employees
WHERE name LIKE 'A%';
```

### Trim extra spaces

```sql
SELECT TRIM(name)
FROM employees;
```

---

## 3️⃣ Date Functions

### Orders placed in 2024

```sql
SELECT *
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2024;
```

### Orders from last 30 days

```sql
SELECT *
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '30 days';
```

---

## 4️⃣ Aggregate Functions

### Total orders and total revenue per customer

```sql
SELECT
  customer_id,
  COUNT(*) AS total_orders,
  SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id;
```

### Average salary per department

```sql
SELECT
  department,
  AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```

---

## 5️⃣ HAVING Clause Logic

### Departments with average salary above 60,000

```sql
SELECT
  department,
  AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

### Customers with more than 3 orders

```sql
SELECT
  customer_id,
  COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 3;
```

---

## 🧠 Interview Gold Rules

* `WHERE` → filters **rows**
* `HAVING` → filters **groups**
* `JOIN` happens **before** `WHERE`
* `HAVING` comes **after** `GROUP BY`
