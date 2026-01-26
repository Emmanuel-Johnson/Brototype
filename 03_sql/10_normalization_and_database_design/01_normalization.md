
# Normalization and Denormalization in Databases

## 🔹 What is Normalization?

Normalization is the process of organizing data into multiple related tables to reduce redundancy and avoid anomalies.

### 👉 Goal:
- Store data once  
- Keep data consistent  
- Avoid update / insert / delete problems  

### ✅ Why Normalization?
Without normalization, bad things happen:
- Same data repeated in many rows  
- Updating one place but forgetting others  
- Inconsistent data  

### 🧠 Example (Before Normalization)

**Orders table**

| order_id | customer_name | customer_phone | product |
|--------|---------------|----------------|---------|
| 1 | Rahul | 9999 | Laptop |
| 2 | Rahul | 9999 | Mouse |

❌ Customer info repeated

### 🧩 After Normalization

**Customers**

| customer_id | name | phone |
|------------|------|-------|
| 1 | Rahul | 9999 |

**Orders**

| order_id | customer_id | product |
|---------|-------------|---------|
| 1 | 1 | Laptop |
| 2 | 1 | Mouse |

✔ No duplication  
✔ Easy updates  
✔ Data integrity  

### 📌 Normal Forms (Quick Idea)
- **1NF** → Atomic values (no lists)  
- **2NF** → No partial dependency  
- **3NF** → No transitive dependency  

> You don’t always need to go till BCNF / 4NF in real projects.

---

## 🔹 What is Denormalization?

Denormalization is the process of intentionally adding redundancy to improve read performance.

### 👉 Goal:
- Faster SELECT queries  
- Fewer JOINs  

### ✅ Why Denormalization?
Normalization is great for consistency, but:
- Too many joins = slower reads  
- Heavy read systems need speed  

So we trade consistency for performance **(carefully)**.

### 🧠 Example (Denormalized)

**Orders table**

| order_id | customer_name | customer_phone | product |
|--------|---------------|----------------|---------|
| 1 | Rahul | 9999 | Laptop |
| 2 | Rahul | 9999 | Mouse |

✔ Faster queries  
❌ Data repeated  
❌ Updates must be handled carefully  

---

## 🔄 Normalization vs Denormalization

| Feature | Normalization | Denormalization |
|-------|---------------|-----------------|
| Redundancy | ❌ Removed | ✅ Added |
| Data integrity | High | Medium |
| Read performance | Slower | Faster |
| Write performance | Faster | Slower |
| Joins | Many | Few |
| Use case | OLTP systems | OLAP / Reporting |

---

## 🏗 Real-world Usage (Important 🔥)

Most systems use **both**:

- **Normalized** → Core transactional tables  
- **Denormalized** → Reports, dashboards, caching, analytics  

### Example:
- PostgreSQL → Normalized  
- Redis / Materialized Views → Denormalized  

---

## 🎯 One-line Exam Answers

**Normalization:**  
Process of organizing data to reduce redundancy and maintain data integrity.

**Denormalization:**  
Process of intentionally introducing redundancy to improve query performance.