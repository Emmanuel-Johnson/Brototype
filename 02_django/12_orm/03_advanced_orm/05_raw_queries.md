# Raw Queries

## WHAT

Raw queries allow you to execute raw SQL directly in Django when ORM queries are not sufficient.

## WHY

They are used for complex queries, performance optimization, or database-specific features that are hard or impossible to express using the ORM.

## WHERE

Raw queries are executed through Django models or database cursors and bypass parts of the ORM abstraction.

## HOW

Django provides two main ways to run raw SQL.

<br>
<br>
<br>

# raw()

## WHAT

`raw()` is a method used to execute raw SQL queries while still mapping the results to Django model instances.

## WHY

It is useful when a query is too complex for ORM but you still want Django to return model objects instead of plain tuples.

## WHERE

`raw()` is called on a model manager, such as `Model.objects.raw()`.

## HOW

You pass a raw SQL query to `raw()`, and Django maps the result columns to model fields.

## Example

```python
users = User.objects.raw(
    "SELECT * FROM auth_user WHERE is_active = %s",
    [True]
)
```

## Important Interview Points

* Returns a `RawQuerySet`
* Results are model instances
* Query must include the model’s primary key
* Mostly read-only
* Use parameters to prevent SQL injection

## raw() vs cursor()

* `raw()` → model instances, safer, read-only
* `cursor()` → tuples, full control, manual handling

---

## Interview One-Liner

> "`raw()` executes raw SQL and maps the result to Django model instances, bridging raw SQL and ORM."

<br>
<br>
<br>

# Cursor

## WHAT

A cursor is a database object used to execute raw SQL queries and fetch results directly from the database.

## WHY

It is used when you need full control over SQL execution, which is not easily achievable using Django ORM or `raw()` queries.

## WHERE

Django provides cursor access through `django.db.connection`, which connects Django to the database engine.

## HOW

You obtain a cursor using `connection.cursor()` and execute SQL commands manually.

## Example

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()
```

## Important Interview Points

* Executes raw SQL
* Bypasses Django ORM
* Results are tuples, not model instances
* Developer must handle SQL safety and portability

## Cursor vs ORM (Quick Comparison)

* ORM → safer, readable, database-agnostic
* Cursor → full SQL control, less safe, database-specific

---

## Interview One-Liner

> "A cursor provides low-level access to execute raw SQL queries directly against the database in Django."

<br>
<br>
<br>

# raw() vs cursor()

## WHAT

`raw()` executes raw SQL and maps results to Django model instances, while `cursor()` provides low-level database access to execute SQL and return raw results.

## WHERE

* `raw()` is used through a model manager: `Model.objects.raw()`
* `cursor()` is accessed via `django.db.connection`

---

## Key Differences

### Result Type

* `raw()` → returns model instances
* `cursor()` → returns tuples (or dictionaries if handled manually)

### Use Case

* `raw()` → when ORM is insufficient but model mapping is still desired
* `cursor()` → when full SQL control is required

### Read / Write

* `raw()` → mostly read-only
* `cursor()` → supports full read and write operations

### Safety

* `raw()` → supports parameterized queries and is safer by default
* `cursor()` → requires manual handling to avoid SQL injection

### Complexity

* `raw()` → simpler and cleaner
* `cursor()` → more complex and error-prone

### Database Portability

* `raw()` → relatively portable
* `cursor()` → database-specific

---

## Examples (Quick Recall)

```python
User.objects.raw(
    "SELECT * FROM auth_user WHERE is_active = %s",
    [True]
)
```

```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
```

---

## Interview One-Liner

> "Use `raw()` when you need raw SQL with model mapping; use `cursor()` when you need complete control over SQL execution."
