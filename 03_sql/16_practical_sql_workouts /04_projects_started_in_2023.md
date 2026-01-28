## ✅ Scenario: Projects Started in 2023

### Assumed Table

```sql
projects(project_id, project_name, start_date)
```

---

## ✅ Query Using EXTRACT

```sql
SELECT project_name
FROM projects
WHERE EXTRACT(YEAR FROM start_date) = 2023;
```

---

## 🧠 Simple Explanation

* `EXTRACT(YEAR FROM start_date)` → gets the **year part** from the date
* `= 2023` → filters only projects **started in 2023**

---

## 🔑 Important Notes (Interview / Exam)

* `EXTRACT` works with `DATE` and `TIMESTAMP`
* Very common in **PostgreSQL interview & exam questions**
* Syntax is **easy to remember and readable**

---

## ⚡ Better Performance Version (Best Practice)

```sql
WHERE start_date >= DATE '2023-01-01'
  AND start_date <  DATE '2024-01-01';
```

📌 **Reason:**

* Avoids applying a function on the column
* Allows PostgreSQL to **use indexes efficiently**

---

## 📝 One-Line Exam Answer

> Use `EXTRACT(YEAR FROM date_column)` to filter rows by year.
