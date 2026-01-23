# FOREIGN KEY in PostgreSQL

A **FOREIGN KEY** ensures that values in a column (or group of columns) exist in a referenced parent table.

It enforces **referential integrity** between tables.

---

## 1️⃣ Basic FOREIGN KEY Example

### Parent table

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name TEXT
);
```

### Child table (with FOREIGN KEY)

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### What this means
- `orders.user_id` must exist in `users.id`
- Prevents **orphan records**
- Ensures **referential integrity**

---

## 2️⃣ FOREIGN KEY with ON DELETE and ON UPDATE

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

### Behavior
- **ON DELETE CASCADE** → deleting a user deletes their orders
- **ON UPDATE CASCADE** → updating `users.id` updates `orders.user_id`

---

## 3️⃣ Named FOREIGN KEY Constraint (Best Practice)

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    CONSTRAINT fk_orders_users
        FOREIGN KEY (user_id)
        REFERENCES users(id)
);
```

### Why name it?
- Easier debugging
- Easier to drop or modify later
- Cleaner schema design

---

## 4️⃣ FOREIGN KEY Allowing NULL

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY,
    user_id INT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

📌 **Important**
- `user_id` **can be NULL**
- But if it is **NOT NULL**, it must exist in `users`

---

## 5️⃣ Composite FOREIGN KEY (Multiple Columns)

### Parent table

```sql
CREATE TABLE courses (
    course_id INT,
    semester INT,
    PRIMARY KEY (course_id, semester)
);
```

### Child table

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    semester INT,
    FOREIGN KEY (course_id, semester)
        REFERENCES courses(course_id, semester)
);
```

✔ Column order must match  
✔ Data types must match  

---

## 🔑 Key Rules to Remember (Interview Gold)

- FOREIGN KEY **can be NULL**
- FOREIGN KEY can reference **PRIMARY KEY or UNIQUE**
- A table can have **multiple foreign keys**
- Parent column must be **indexed** (PRIMARY KEY or UNIQUE)

---

## 🧠 PRIMARY KEY vs FOREIGN KEY (Quick)

| PRIMARY KEY | FOREIGN KEY |
|------------|-------------|
| Identifies a row | References another table |
| UNIQUE + NOT NULL | Can be NULL |
| One per table | Multiple allowed |

---