# PRIMARY KEY in PostgreSQL

A **PRIMARY KEY** uniquely identifies each row in a table.

📌 **PRIMARY KEY = UNIQUE + NOT NULL**

---

## 1️⃣ Basic PRIMARY KEY (Single Column)

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150)
);
```

### What this does
- `id` must be **UNIQUE**
- `id` **cannot be NULL**
- PostgreSQL automatically creates an **index** on `id`

---

## 2️⃣ Auto-Increment PRIMARY KEY (Most Common)

### Using SERIAL

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);
```

### Modern & Recommended → GENERATED AS IDENTITY

```sql
CREATE TABLE users (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT,
    email TEXT
);
```

✅ PostgreSQL standard  
✅ Safer than `SERIAL`  
✅ Best practice for new projects  

---

## 3️⃣ PRIMARY KEY with BIGINT (Large Systems)

```sql
CREATE TABLE orders (
    order_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_date TIMESTAMP,
    total_amount NUMERIC
);
```

✔️ Use this when you expect **millions of rows**.

---

## 4️⃣ Composite PRIMARY KEY (Multiple Columns)

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    enrolled_at TIMESTAMP,
    PRIMARY KEY (student_id, course_id)
);
```

### Rules
- Combination of columns must be **unique**
- **No column** in a PRIMARY KEY can be `NULL`

---

## 5️⃣ Named PRIMARY KEY Constraint (Interview Friendly)

```sql
CREATE TABLE products (
    product_id INT,
    name TEXT,
    CONSTRAINT products_pkey PRIMARY KEY (product_id)
);
```

### Why name it?
- Easier to reference in `ALTER TABLE`
- Cleaner error messages
- Better schema readability

---

## 🔑 Important Facts (Remember These)

- A table can have **only ONE PRIMARY KEY**
- PRIMARY KEY = **UNIQUE + NOT NULL**
- PRIMARY KEY automatically creates an **index**
- PRIMARY KEY **cannot allow NULL values**

---

## ⭐ Which One Should You Use?

| Scenario | Recommended |
|--------|-------------|
| Learning / small apps | `SERIAL` |
| Production / modern apps | `GENERATED AS IDENTITY` |
| Many-to-many tables | Composite PRIMARY KEY |

---