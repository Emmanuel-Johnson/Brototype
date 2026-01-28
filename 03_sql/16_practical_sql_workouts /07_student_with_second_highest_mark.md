## Find the Second Highest Mark (PostgreSQL)

### ✅ 1️⃣ Using `OFFSET` (simple & clean)

```sql
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 1 OFFSET 1;
```

* 🔹 Works when **marks are unique**
* 🔹 Easy to understand

---

### ✅ 2️⃣ Using `MAX()` (handles duplicates correctly) ⭐ **BEST**

```sql
SELECT *
FROM students
WHERE marks = (
  SELECT MAX(marks)
  FROM students
  WHERE marks < (
    SELECT MAX(marks)
    FROM students
  )
);
```

* 🔹 Returns **all students with the second highest mark**
* 🔹 **Interview‑safe answer**

---

### ✅ 3️⃣ Using `DISTINCT` + `ORDER BY`

```sql
SELECT *
FROM students
WHERE marks = (
  SELECT DISTINCT marks
  FROM students
  ORDER BY marks DESC
  OFFSET 1
  LIMIT 1
);
```

---

## ⚠️ Important Interview Notes

| Method   | Handles ties | Recommended |
| -------- | ------------ | ----------- |
| OFFSET   | ❌ No         | ❌ No        |
| MAX()    | ✅ Yes        | ✅ Yes       |
| DISTINCT | ✅ Yes        | ✅ Yes       |
