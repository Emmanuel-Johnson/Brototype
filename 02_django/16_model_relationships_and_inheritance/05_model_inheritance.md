# Model Inheritance in Django

Django supports **three types of model inheritance**:

1. Abstract Base Class  
2. Multi-table Inheritance  
3. Proxy Model  

---

## 1️⃣ Abstract Base Class

### What is it?

- Used to **share common fields**
- **No database table** is created for the base class
- Fields are **copied into child models**

---

### Example

```python
from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

### Inheriting the Base Class

```python
class Post(TimeStampedModel):
    title = models.CharField(max_length=200)


class Comment(TimeStampedModel):
    text = models.TextField()
```

---

### Database Result

- ❌ No table for `TimeStampedModel`
- ✅ `Post` and `Comment` tables contain `created_at`, `updated_at`

---

### When to Use

- Reusable common fields
- Base models like:
  - timestamps
  - soft delete
  - audit fields

---

## 2️⃣ Multi-table Inheritance

### What is it?

- Each model has its **own database table**
- Child model has an **implicit OneToOneField** to parent
- Parent data stored separately

---

### Example

```python
class Person(models.Model):
    name = models.CharField(max_length=100)


class Student(Person):
    roll_no = models.IntegerField()
```

---

### Database Structure

**person**
```
id
name
```

**student**
```
id
person_ptr_id  (OneToOneField)
roll_no
```

---

### Accessing Data

```python
student = Student.objects.get(id=1)

student.name       # from Person
student.roll_no    # from Student
```

---

### Query Parent → Child

```python
person = Person.objects.get(id=1)
person.student
```

---

### When to Use

- Clear **“is-a” relationship**

Examples:
- Person → Employee
- Vehicle → Car

---

### Drawbacks

- Extra JOINs (slower)
- More complex queries

---

## 3️⃣ Proxy Model

### What is it?

- ❌ No new table
- ❌ No new fields
- ✅ Changes behavior only, not structure

---

### Example

```python
class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)


class CompletedOrder(Order):
    class Meta:
        proxy = True

    def is_completed(self):
        return self.status == "completed"
```

---

### Usage

```python
orders = CompletedOrder.objects.filter(status="completed")

for order in orders:
    print(order.is_completed())
```

---

### When to Use

- Custom model methods
- Custom managers
- Different admin behavior

---

## Comparison Table

| Feature | Abstract Base | Multi-table | Proxy |
|------|---------------|------------|-------|
| DB table for base | ❌ No | ✅ Yes | ❌ No |
| DB table for child | ✅ Yes | ✅ Yes | ❌ No |
| Extra fields allowed | ✅ Yes | ✅ Yes | ❌ No |
| Performance | Fast | Slower (joins) | Fast |
| Use case | Share fields | True inheritance | Change behavior |

---

## Quick Interview One-liners

- **Abstract Base** → “Code reuse, no DB table”
- **Multi-table** → “Each model has its own table”
- **Proxy** → “Same table, different behavior”

---

## Common Mistake

❌ Using multi-table inheritance when abstract base class is enough  
✅ Prefer **abstract base class** unless you really need parent queries