## WHAT

`get()` is a QuerySet method used to retrieve exactly one object from the database that matches the given condition.

## WHY

It is used when you are sure only one record should exist, such as fetching data by a primary key or a unique field.

## WHERE

`get()` is called on a model manager or a QuerySet, for example `Model.objects.get()`.

## HOW

Django executes a SQL query and expects a single result. If the result count is not exactly one, Django raises an exception.

## Example

```python
user = User.objects.get(id=1)
```

## Important Behavior (Very Important for Interviews)

* **Returns**: a single model instance
* **Raises `DoesNotExist`**: if no record is found
* **Raises `MultipleObjectsReturned`**: if more than one record is found

```python
User.objects.get(email="test@example.com")
```

## get() vs filter()

* `get()` → returns one object
* `filter()` → returns a QuerySet (zero or more objects)

---

## Interview One-Liner

> "`get()` is used when exactly one object is expected; otherwise, Django raises an exception."
