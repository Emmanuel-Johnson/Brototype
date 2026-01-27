# SQL Injection

## 1️⃣ What is SQL Injection?

**SQL Injection** is a security attack where an attacker inserts
malicious SQL code into an application's input field to access, modify,
or delete database data.

📌 **In short:**\
User input is treated as SQL code instead of data.

**Definition (exam-friendly):**\
SQL Injection is an attack in which malicious SQL statements are
inserted into application inputs to manipulate the database.

------------------------------------------------------------------------

## 2️⃣ How SQL Injection Happens

### ❌ Vulnerable Code (Example)

``` sql
SELECT * FROM users 
WHERE username = 'admin' AND password = '1234';
```

If the application builds this query using raw user input:

    username = admin
    password = ' OR '1'='1

### 🔥 Final Query Becomes

``` sql
SELECT * FROM users 
WHERE username = 'admin' AND password = '' OR '1'='1';
```

💥 `'1'='1'` is always true, so:

-   Authentication is bypassed
-   Attacker logs in without knowing the password

------------------------------------------------------------------------

## ⚠️ What Attackers Can Do

-   Bypass login
-   Read sensitive data
-   Delete tables
-   Modify records
-   Execute admin-level queries

### Example

``` sql
DROP TABLE users;
```

------------------------------------------------------------------------

## 3️⃣ Preventing SQL Injection

### ✅ 1. Use Prepared Statements (MOST IMPORTANT)

``` sql
SELECT * FROM users WHERE username = ? AND password = ?;
```

✔ User input is treated as data, not SQL\
✔ Works in PostgreSQL, MySQL, Django ORM, etc.

------------------------------------------------------------------------

### ✅ 2. Use ORM (Django / SQLAlchemy)

Since you're in **Brototype (Django + React)** --- this is 🔥 important:

``` python
User.objects.filter(username=username, password=password)
```

✔ ORM automatically prevents SQL injection

------------------------------------------------------------------------

### ✅ 3. Input Validation

-   Reject unexpected characters
-   Limit input length
-   Validate types (numbers, emails, etc.)

------------------------------------------------------------------------

### ✅ 4. Least Privilege Principle

Application user should **NOT** be SUPERUSER.

``` sql
GRANT SELECT, INSERT ON users TO app_user;
```

------------------------------------------------------------------------

### ✅ 5. Avoid Dynamic SQL

❌ Bad:

``` sql
"SELECT * FROM users WHERE name = '" + user_input + "'";
```

✔ Good: - Prepared statements - ORM queries

------------------------------------------------------------------------

## 📌 One-Line Summary (Perfect for Exams)

-   **SQL Injection:** Injecting malicious SQL via user input
-   **Cause:** Unsanitized / dynamic SQL queries
-   **Prevention:** Prepared statements, ORM, input validation, least
    privilege