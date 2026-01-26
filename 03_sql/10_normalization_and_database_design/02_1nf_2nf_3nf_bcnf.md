## 🔹 1NF (First Normal Form)

### ✅ Rule
A table is in **1NF** if:
- Each column has **atomic (indivisible) values**
- No **repeating groups / arrays**
- Each row is **uniquely identifiable** (primary key)

### ❌ Not in 1NF

| id | name | phones |
|----|------|--------|
| 1 | Rahul | 9999,8888 |

❌ `phones` has multiple values

### ✔ In 1NF

| id | name | phone |
|----|------|-------|
| 1 | Rahul | 9999 |
| 1 | Rahul | 8888 |

*(Better approach → separate phone table)*

👉 **1NF = No multi-valued columns**

---

## 🔹 2NF (Second Normal Form)

### ✅ Rule
A table is in **2NF** if:
- It is already in **1NF**
- There is **no partial dependency**

### 📌 Partial Dependency
A **non-key column** depends on **only part of a composite primary key**.

### ❌ Not in 2NF

**Primary Key = (order_id, product_id)**

| order_id | product_id | product_name | quantity |
|---------|------------|--------------|----------|
| 1 | 101 | Laptop | 2 |

❌ `product_name` depends only on `product_id`, not the full key

### ✔ In 2NF

**Orders**

| order_id | product_id | quantity |
|---------|------------|----------|

**Products**

| product_id | product_name |
|-----------|--------------|

👉 **2NF = No partial dependency**

---

## 🔹 3NF (Third Normal Form)

### ✅ Rule
A table is in **3NF** if:
- It is in **2NF**
- There is **no transitive dependency**

### 📌 Transitive Dependency
A **non-key column** depends on **another non-key column**.

### ❌ Not in 3NF

| emp_id | emp_name | dept_id | dept_name |
|-------|----------|---------|-----------|

❌ `dept_name` depends on `dept_id`, not directly on `emp_id`  
(emp_id → dept_id → dept_name)

### ✔ In 3NF

**Employees**

| emp_id | emp_name | dept_id |
|-------|----------|---------|

**Departments**

| dept_id | dept_name |
|--------|-----------|

👉 **3NF = Non-key depends only on the key**

---

## 🔹 BCNF (Boyce–Codd Normal Form)

🧠 **Stronger version of 3NF**

### ✅ Rule
A table is in **BCNF** if:
- For every functional dependency **A → B**
- **A must be a super key**

### ❌ Problem Case (3NF but NOT BCNF)

| student | course | instructor |
|--------|--------|------------|

**Functional Dependencies:**
- (student, course) → instructor
- instructor → course ❌ (instructor is NOT a super key)

✔ Table is in **3NF**  
❌ Violates **BCNF**

### ✔ BCNF Fix

**Instructor_Course**

| instructor | course |
|-----------|--------|

**Student_Course**

| student | course |
|--------|--------|

👉 **BCNF removes anomalies that 3NF allows**

---

## 🔥 Quick Comparison Table

| Normal Form | Main Rule |
|-----------|-----------|
| 1NF | Atomic values, no lists |
| 2NF | No partial dependency |
| 3NF | No transitive dependency |
| BCNF | Determinant must be a super key |

---

## 🧠 Memory Tricks (Interview Gold 🏆)

- **1NF** → No repeating columns  
- **2NF** → Whole key dependency  
- **3NF** → Nothing but the key  
- **BCNF** → Only keys determine  

---