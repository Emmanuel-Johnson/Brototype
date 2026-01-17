## WHAT

`values_list()` is a QuerySet method that returns database records as tuples instead of model instances.

## WHY

It is used when you need specific fields in a lightweight format, especially for iteration or membership checks.

## WHERE

`values_list()` is called on a model manager or a QuerySet, such as `Model.objects.values_list()`.

## HOW

Django generates a SQL query that selects only the specified columns and returns each row as a tuple.

## Example

```python
users = User.objects.values_list('id', 'username')
```

**Output:**

```python
[(1, 'alex'), (2, 'sam')]
```

## flat=True

When retrieving only one field, `flat=True` returns a flat list instead of tuples.

```python
usernames = User.objects.values_list('username', flat=True)
```

**Output:**

```python
['alex', 'sam']
```

## Important Behavior (Interview Points)

* **Returns**: QuerySet of tuples (or flat list)
* **Does NOT return** model instances
* **More memory efficient** than full model objects
* **Lazy evaluation** still applies

## values() vs values_list()

* `values()` → dictionaries
* `values_list()` → tuples / flat list

---

## Interview One-Liner

> "`values_list()` returns a QuerySet of tuples (or a flat list) containing selected fields instead of model instances."
