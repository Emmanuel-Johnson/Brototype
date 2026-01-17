## WHAT

A QuerySet is a Django object that represents a database query used to retrieve model data. It is lazy, meaning the query is executed only when the data is actually needed.

## WHY

QuerySets allow you to read, filter, and manipulate database data using Python code instead of raw SQL. They make querying consistent, safe, and reusable.

## WHERE

QuerySets are created and used through Django model managers (`objects`) and sit between Django models and the database.

## HOW

When you call ORM methods like `all()`, `filter()`, or `exclude()`, Django builds a QuerySet. The actual SQL query is executed only when the data is needed (lazy evaluation).

## Common QuerySet Examples

```python
User.objects.all()
User.objects.filter(age__gte=18)
User.objects.exclude(is_active=False)
User.objects.get(id=1)
```

## Important QuerySet Concepts (Very Important for Interviews)

### Lazy Evaluation

A QuerySet does not hit the database until it is evaluated (iteration, printing, converting to list, etc.).

### Chainable

Multiple filters can be chained, and Django combines them into a single SQL query.

```python
User.objects.filter(age__gte=18).filter(is_active=True)
```

### Immutable

Each QuerySet returns a new QuerySet; the original QuerySet is not modified.

## When a QuerySet Hits the Database

* Iterating over it
* Converting it to a list
* Calling `len()`
* Using `exists()`, `first()`, or `last()`

---

## Interview One-Liner

> "A QuerySet is a lazy, chainable, and immutable representation of a database query in Django ORM."
