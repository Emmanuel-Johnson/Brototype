# models.py — Deep Dive

## What is models.py?

`models.py` is where you define your **data structure** in Django.  
A **model** represents a database table, and each field maps to a **column**.  
Django uses models to generate SQL, manage schema, and interact with data using Python objects.

---

## Basic Model Structure

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
```

- `Product` → table name  
- Fields → columns  
- Each row → model instance  

---

## Common Model Fields (Important)

- `CharField` → short text  
- `TextField` → long text  
- `IntegerField` → numbers  
- `DecimalField` → money  
- `BooleanField` → true/false  
- `DateTimeField` → timestamps  
- `ImageField` / `FileField` → files  

---

## Primary Key & IDs

By default, Django adds:

```python
id = models.BigAutoField(primary_key=True)
```

Custom primary key example:

```python
import uuid

product_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
```

---

## Relationships (Very Important)

### One-to-One

```python
user = models.OneToOneField(User, on_delete=models.CASCADE)
```

One record ↔ one record

---

### One-to-Many (ForeignKey)

```python
category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name='products'
)
```

One category → many products

---

### Many-to-Many

```python
tags = models.ManyToManyField(Tag)
```

Django automatically creates a **join table**.

---

## on_delete Behaviors

- `CASCADE` → delete related data  
- `SET_NULL` → set field to NULL  
- `PROTECT` → block deletion  
- `SET_DEFAULT` → set default value  

---

## Model Methods

### Instance Methods

```python
def discounted_price(self):
    return self.price * 0.9
```

Encapsulates business logic inside the model.

---

## Meta Options

```python
class Meta:
    ordering = ['-created_at']
    db_table = 'products'
    verbose_name_plural = 'Products'
```

Controls table behavior and metadata.

---

## Model Validation

```python
from django.core.exceptions import ValidationError

def clean(self):
    if self.price < 0:
        raise ValidationError("Price cannot be negative")
```

Runs during model/form validation.

---

## Model Managers

```python
class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Product(models.Model):
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active = ActiveManager()
```

Custom managers control default query behavior.

---

## Migrations & Database Sync

```bash
python manage.py makemigrations
python manage.py migrate
```

- Tracks schema changes  
- Auto-generates SQL  
- Safely updates the database  

---

## Key Interview Points

- Model = table, instance = row  
- ORM abstracts SQL  
- Relationships handled automatically  
- Migrations manage schema safely  
- Business logic can live in models  