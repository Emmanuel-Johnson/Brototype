## WHAT

Lazy evaluation means Django does not execute a database query immediately when a QuerySet is created. The query runs only when the data is actually needed.

## WHY

It avoids unnecessary database hits and improves performance by executing queries only when required.

## WHERE

Lazy evaluation applies to Django QuerySets, which sit between Django models and the database.

## HOW

When you call methods like `filter()` or `exclude()`, Django only builds the query. The actual SQL is executed only when the QuerySet is evaluated, such as during iteration or conversion to a list.

## Example

```python
qs = User.objects.filter(is_active=True)  # No DB hit
for user in qs:                          # DB hit happens here
    print(user.name)
```

## When Evaluation Happens

* Iteration (for loop)
* `list(qs)`
* `len(qs)`
* `exists()`, `first()`, `last()`

---

## Interview One-Liner

> "Django QuerySets are lazily evaluated, meaning SQL runs only when the data is actually accessed."
