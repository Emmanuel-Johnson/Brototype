## What is the Meta Class?

The **Meta class** is an inner class inside a Django model used to define **model-level configuration**.

👉 It controls **how the model behaves**, not **what data it stores**.

---

## Basic Structure

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        pass
```

- `Meta` does **not** create database columns
- It affects **queries, admin UI, constraints, and table behavior**

---

## Commonly Used Meta Options

---

### 1️⃣ `ordering`

Sets the **default order** for querysets.

```python
class Meta:
    ordering = ["-created_at"]
```

---

### 2️⃣ `verbose_name` & `verbose_name_plural`

Human‑readable names (used in Django admin).

```python
class Meta:
    verbose_name = "Book"
    verbose_name_plural = "Books"
```

---

### 3️⃣ `db_table`

Specify a **custom database table name**.

```python
class Meta:
    db_table = "library_books"
```

---

### 4️⃣ `unique_together` (Legacy)

Ensures a **combination of fields is unique**.

```python
class Meta:
    unique_together = ("student", "course")
```

⚠️ Legacy option — prefer `constraints`.

---

### 5️⃣ `constraints` (Recommended)

Modern and flexible database constraints.

```python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["email"],
            name="unique_email"
        )
    ]
```

---

### 6️⃣ `indexes`

Add database indexes for performance.

```python
class Meta:
    indexes = [
        models.Index(fields=["title"]),
    ]
```

---

### 7️⃣ `abstract`

Used in **abstract base models**.

```python
class Meta:
    abstract = True
```

---

### 8️⃣ `proxy`

Used in **proxy models**.

```python
class Meta:
    proxy = True
```

---

### 9️⃣ `permissions`

Define **custom permissions**.

```python
class Meta:
    permissions = [
        ("can_publish", "Can publish books"),
    ]
```

---

### 🔟 `managed`

Tell Django whether it should manage the table.

```python
class Meta:
    managed = False
```

Useful for **legacy databases**.

---

## Realistic Example

```python
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        ordering = ["student"]
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_student_course"
            )
        ]
```

---

## Important Facts (Interview‑Ready)

- `Meta` is **optional**
- One model → **one Meta class**
- Controls **behavior**, not fields
- Evaluated at **model load time**
- Used heavily by **Django admin & ORM**

---

## Common Mistakes

❌ Thinking `Meta` creates database fields  
❌ Forgetting to run migrations after Meta changes  
❌ Overusing `db_table` unnecessarily  

---

## One‑Line Summary

**The Meta class defines how a Django model behaves, not what it stores.**

<br>
<br>
<br>

## What is `ordering`?

`ordering` defines the **default order of records** returned by a model’s queryset.

It is defined inside the model’s `Meta` class.

```python
class Meta:
    ordering = [...]
```

➡ Automatically applied to:

- `Model.objects.all()`
- `Model.objects.filter(...)`

---

## Basic Example

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()

    class Meta:
        ordering = ["price"]
```

### Result

- Records are sorted by **price (ascending)**

---

## Descending Order

```python
class Meta:
    ordering = ["-price"]
```

- `-` means **descending order**

---

## Multiple Fields Ordering

```python
class Meta:
    ordering = ["price", "-title"]
```

### Meaning

1. Order by `price` **ASC**
2. If prices are the same → order by `title` **DESC**

---

## Ordering by Related Fields

```python
class Book(models.Model):
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        ordering = ["publisher__name"]
```

- Uses Django’s **double underscore (`__`) lookup**
- Orders books by publisher name

---

## Ordering by Date (Common Use Case)

```python
class Meta:
    ordering = ["-created_at"]
```

- Newest records appear **first**

---

## Override Default Ordering

You can override `Meta.ordering` in queries.

```python
Book.objects.order_by("title")
Book.objects.order_by("-price")
```

---

## Remove Ordering Completely

```python
Book.objects.order_by()
```

- Useful when default ordering hurts performance

