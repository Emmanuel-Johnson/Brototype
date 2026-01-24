# 🔗 What is a SELF JOIN?

A **SELF JOIN** is when:

* A table is joined with **itself**

There is **no special keyword** for SELF JOIN —
it’s just a normal `JOIN` using **table aliases**.

---

## 🧠 Why do we need SELF JOIN?

When a table has a **relationship within itself**, like:

* Employee → Manager
* Category → Parent Category
* Comment → Reply
* Folder → Parent Folder

---

## 1️⃣ Basic SELF JOIN Syntax

```sql
SELECT a.column, b.column
FROM table a
JOIN table b
ON a.common_column = b.common_column;
```

👉 **Aliases (`a`, `b`) are mandatory** to distinguish the same table.

---

## 2️⃣ Example: Employees and Managers

### Table structure

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name TEXT,
    manager_id INT
);
```

`manager_id` references `employees.id`

---

### SELF JOIN Query

```sql
SELECT
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.id;
```

### Result

* Employees **with managers** → manager name shown
* **Top-level managers** → `NULL` manager

✔ `LEFT JOIN` is important here

---

## 3️⃣ Find Employees Without Managers

```sql
SELECT e.name
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.id
WHERE m.id IS NULL;
```

---

## 4️⃣ Hierarchical Example: Categories

```sql
SELECT
    child.name AS category,
    parent.name AS parent_category
FROM categories child
LEFT JOIN categories parent
ON child.parent_id = parent.id;
```

Used in:

* Menus
* Tree structures
* Nested comments

---

## ❌ Common Mistakes

* ❌ Forgetting table aliases
* ❌ Using `INNER JOIN` when `NULL`s are needed
* ❌ Confusing **parent** vs **child** sides

---

## 🔑 Interview Key Points

* SELF JOIN = table joined to itself
* No special syntax
* Aliases are mandatory
* Used for hierarchical data

---

## 🧠 Mental Model

> “Treat the same table as two different roles.”
