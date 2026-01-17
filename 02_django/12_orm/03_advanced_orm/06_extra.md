## WHAT

`extra()` is a legacy QuerySet method that allows you to inject raw SQL fragments into ORM queries.

## WHY

It was used in older Django versions when certain SQL operations were not supported by the ORM.

## WHERE

`extra()` is called on a QuerySet, such as `Model.objects.extra()`.

## HOW

It lets you add custom SQL for `SELECT`, `WHERE`, `ORDER BY`, and `TABLES` clauses.

## Example

```python
User.objects.extra(
    where=["age > %s"],
    params=[18]
)
```

## Important Interview Points

* Deprecated / legacy feature
* Not recommended in modern Django
* Hard to maintain
* Risk of SQL injection
* Database-specific SQL

## Why extra() Is Discouraged

* Breaks ORM abstraction
* Poor readability
* Not future-proof
* Replaced by `annotate()`, `Q`, `F`, `Subquery`, and `RawSQL`

---

## Interview One-Liner

> "`extra()` is a legacy Django ORM method for injecting raw SQL and is now discouraged in favor of modern ORM features."
