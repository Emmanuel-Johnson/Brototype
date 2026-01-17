## WHAT

`exclude()` is a QuerySet method used to retrieve objects that do not match the given conditions.

## WHY

It helps filter out unwanted records while still working safely with multiple results, without raising exceptions.

## WHERE

`exclude()` is called on a model manager or an existing QuerySet, such as `Model.objects.exclude()`.

## HOW

Django builds a QuerySet that negates the given condition and executes the SQL query only when the QuerySet is evaluated (lazy evaluation).

## Example

```python
users = User.objects.exclude(is_active=False)
```

## Important Behavior (Interview Points)

* **Returns**: a QuerySet
* **No exception** if no records are found
* **Chainable** with other QuerySet methods

```python
User.objects.filter(age__gte=18).exclude(is_staff=True)
```

## exclude() vs filter()

* `filter()` → includes matching records
* `exclude()` → excludes matching records

---

## Interview One-Liner

> "`exclude()` retrieves all objects except those that match the given condition and always returns a QuerySet."
