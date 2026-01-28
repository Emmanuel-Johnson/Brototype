## Find the Top Scoring Student

### 1️⃣ Using `ORDER BY` (most common & interview-friendly)

```sql
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 1;
```

---

### 2️⃣ Using `MAX()` (conceptually clean)

```sql
SELECT *
FROM students
WHERE marks = (
  SELECT MAX(marks)
  FROM students
);
```

👉 This approach is better when **multiple students have the same highest mark**.

---

### 3️⃣ If you want only `name` + `marks`

```sql
SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 1;
```

---

## ⚠️ Important Interview Notes

* **`LIMIT 1`** → returns **only one row**, even if there is a tie
* **`MAX()`** → returns **all toppers** if multiple students share the highest marks
