`bulk_create()` is a Django ORM method used to insert multiple objects into the database in a **single query**.

## What it does

Instead of calling `.save()` repeatedly inside a loop, `bulk_create()` sends **one SQL INSERT** for many rows at once. This makes it much faster when creating large datasets.

## Basic example

```python
books = [
    Book(title="Django Basics", price=300, pages=200),
    Book(title="Advanced Django", price=500, pages=350),
    Book(title="ORM Deep Dive", price=450, pages=280),
    Book(title="REST with Django", price=400, pages=300),
    Book(title="Django Internals", price=550, pages=420),
]

Book.objects.bulk_create(books)
```

This creates all 3 books in **one database hit**.

## Why it’s used

Without `bulk_create()`:

```python
for book in books:
    book.save()
```

This runs **N queries**.

With `bulk_create()`:

* Only **1 query** is executed
* Huge performance improvement for large inserts

## Important rules / limitations

* `.save()` is **NOT called**
* `pre_save` and `post_save` signals **do NOT run**
* Auto fields like `id` may **not be available immediately** (depends on DB)
* Cannot be used for **ManyToMany** fields directly
* Validation (`full_clean`) is **not run automatically**

## With options

```python
Book.objects.bulk_create(books, batch_size=100)
```

Useful when inserting very large datasets to avoid database limits.

## When to use

Use `bulk_create()` for:

* Initial data loads
* Data imports / migrations
* Logs or analytics data
* Test data generation
* Any case where **speed matters more than signals or per-object logic**