---

## Ordering with NULL Values

Django supports `nulls_first` and `nulls_last`.

```python
from django.db.models import F

Book.objects.order_by(
    F("price").asc(nulls_last=True)
)
```

---

## Performance Notes

- `ordering` adds an `ORDER BY` clause in SQL
- Ordering on **non-indexed fields** can be slow
- Avoid heavy ordering on **large tables**

---

## Common Mistakes

❌ Forgetting `-` for descending order  
❌ Assuming `ordering` affects `.get()`  
❌ Overusing complex ordering in `Meta`  

---

## Interview One-Liners

- `ordering` defines default queryset order  
- Can be overridden using `order_by()`  
- Supports multiple fields & related fields  

---

## Quick Summary

- Put default order in `Meta`
- Use `-` for descending
- Override when needed
- Be careful with performance

<br>
<br>
<br>

## What is `verbose_name`?

`verbose_name` is a **human-readable name** for a **model or field**.

👉 It is mainly used in:

- Django Admin
- Forms
- Error messages

It does **not** affect the database structure.

---

## `verbose_name` in Model (Meta class)

### Example

```python
class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Book Item"
```

### Admin Display

- Shows **Book Item** (singular)

---

## Plural Name (`verbose_name_plural`)

```python
class Meta:
    verbose_name = "Book Item"
    verbose_name_plural = "Book Items"
```

⚠️ If `verbose_name_plural` is **not set**, Django automatically adds **`s`**.

---

## `verbose_name` in Fields

### Example

```python
class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Book Title"
    )
```

- Admin & forms show **Book Title** instead of `title`

---

## `verbose_name` with ForeignKey

```python
class Book(models.Model):
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        verbose_name="Publisher Name"
    )
```

---

## `verbose_name` with ManyToManyField

```python
authors = models.ManyToManyField(
    Author,
    verbose_name="Book Authors"
)
```

---

## Model vs Field `verbose_name`

| Location | Purpose |
|--------|---------|
| Model `Meta` | Display model name |
| Field | Display field label |

---

## Why Use `verbose_name`?

- Makes Django Admin UI cleaner
- Improves form labels
- Produces better error messages
- Helpful for non-technical users

---

## Best Practices

- Use **Title Case** for display
- Use **singular** for `verbose_name`
- Use **plural** for `verbose_name_plural`
- Always use it in **reusable apps**

---

## Common Mistakes

❌ Using `snake_case`  
❌ Forgetting `verbose_name_plural`  
❌ Thinking it affects database structure  

---

## Interview One-Liner

**`verbose_name` controls the human-friendly display name, not the database name.**

---

## Quick Summary

- `verbose_name` = display name
- Used in admin & forms
- Does not affect database
- Works for models & fields

<br>
<br>
<br>

## What is `unique_together`?

`unique_together` is a **Meta option** used to enforce **uniqueness across a combination of fields**.

👉 The **pair / group of fields must be unique**, not the individual fields.

---

## Basic Example  
### Student–Course Enrollment

```python
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "course")
```

### Meaning

- ✔ A student can enroll in **many courses**
- ❌ The same student **cannot enroll twice** in the same course

---

## How It Works

- Django creates a **database-level UNIQUE constraint**
- Enforced at the **database level**, not just Django validation
- Violations raise an **IntegrityError**

---

## Multiple Unique Combinations

```python
class Meta:
    unique_together = [
        ("student", "course"),
        ("student", "semester"),
    ]
```

---

## Query Behavior

```python
Enrollment.objects.create(student=s1, course=c1)
Enrollment.objects.create(student=s1, course=c1)  # ❌ IntegrityError
```

---

## `unique_together` vs `unique=True`

| Feature | unique=True | unique_together |
|------|-------------|-----------------|
| Scope | Single field | Multiple fields |
| Example | email | (student, course) |
| Flexibility | Low | Medium |

---

## Important Notes

