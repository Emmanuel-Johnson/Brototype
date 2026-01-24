# 🧠 Logical Operators in PostgreSQL

PostgreSQL supports **three logical operators**:

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| AND      | all conditions must be TRUE         |
| OR       | at least one condition must be TRUE |
| NOT      | reverses the condition              |

They are mostly used in **WHERE**, **ON**, **HAVING**, and **CASE**.

---

## 1️⃣ AND

All conditions must be **TRUE**.

```sql
SELECT *
FROM employees
WHERE department = 'IT'
AND salary >= 60000;
```

✔ department must be IT
✔ salary must be ≥ 60000

---

## 2️⃣ OR

At least **one** condition must be TRUE.

```sql
SELECT *
FROM employees
WHERE department = 'HR'
OR department = 'Finance';
```

---

## ⚠️ AND vs OR (Classic Mistake)

```sql
WHERE department = 'IT'
OR department = 'HR'
AND salary > 60000;
```

❗ Interpreted as:

```sql
WHERE department = 'IT'
OR (department = 'HR' AND salary > 60000);
```

Because **AND has higher precedence than OR**.

---

### ✅ Always Use Parentheses

```sql
WHERE (department = 'IT' OR department = 'HR')
AND salary > 60000;
```

📌 **Interview Rule**

> If you mix `AND` + `OR` → use parentheses.

---

## 3️⃣ NOT

Reverses a condition.

```sql
SELECT *
FROM employees
WHERE NOT department = 'IT';
```

Same as:

```sql
WHERE department <> 'IT';
```

---

### NOT with IN

```sql
WHERE department NOT IN ('HR', 'Finance');
```

### NOT with LIKE

```sql
WHERE name NOT LIKE 'A%';
```

---

## ⚠️ NOT + NULL Trap

```sql
WHERE department NOT IN ('HR', 'Finance');
```

❌ If `department` is `NULL` → row is **excluded**

### ✅ Safer Version

```sql
WHERE department IS DISTINCT FROM 'HR'
AND department IS DISTINCT FROM 'Finance';
```

---

## 🧮 Truth Table (NULL Logic)

PostgreSQL uses **3-valued logic**: `TRUE`, `FALSE`, `UNKNOWN`.

### AND

| A     | B     | A AND B |
| ----- | ----- | ------- |
| TRUE  | TRUE  | TRUE    |
| TRUE  | FALSE | FALSE   |
| TRUE  | NULL  | NULL    |
| FALSE | NULL  | FALSE   |

---

### OR

| A     | B    | A OR B |
| ----- | ---- | ------ |
| TRUE  | NULL | TRUE   |
| FALSE | NULL | NULL   |
| NULL  | NULL | NULL   |

---

### NOT

| A     | NOT A |
| ----- | ----- |
| TRUE  | FALSE |
| FALSE | TRUE  |
| NULL  | NULL  |

📌 `WHERE` keeps **only TRUE rows**.

---

## 🔗 Logical Operators with JOINs

### ❌ Wrong (Kills LEFT JOIN)

```sql
SELECT u.name
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
WHERE o.status = 'PAID'
AND o.amount > 100;
```

---

### ✅ Correct

```sql
SELECT u.name
FROM users u
LEFT JOIN orders o
ON u.id = o.user_id
AND o.status = 'PAID'
AND o.amount > 100;
```

---

## 🧠 De Morgan’s Laws (Interview Favorite)

```
NOT (A AND B) = (NOT A) OR (NOT B)
NOT (A OR B)  = (NOT A) AND (NOT B)
```

### Example

```sql
WHERE NOT (salary > 50000 AND department = 'IT');
```

Same as:

```sql
WHERE salary <= 50000
OR department <> 'IT';
```

---

## ✅ One-Page Mental Model

* `AND` → stricter (more restrictive)
* `OR` → broader (more inclusive)
* `NOT` → flips result
* `AND > OR` (precedence)
* Parentheses save lives 😄
* `NULL` creates `UNKNOWN`
