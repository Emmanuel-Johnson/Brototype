`delete()` is a Django ORM method used to remove model instances from the database.

It can be called on a **single object** or on a **QuerySet**.

## Basic examples

### Deleting a single object

```python
book = Book.objects.get(id=1)
book.delete()
```

### Deleting multiple objects (QuerySet)

```python
Book.objects.filter(price__lt=100).delete()
```

When called on a QuerySet, Django executes a **bulk SQL DELETE**.

## Key points

* Runs `pre_delete` and `post_delete` signals
* Respects `on_delete` behavior (`CASCADE`, `SET_NULL`, etc.)
* Returns `(count, details)` of deleted objects
* Does **not** call `.save()`

## Bulk delete in Django

Django does **not** have a separate `bulk_delete()` method.

👉 **Bulk delete** simply means calling `delete()` on a QuerySet.

```python
Book.objects.filter(is_outdated=True).delete()
```

This deletes all matching rows in **one operation**, making it the bulk delete.

## `delete()` vs bulk delete (conceptual)

| Aspect    | Single delete() | Bulk delete     |
| --------- | --------------- | --------------- |
| Called on | Model instance  | QuerySet        |
| Queries   | 1               | 1 (main delete) |
| Signals   | Yes             | Yes             |
| Use case  | One object      | Many objects    |

## Interview clarity line

Django does **not** provide a separate `bulk_delete()` method.

Calling `delete()` on a **QuerySet** is the bulk delete.
