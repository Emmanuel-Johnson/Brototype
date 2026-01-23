## 🔗 What is One-to-Many?

A **One-to-Many relationship** means:

- One row in **Table A** can be related to **many rows** in **Table B**
- Each row in **Table B** relates to **only one row** in **Table A**

### Examples
- One **User** → Many **Orders**
- One **Category** → Many **Products**
- One **Author** → Many **Books**

---

## ✅ How to Implement One-to-Many (Correct Way)

📌 The **FOREIGN KEY always goes on the “many” side**.

---

## 1️⃣ Example: Users → Orders

### Parent table (ONE side)

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

### Child table (MANY side)

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 🧠 Why this works
- `users.id` → PRIMARY KEY
- `orders.user_id` → FOREIGN KEY
- Many orders can share the same `user_id`
- Each order belongs to **one user only**

✔ This is a **true One-to-Many**

---

## 2️⃣ One-to-Many with NOT NULL (Mandatory Relationship)

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

📌 Every order **must belong to a user**

---

## 3️⃣ One-to-Many with ON DELETE Rules

### a) CASCADE (Most Common)

```sql
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE CASCADE
```

➡ Delete user → delete all related orders

---

### b) SET NULL

```sql
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE SET NULL
```

➡ User deleted → orders remain, `user_id` becomes `NULL`

⚠️ Column must allow `NULL`

---

### c) RESTRICT / NO ACTION (Default)

```sql
FOREIGN KEY (user_id)
REFERENCES users(id)
ON DELETE RESTRICT
```

➡ Cannot delete user if orders exist

---

## ❌ Common Mistake

Adding `UNIQUE` to the foreign key:

```sql
user_id INT UNIQUE
```

❌ This turns it into **One-to-One**, not One-to-Many

---

## 🔑 Interview Key Points

- FOREIGN KEY is **always on the many side**
- Foreign key **can be NULL**
- Parent column must be **PRIMARY KEY or UNIQUE**
- One table can have **multiple foreign keys**

---

## 🧩 Visual Logic (Easy to Remember)

```
users (1) ────────< orders (many)
        PK        FK
```

---

## 🚀 Real-World Examples

| One | Many |
|----|------|
| User | Orders |
| Category | Products |
| Department | Employees |
| Blog | Comments |

---