- Order of fields **does not matter**
- Works with:
  - `CharField`
  - `ForeignKey`
  - Any field type
- **Requires migrations**

---

## ⚠️ Legacy Warning

`unique_together` is **legacy**.

👉 Django now **recommends using `constraints` with `UniqueConstraint`** instead.

---

## Modern Replacement (Recommended)

```python
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["student", "course"],
            name="unique_student_course"
        )
    ]
```

### Why This Is Better

- Named constraint
- Supports conditional uniqueness
- More readable
- Future-proof

---

## Common Mistakes

❌ Forgetting migrations  
❌ Using `unique_together` in new projects  
❌ Assuming Django auto-handles duplicates  
❌ No error handling for `IntegrityError`  

---

## Interview One-Liner

**`unique_together` ensures a combination of fields is unique at the database level.**

---

## Quick Summary

- Enforces **composite uniqueness**
- Database-level constraint
- Still works, but **legacy**
- Prefer `UniqueConstraint` for new code

<br>
<br>
<br>

## What are Constraints?

**Constraints** are **database-level rules** defined in a model’s `Meta` class to enforce **data integrity**.

👉 They are the **modern replacement for `unique_together`**.

---

## Where Constraints Live

```python
class Meta:
    constraints = [
        ...
    ]
```

They are applied at the **database level**, not just Django validation.

---

## Types of Constraints

Django mainly provides **two** types:

1. `UniqueConstraint`
2. `CheckConstraint`

---

## 1️⃣ UniqueConstraint

### What It Does

Ensures **uniqueness across one or more fields**.

---

### Basic Example

```python
from django.db import models

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_student_course"
            )
        ]
```

### Meaning

- ✔ Same student can take **different courses**
- ❌ Same student **cannot take the same course twice**

---

### Conditional Uniqueness

```python
from django.db.models import Q

models.UniqueConstraint(
    fields=["email"],
    condition=Q(is_active=True),
    name="unique_active_email"
)
```

✔ Only **active users** must have unique emails

---

### Unique on Expressions

```python
from django.db.models.functions import Lower

models.UniqueConstraint(
    Lower("email"),
    name="unique_lower_email"
)
```

- Enforces **case-insensitive uniqueness**

---

## 2️⃣ CheckConstraint

### What It Does

Ensures a **logical condition is always true**.

---

### Basic Example

```python
models.CheckConstraint(
    check=models.Q(age__gte=18),
    name="age_must_be_18_plus"
)
```

❌ Prevents saving records where `age < 18`

---

### Multiple Conditions

```python
models.CheckConstraint(
    check=models.Q(start_date__lt=models.F("end_date")),
    name="valid_date_range"
)
```

✔ Ensures `start_date` is before `end_date`

---

## Constraint Naming (IMPORTANT)

- `name` is **mandatory**
- Must be **unique per database**
- Used in **migrations and database schema**

---

## constraints vs unique_together

| Feature | constraints | unique_together |
|------|-------------|-----------------|
| Flexibility | High | Low |
| Conditional rules | ✅ Yes | ❌ No |
| Readable names | ✅ Yes | ❌ No |
| Recommended | ✅ Yes | ❌ Legacy |

---

## When Constraints Are Checked

- At **database level**
- On:
  - `.save()`
  - `.create()`
  - `.bulk_create()`
- Violations raise **IntegrityError**

---

## Common Mistakes

❌ Forgetting constraint name  
❌ Using `unique_together` in new projects  
❌ Assuming Django forms catch everything  
❌ Not handling database errors  

---

## Performance Note

- Constraints add **DB-level checks**
- Proper indexing helps
- Worth it for **data safety**

---

## Interview One-Liners

- Constraints enforce **data integrity at DB level**
- `UniqueConstraint` replaces `unique_together`
- `CheckConstraint` enforces business rules

---

## Quick Summary

- Defined in `Meta.constraints`
- Modern and flexible
- Database-level protection
- **Highly recommended**