`bulk_update()` is a Django ORM method used to update multiple model instances in the database in a **single query**.

## What it does

It takes a list (or queryset) of **already existing model objects** and updates specific fields for all of them at once.

## Basic example

```python
books = Book.objects.filter(pages__gt=400)

for book in books:
    book.price += 100
    book.pages -= 20

Book.objects.bulk_update(books, ['price', 'pages'])
```

This updates the `price` field for all books in **one database query**.

## Why it’s used

If you do:

```python
for book in books:
    book.price = 500
    book.save()
```

Django performs **N UPDATE queries**.

Using `bulk_update()` performs **one bulk UPDATE**, which is much faster.

## Important rules

* Objects **must already exist** in the database (must have `id`)
* You must **explicitly list fields** to update
* `.save()` is **NOT called**
* Signals are **NOT triggered**
* No model validation is performed

## `bulk_update()` vs `update()`

| bulk_update()            | update()                |
| ------------------------ | ----------------------- |
| Works on model instances | Works on QuerySets      |
| Different values per row | Same value for all rows |
| Field list required      | No field list needed    |
| Slightly slower          | Fastest                 |

## When to use

Use `bulk_update()` when:

* Each row needs a **different value**
* You already have objects in memory
* You want bulk speed with per-object values

## Interview one-liner

Use `update()` when setting the **same value** for many rows.

Use `bulk_update()` when setting **different values** for many rows.
