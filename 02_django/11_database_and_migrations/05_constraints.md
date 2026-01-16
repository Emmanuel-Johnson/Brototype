# Constraints

## What are Constraints?

**Constraints** are rules applied at the **database level** to ensure data integrity, accuracy, and consistency.  
They prevent invalid data from being inserted or updated in a table.

---

## Common Types of Constraints

### 1. NOT NULL

Ensures a column cannot have `NULL` values.

```python
name = models.CharField(max_length=100, null=False)
```

---

### 2. UNIQUE

Ensures all values in a column (or combination of columns) are unique.

```python
email = models.EmailField(unique=True)
```

---

### 3. PRIMARY KEY

Uniquely identifies each row in a table.

```python
id = models.BigAutoField(primary_key=True)
```

---

### 4. FOREIGN KEY

Ensures **referential integrity** between tables.

```python
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

---

### 5. CHECK

Ensures values satisfy a specific condition.

```python
from django.db.models import Q, CheckConstraint

class Product(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(price__gte=0),
                name='price_non_negative'
            )
        ]
```

---

### 6. DEFAULT

Provides a default value if none is supplied.

```python
status = models.CharField(max_length=20, default='active')
```

---

## Constraints in Django (`Meta.constraints`)

```python
from django.db.models import UniqueConstraint

class Order(models.Model):
    order_id = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['order_id', 'user'],
                name='unique_order_per_user'
            )
        ]
```

---

## Model-Level vs Database-Level

- **Model validation** → Python-side checks  
- **Constraints** → enforced by the database  

Constraints protect data even when using **raw SQL** or accessing the DB outside Django.

---

## Key Interview Points

- Constraints enforce **data integrity**
- Applied at the **database level**
- Prevent invalid inserts and updates
- Django supports constraints via `Meta`
- Constraints are safer than relying only on model validation