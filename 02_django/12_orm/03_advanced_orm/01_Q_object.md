## WHAT

A `Q` object is used to build complex database queries using logical conditions like AND, OR, and NOT.

## WHY

Normal `filter()` arguments only support AND logic. `Q` objects allow OR conditions and more flexible query combinations.

## WHERE

`Q` objects are used inside QuerySet methods such as `filter()`, `exclude()`, and `get()`.

## HOW

You import `Q` from `django.db.models` and combine conditions using bitwise operators.

## Example: OR Condition

```python
from django.db.models import Q

User.objects.filter(
    Q(is_staff=True) | Q(is_superuser=True)
)
```

## Example: AND Condition

```python
User.objects.filter(
    Q(is_active=True) & Q(age__gte=18)
)
```

## Example: NOT Condition

```python
User.objects.filter(
    ~Q(is_active=True)
)
```

## Important Interview Points

* `|` → OR
* `&` → AND
* `~` → NOT
* Improves readability for complex queries
* Converted to SQL by Django ORM

---

## Interview One-Liner

> "Q objects allow complex query logic using AND, OR, and NOT conditions in Django ORM."
