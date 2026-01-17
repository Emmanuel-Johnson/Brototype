## WHAT

`filter()` is a QuerySet method used to retrieve multiple objects from the database that match given conditions.

## WHY

It is used when zero, one, or many records can exist, and you want a safe way to fetch matching data without raising exceptions.

## WHERE

`filter()` is called on a model manager or an existing QuerySet, such as `Model.objects.filter()`.

## HOW

Django builds a QuerySet based on the conditions provided and executes the SQL query only when the QuerySet is evaluated (lazy evaluation).

## Example

```python
users = User.objects.filter(is_active=True)
```

## Important Behavior (Interview Points)

* **Returns**: a QuerySet
* **No exception** if no records are found
* **Chainable** with other QuerySet methods

```python
User.objects.filter(age__gte=18).filter(is_staff=True)
```

## filter() vs get()

* `filter()` → returns zero or more objects (QuerySet)
* `get()` → returns exactly one object or raises an error

---

## Interview One-Liner

> "`filter()` safely retrieves multiple records and always returns a QuerySet, even if no data matches."
