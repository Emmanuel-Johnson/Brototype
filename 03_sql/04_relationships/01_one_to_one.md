## 🔗 What is a One-to-One Relationship?

A **One-to-One relationship** means:

- One row in **Table A** is related to **exactly one row** in **Table B**
- And one row in **Table B** is related to **exactly one row** in **Table A**

### Examples
- One **User** → One **Profile**
- One **Employee** → One **ID Card**

---

## ✅ How to Implement One-to-One in PostgreSQL

There are **two correct ways**, but one is usually preferred depending on business rules.

---

## 1️⃣ FOREIGN KEY + UNIQUE  
**(Most Common & Recommended)**

### Parent table

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

### Child table

```sql
CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Why this works
- `FOREIGN KEY` → enforces relationship
- `UNIQUE` → ensures only one profile per user
- Together they create a **true one-to-one**

📌 `user_id` can be `NULL` → optional relationship  
📌 Add `NOT NULL` if profile is **mandatory**

---

## 2️⃣ Shared PRIMARY KEY  
**(Strict One-to-One)**

This is a **stronger** form of one-to-one.

### Parent table

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT
);
```

### Child table

```sql
CREATE TABLE profiles (
    user_id INT PRIMARY KEY,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Why this is powerful
- `user_id` is both **PRIMARY KEY + FOREIGN KEY**
- Profile **cannot exist without a user**
- Guarantees **exactly one profile per user**

### Use this when
- Tables are **tightly coupled**
- Child table has **no meaning on its own**

---

## ❌ Wrong Way (Common Mistake)

```sql
user_id INT
```

Without `UNIQUE` or `PRIMARY KEY`:

➡ This becomes **one-to-many**, not one-to-one ❌

---

## 🧠 Interview Comparison

| Method | When to Use |
|------|------------|
| FOREIGN KEY + UNIQUE | Optional relationship |
| Shared PRIMARY KEY | Mandatory, strict one-to-one |

---

## 🔑 Key Rules to Remember

- One-to-One **always needs UNIQUE**
- FOREIGN KEY **alone is not enough**
- Shared PRIMARY KEY = **strongest design**
- Choose based on **business rules**

---

## 🧪 Real-World Examples

- `users` ↔ `user_profiles`
- `employees` ↔ `employee_passports`
- `orders` ↔ `order_invoices`

---