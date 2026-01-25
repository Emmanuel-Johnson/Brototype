## 1️⃣ What is a Correlated Subquery?

A **correlated subquery** is a subquery that **depends on the outer query**.

👉 It **cannot run alone**
👉 It runs **once for each row** of the outer query

---

## 2️⃣ Simple Definition (Exam‑Ready 📝)

> **A correlated subquery is a subquery that uses values from the outer query and is executed once per row.**

---

## 3️⃣ Basic Example (Most Common)

❓ *Find employees earning more than the average salary of their own department*

```sql
SELECT name, salary, department_id
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);
```

### 🧠 What’s Happening?

* Outer query picks **one employee**
* Subquery calculates **average salary of THAT employee’s department**
* Salary is compared
* Repeats for **every row**

➡️ That’s why it’s called **correlated**

---

## 4️⃣ Why a Normal Subquery Won’t Work Here

❌ Wrong logic:

```sql
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```

✔ Compares with **overall average**
❌ Not **department‑wise**

---

## 5️⃣ Correlated Subquery with EXISTS (VERY IMPORTANT 🔥)

❓ *Departments that have at least one employee*

```sql
SELECT d.name
FROM departments d
WHERE EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.id
);
```

### Why `SELECT 1`?

* `EXISTS` only checks **presence**
* Returned columns **don’t matter**
* Stops at **first match** → fast ⚡

---

## 6️⃣ Correlated Subquery with NOT EXISTS

❓ *Departments with no employees*

```sql
SELECT d.name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.department_id = d.id
);
```

✔ Very clean
✔ Much safer than `NOT IN`

---

## 7️⃣ Correlated Subquery in SELECT Clause

```sql
SELECT
    e.name,
    e.salary,
    (
        SELECT COUNT(*)
        FROM employees e2
        WHERE e2.department_id = e.department_id
    ) AS dept_employee_count
FROM employees e;
```

⚠ Runs **once per row**
⚠ Can be expensive on **large tables**

---

## 8️⃣ Performance Notes (INTERVIEW FAVORITE ⭐)

| Point        | Truth                      |
| ------------ | -------------------------- |
| Execution    | Runs per row               |
| Speed        | Slower than JOIN (usually) |
| Optimization | DB may rewrite internally  |
| Best for     | `EXISTS` / `NOT EXISTS`    |

👉 Real projects → **JOIN preferred**
👉 Interviews → **Know both**

---

## 9️⃣ Correlated Subquery vs JOIN (Same Result)

### Correlated Subquery

```sql
SELECT name, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department_id = e.department_id
);
```

### JOIN Version (Faster)

```sql
SELECT e.name, e.salary
FROM employees e
JOIN (
    SELECT department_id, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department_id
) d
ON e.department_id = d.department_id
WHERE e.salary > d.avg_sal;
```

✔ Same output
✔ JOIN scales better

---

## 🔟 Common Mistakes ❌

❌ Forgetting to reference outer table
❌ Using correlated subquery when JOIN is enough
❌ Assuming it runs only once
❌ Using `=` instead of `EXISTS`

---

## 🧠 One‑Liner to Remember

> **Normal subquery → runs once**
> **Correlated subquery → runs once per row**

---

✅ Perfect for **PostgreSQL interviews & deep understanding**
