## 🔗 What is Many-to-Many?

A **Many-to-Many relationship** means:

- One row in **Table A** can relate to **many rows** in **Table B**
- One row in **Table B** can relate to **many rows** in **Table A**

### Examples
- **Students** ↔ **Courses**
- **Users** ↔ **Roles**
- **Products** ↔ **Orders**

---

## ❗ Important Rule

👉 Relational databases **do NOT support Many-to-Many directly**

You must use a **junction (bridge) table**.

---

## ✅ Correct Implementation (Junction Table)

### Example: Students ↔ Courses

### 1️⃣ Table A (Students)

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

### 2️⃣ Table B (Courses)

```sql
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    title TEXT
);
```

### 3️⃣ Junction Table (Many-to-Many)

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrolled_at TIMESTAMP,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

### 🧠 Why this works
- Each student can appear **many times**
- Each course can appear **many times**
- Composite PRIMARY KEY prevents **duplicate pairs**
- Foreign keys ensure **data integrity**

✔ This is a **true Many-to-Many**

---

## 🔁 Alternative: Surrogate Key (Sometimes Used)

```sql
CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrolled_at TIMESTAMP,
    UNIQUE (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```

### Used when:
- You want a **simple primary key**
- Junction table has **many extra columns**
- You plan to reference the junction table directly

---

## ❌ Common Mistakes

- ❌ No junction table
- ❌ Putting multiple IDs in one column
- ❌ Missing `UNIQUE` or composite PRIMARY KEY
- ❌ FOREIGN KEY referencing a non-unique column

---

## 🔑 Interview Key Points

- Many-to-Many **always needs a junction table**
- Junction table has **two foreign keys**
- Composite PRIMARY KEY is **best practice**
- Surrogate key is **optional**, not mandatory

---

## 🧩 Visual Memory Trick

```
students ──< enrollments >── courses
      1        many      1
```

---

## 🌍 Real-World Examples

| Table A | Junction | Table B |
|-------|----------|---------|
| Users | user_roles | Roles |
| Orders | order_products | Products |
| Movies | movie_actors | Actors |

---