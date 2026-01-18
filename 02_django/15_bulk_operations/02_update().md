`update()` is a Django ORM method used to modify one or more database rows **directly** in a single SQL query.

## What it does

`update()` runs an SQL **UPDATE** on the database without loading model instances into Python memory.

## Basic example

```python
Book.objects.filter(published=False).update(published=True)
```

This updates **all matching rows at once**.

## Why it’s used

If you update objects like this:

```python
for book in books:
    book.published = True
    book.save()
```

Django executes **N UPDATE queries**.

Using `update()` does the same work in **one query**, which is much faster.

## Key characteristics

* Executes a **single SQL UPDATE**
* Does **not** call `.save()`
* Does **not** trigger signals
* Works only on **QuerySets**, not single objects
* Returns the **number of rows updated**

```python
count = Book.objects.filter(price__lt=500).update(price=500)
```

## What you cannot do

* Cannot update `ManyToManyField`
* Cannot run model validation
* Cannot apply Python logic per object

## `update()` vs `save()`

| update()      | save()              |
| ------------- | ------------------- |
| Bulk DB-level | Per-object          |
| Fast          | Slower              |
| No signals    | Signals run         |
| No validation | Validation possible |

## When to use

Use `update()` when you need **fast, mass updates** and don’t need business logic, signals, or per-object hooks.

## Example: Increase Book Price Using F()

`F()` expressions in Django allow you to reference **model fields directly at the database level**. This is useful when you want to update a field based on its **current value**, without first fetching objects into Python.

### Code Example

```python
from django.db.models import F

Book.objects.filter(pages__gt=300).update(
    price=F('price') + 50
)
