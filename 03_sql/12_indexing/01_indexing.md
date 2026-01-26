# 📌 Database Indexing – Complete Notes

## 1️⃣ What is Indexing?

**Indexing** is a database technique used to speed up data retrieval from a table.

👉 Instead of scanning every row (**full table scan**), the database uses an **index** to quickly locate the required rows.

💡 **Analogy**:

* Book without index → read every page
* Book with index → jump directly to the page

---

## 2️⃣ What is an Index?

An **index** is a separate data structure that stores:

* Column values
* A pointer/reference to the actual row in the table

📌 Indexes are usually implemented using:

* **B-Tree** (most common)
* **Hash index** (used for exact matches)

### Example

```sql
CREATE INDEX idx_emp_name ON employee(emp_name);
```

```sql
SELECT * FROM employee WHERE emp_name = 'Rahul';
```

🚀 This query becomes much faster.

---

## 3️⃣ How Indexing Works (Internally)

### ❌ Without Index

* Database checks rows one by one
* Linear search → **O(n)**

### ✅ With Index

1. Database looks into the index structure
2. Finds the matching key value
3. Gets the row address (pointer)
4. Fetches the row directly

🧠 **Using B-Tree**:

* Data is stored in sorted order
* Search time ≈ **O(log n)**

---

## 4️⃣ Clustered Index

### 🔹 Definition

A **clustered index** determines the **physical order** of data in a table.

📌 **Rules**:

* Data rows are stored in index order
* Only **ONE** clustered index per table
* Usually created on **PRIMARY KEY**

### 📘 Example

```sql
PRIMARY KEY (emp_id)
```

Table data on disk:

```
emp_id: 1 → 2 → 3 → 4
```

🧠 **Think**: The table *is* the clustered index.

---

## 5️⃣ Non-Clustered Index

### 🔹 Definition

A **non-clustered index**:

* Stores index values separately
* Contains pointers to actual table rows
* Does **NOT** change physical data order

📌 **Key Points**:

* Multiple non-clustered indexes allowed
* Slightly slower than clustered index
* Smaller than table data

### 📘 Example

```sql
CREATE INDEX idx_dept ON employee(dept_id);
```

Structure:

```
dept_id → row pointer
```

🧠 **Think**: Index is separate, table stays the same.

---

## 6️⃣ Clustered vs Non-Clustered Index

| Feature        | Clustered Index     | Non-Clustered Index |
| -------------- | ------------------- | ------------------- |
| Physical order | Changes table order | No change           |
| Number allowed | Only one            | Many                |
| Speed          | Faster              | Slightly slower     |
| Storage        | Table itself        | Separate structure  |
| Common use     | Primary key         | Search columns      |

---

## 7️⃣ Advantages of Indexing ✅

✔ Faster `SELECT` queries
✔ Efficient searching & sorting
✔ Improves `JOIN` performance
✔ Reduces disk I/O
✔ Essential for large tables

---

## 8️⃣ Disadvantages of Indexing ❌

❌ Extra storage space required
❌ Slower `INSERT`, `UPDATE`, `DELETE` operations
❌ Too many indexes hurt performance
❌ Index maintenance overhead

⚠️ **Rule of Thumb**:
Index **read-heavy columns**, not frequently updated ones.

---

## 9️⃣ When to Use Indexing?

### ✅ Use When:

* Table is large
* Column used in `WHERE`, `JOIN`, `ORDER BY`
* Data is read frequently

### ❌ Avoid When:

* Table is small
* Column has very few unique values
* Heavy write operations (frequent updates)

---