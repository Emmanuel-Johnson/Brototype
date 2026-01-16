# Primary Key vs Unique Key

Both **Primary Key** and **Unique Key** are used to ensure uniqueness in a database, but they serve different purposes and follow different rules.

---

## Primary Key

A **Primary Key** uniquely identifies each row in a table.

### Key Characteristics

- Must be **unique**
- **Cannot be NULL**
- Only **one primary key** per table
- Automatically indexed
- Used as the **main identifier** for rows

### Example (Django)

```python
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
```

---

## Unique Key

A **Unique Key** ensures that a column (or combination of columns) has unique values, but it is **not** the main identifier.

### Key Characteristics

- Must be **unique**
- May allow **one NULL** (database-dependent)
- **Multiple unique keys** allowed per table
- Automatically indexed
- Used to enforce **business rules**

### Example (Django)

```python
class User(models.Model):
    email = models.EmailField(unique=True)
```

---

## Combined Unique Constraint

Used when uniqueness depends on **multiple columns**.

```python
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')
```

Ensures a student cannot enroll in the same course more than once.

---

## Quick Comparison (Interview-Friendly)

| Feature | Primary Key | Unique Key |
|------|------------|-----------|
| Uniqueness | Yes | Yes |
| NULL allowed | No | DB-dependent |
| Count per table | One | Multiple |
| Main identifier | Yes | No |
| Index created | Yes | Yes |

---

## One-Line Interview Answer

- **Primary Key** → identifies the row  
- **Unique Key** → enforces a uniqueness rule