## 1️⃣ CREATE USER vs CREATE ROLE

### 👉 Key Idea
In PostgreSQL, **users and roles are the same internally**.  
A **user is simply a role with LOGIN permission**.

---

### 🔹 CREATE ROLE
Creates a role **without login** by default.

```sql
CREATE ROLE manager;
```

**Characteristics:**
- ❌ Cannot log in
- ✅ Used to group permissions
- ✅ Other users/roles can be assigned this role

**Best for:**
- Permission grouping
- Role-Based Access Control (RBAC)

---

### 🔹 CREATE USER
Shortcut for creating a role **with LOGIN permission**.

```sql
CREATE USER alice WITH PASSWORD 'password123';
```

**Internally same as:**
```sql
CREATE ROLE alice LOGIN PASSWORD 'password123';
```

**Characteristics:**
- ✅ Can log in
- ✅ Represents a real user or application

---

### 🔁 Quick Comparison

| Feature | CREATE ROLE | CREATE USER |
|------|-----------|-----------|
| Can login | ❌ No (default) | ✅ Yes |
| Can hold permissions | ✅ Yes | ✅ Yes |
| Can be assigned roles | ✅ Yes | ✅ Yes |
| Internal difference | ❌ None | ❌ None |

📌 **Exam Line:**  
PostgreSQL treats users and roles the same; a user is a role with LOGIN privilege.

---

## 2️⃣ GRANT Permissions (PostgreSQL)

Used to **give privileges** on database objects.

### 🔹 Granting privileges on tables
```sql
GRANT SELECT ON table_name TO role_name;
```

**Multiple permissions:**
```sql
GRANT SELECT, INSERT, UPDATE ON table_name TO user1;
```

**All permissions:**
```sql
GRANT ALL PRIVILEGES ON table_name TO user1;
```

---

### 🔹 Grant on database
```sql
GRANT CONNECT ON DATABASE mydb TO user1;
```

---

### 🔹 Grant role to another role (Role Inheritance)
```sql
GRANT manager TO alice;
```

📌 Meaning:  
`alice` inherits all permissions of `manager`.

---

### 🔹 Grant on schema
```sql
GRANT USAGE ON SCHEMA public TO user1;
```

📌 Without this → user cannot access objects inside the schema.

---

### 🔹 Grant Default Privileges (IMPORTANT)
Applies to **future objects**.

```sql
ALTER DEFAULT PRIVILEGES
GRANT SELECT ON TABLES TO user1;
```

---

## 3️⃣ REVOKE Permissions

Used to **remove privileges**.

### 🔹 Revoke table permission
```sql
REVOKE SELECT ON table_name FROM user1;
```

### 🔹 Revoke multiple permissions
```sql
REVOKE INSERT, UPDATE ON table_name FROM user1;
```

### 🔹 Revoke role
```sql
REVOKE manager FROM alice;
```

### 🔹 Revoke all permissions
```sql
REVOKE ALL PRIVILEGES ON table_name FROM user1;
```

---

## 4️⃣ Role Attributes (VERY IMPORTANT)

Often asked indirectly 👇

```sql
CREATE ROLE admin WITH
LOGIN
SUPERUSER
CREATEDB
CREATEROLE;
```

| Attribute | Meaning |
|--------|--------|
| LOGIN | Can log in |
| SUPERUSER | Full access |
| CREATEDB | Can create databases |
| CREATEROLE | Can create roles |
| INHERIT | Inherit role permissions (default) |
| NOINHERIT | Must use SET ROLE explicitly |

---

## 5️⃣ SET ROLE vs INHERIT

```sql
SET ROLE manager;
```

📌 Temporarily switches to role permissions.

- **INHERIT** → permissions are automatic
- **NOINHERIT** → must explicitly use `SET ROLE`

---

## 6️⃣ Ownership vs Privileges (Common Confusion)

- **Owner** → full control, cannot be revoked
- **Privileges** → granted/revoked

```sql
ALTER TABLE table_name OWNER TO new_owner;
```

---

## 7️⃣ Real-World Best Practice (Interview Gold ⭐)

- Create roles for permissions
- Assign roles to users
- Never grant permissions directly to users

**Example:**
```sql
CREATE ROLE readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly;
GRANT readonly TO alice;
```

---

## 🧠 One-Page Exam Summary

- CREATE USER = role with LOGIN
- CREATE ROLE = permission container
- GRANT → give permission
- REVOKE → remove permission
- Roles can inherit roles
- Default privileges affect future objects