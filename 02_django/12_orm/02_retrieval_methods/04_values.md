## WHAT

`values()` is a QuerySet method that returns database records as dictionaries instead of model instances.

## WHY

It is used when you only need specific fields and want lighter, faster queries without creating full model objects.

## WHERE

`values()` is called on a model manager or a QuerySet, such as `Model.objects.values()`.

## HOW

Django generates a SQL query that selects only the specified columns and returns each row as a dictionary.

## Example

```python
users = User.objects.values('id', 'username', 'email')
```

**Output:**

```python
[
  {'id': 1, 'username': 'alex', 'email': 'a@example.com'},
  {'id': 2, 'username': 'sam', 'email': 's@example.com'}
]
```

## Important Behavior (Interview Points)

* **Returns**: a QuerySet of dictionaries
* **Does NOT return** model instances
* **Improves performance** by fetching only required fields
* **Lazy evaluation** still applies

## values() vs Normal QuerySet

* Normal QuerySet → returns model objects
* `values()` → returns dictionaries

---

## Interview One-Liner

> "`values()` returns a QuerySet of dictionaries containing only the requested fields, not model objects."
