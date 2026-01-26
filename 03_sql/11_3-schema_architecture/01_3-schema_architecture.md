
# 3-Schema Architecture 🧱

The **3-Schema Architecture** is a database design concept that separates a database system into **three levels**.

### 👉 Why?
To achieve:
- **Data abstraction**
- **Data independence**  
(Changes in one level don’t affect the others)

---

## 1️⃣ Internal Schema (Physical Level)

### 🔹 What it describes
- How data is **actually stored** in the database
- Physical storage details

### 🔹 Includes
- File organization  
- Indexes  
- B-trees, hashing  
- Disk blocks, pointers, compression  

### 🔹 Who cares about this
- Database Administrators (DBA)  
- Database engine  

### 🔹 Example
- Employee table stored in disk blocks  
- Index on `emp_id` using B-tree  

📌 **Users never see this level.**

---

## 2️⃣ Conceptual Schema (Logical Level)

### 🔹 What it describes
- Overall **structure of the database**
- What data is stored & how it is related
- Independent of physical storage

### 🔹 Includes
- Tables  
- Columns  
- Data types  
- Constraints (PK, FK, UNIQUE)  
- Relationships  

### 🔹 Who cares about this
- Database designers  
- Developers  

### 🔹 Example
```
EMPLOYEE(emp_id, emp_name, dept_id)
DEPARTMENT(dept_id, dept_name)
```

📌 **This is the single global view of the database.**

---

## 3️⃣ External Schema (View Level)

### 🔹 What it describes
- How **different users** see the data
- Each user/application can have its own view

### 🔹 Includes
- Subsets of tables  
- Views  
- Hidden or restricted columns  

### 🔹 Who cares about this
- End users  
- Applications  

### 🔹 Example
- **HR View** → emp_id, emp_name, dept_name  
- **Payroll View** → emp_id, salary  

📌 **One database → many external schemas.**

---

## 🔁 How They Work Together

```
User View (External Schema)
        ↓
Logical Design (Conceptual Schema)
        ↓
Physical Storage (Internal Schema)
```

---

## 🎯 Key Benefits

- ✅ Data abstraction  
- ✅ Security (users see only what they need)  
- ✅ Data independence  

### Types of Data Independence
- **Physical data independence** → Change storage without affecting tables  
- **Logical data independence** → Change tables without breaking user views  

---

## 🧠 Exam Tip (Easy Memory Trick)

- **External** → What users see  
- **Conceptual** → What the database *is*  
- **Internal** → How data is stored  

---