## WHAT

Annotation is the process of adding calculated fields to each object in a QuerySet.

## WHY

It allows per-object calculations to be done at the database level, avoiding extra queries and Python-side loops.

## WHERE

Annotation is used on QuerySets with the `annotate()` method and aggregate functions.

---

## annotate() — Django ORM

### WHAT

`annotate()` adds one or more computed values to every object in the QuerySet.

### HOW

Django generates a SQL query with `GROUP BY` and attaches the calculated value as an attribute on each object.

### Example

```python
from django.db.models import Count

Author.objects.annotate(book_count=Count('books'))
```

Each `Author` object will have a `book_count` attribute.

### Important Interview Points

* Returns a QuerySet
* Adds calculated fields per object
* Uses aggregate functions internally
* Works well with related fields

---

## annotate() vs aggregate() (Quick Recall)

* `annotate()` → per-object calculation
* `aggregate()` → overall summary
* `annotate()` → returns a QuerySet
* `aggregate()` → returns a dictionary

---

## Interview One-Liner

> "`annotate()` adds calculated fields to each object in a QuerySet using database-level computations."
