## WHAT

An `F` object represents the value of a model field and allows database operations using field-to-field comparisons.

## WHY

It lets calculations and comparisons happen at the database level, avoiding race conditions and extra queries.

## WHERE

`F` objects are used inside QuerySet methods such as `filter()`, `update()`, and `annotate()`.

## HOW

You import `F` from `django.db.models` and reference model fields directly instead of Python values.

## Example: Field Comparison

```python
from django.db.models import F

Product.objects.filter(stock__gt=F('sold'))
```

## Example: Atomic Update

```python
Product.objects.update(stock=F('stock') - 1)
```

This runs as a single SQL query, even with concurrent requests.

## Important Interview Points

* Works at the database level
* Prevents race conditions
* Useful for counters and increments
* No need to fetch objects into Python

## F Object vs Normal Update

* Normal update → fetch → modify → save
* `F` object → direct database operation

---

## Interview One-Liner

> "F objects allow field-based operations directly in the database, making updates safe and efficient."
