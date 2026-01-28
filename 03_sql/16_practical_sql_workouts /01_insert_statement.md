## 1️⃣ Basic INSERT (Single Row)

```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

### 📌 Example

```sql
INSERT INTO employees (id, name, salary)
VALUES (1, 'John', 50000);
```

---

## 2️⃣ INSERT Without Column List

⚠️ Use this **only if you know the column order exactly**.

```sql
INSERT INTO employees
VALUES (1, 'John', 50000);
```

---

## 3️⃣ INSERT Multiple Rows

✅ Faster than inserting one row at a time.

```sql
INSERT INTO employees (id, name, salary)
VALUES
(2, 'Alice', 60000),
(3, 'Bob', 55000);
```

---

## 4️⃣ INSERT with DEFAULT Values

### Using DEFAULT for specific columns

```sql
INSERT INTO employees (name, salary)
VALUES ('David', DEFAULT);
```

### All default values

```sql
INSERT INTO employees
DEFAULT VALUES;
```

---

## 5️⃣ INSERT Data from Another Table

```sql
INSERT INTO employees_backup (id, name, salary)
SELECT id, name, salary
FROM employees
WHERE salary > 50000;
```

---

## 6️⃣ INSERT and RETURN Inserted Row (PostgreSQL Special 💡)

### Return all columns

```sql
INSERT INTO employees (name, salary)
VALUES ('Emma', 65000)
RETURNING *;
```

### Return specific columns

```sql
RETURNING id, name;
```

---

## 7️⃣ Handling Auto-Increment Columns (SERIAL / IDENTITY)

```sql
INSERT INTO employees (name, salary)
VALUES ('Mike', 48000);
```

📌 PostgreSQL automatically generates the `id` value.

---

## 🔑 Key Things to Remember (Exam‑Friendly)

* `INSERT INTO` adds new rows to a table
* Column list is optional but **recommended**
* `RETURNING` is **PostgreSQL‑specific**
* Use `DEFAULT` for default column values
* Multiple row inserts are **faster** than single inserts
