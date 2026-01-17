## WHAT

`contains` and `icontains` are field lookups used with `filter()` to check whether a field contains a given substring.

## WHY

They are used for search-like queries, such as finding users, products, or titles that include certain text.

## WHERE

They are applied to text-based fields like `CharField` and `TextField` inside Django QuerySets.

## HOW

Django translates these lookups into SQL `LIKE` queries.

## contains

Case-sensitive search (depends on database collation).

```python
User.objects.filter(username__contains="Alex")
```

Matches only if the case matches.

## icontains

Case-insensitive search.

```python
User.objects.filter(username__icontains="alex")
```

Matches `Alex`, `ALEX`, `alex`, etc.

## Important Interview Points

* Works with `filter()` and `exclude()`
* Uses SQL `LIKE %value%`
* `icontains` is preferred for user-facing search
* Performance can be slow on large tables without proper indexing

---

## Interview One-Liner

> "`contains` performs a case-sensitive substring search, while `icontains` performs a case-insensitive substring search in Django ORM."
