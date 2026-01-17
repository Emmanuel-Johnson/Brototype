# Django ORM

## 1. WHAT
ORM is a layer used to interact with the database using Python objects instead of writing raw SQL. In Django, ORM maps tables to models and rows to class instances.

## 2. WHY
It removes the need to repeatedly write SQL for common operations like CRUD. Without ORM, developers must handle queries, data mapping, and database differences manually, which is error-prone and slow.

## 3. WHERE
Django ORM sits between the Django application logic and the database. During the request–response cycle, views use ORM to fetch or update data before sending a response.

## 4. HOW
First, you define models that represent database tables. Django converts ORM queries into SQL automatically. The database executes the SQL and Django returns Python objects.

## 5. WHEN
Use ORM for most application-level database operations and rapid development. Avoid it for highly complex or performance-critical queries where optimized raw SQL is needed.

## 6. EXAMPLE
In an e-commerce project,  
`Product.objects.filter(stock__gt=0)`  
is used to fetch available products without writing a SQL `SELECT` query.

## 7. PROS & CONS
ORM improves productivity, readability, and database portability. However, it can hide inefficient queries and may be slower than hand-written SQL for complex cases.

## 8. COMMON MISTAKES
Using ORM in loops causing N+1 queries, and assuming ORM queries are always optimized without checking the generated SQL.

<br>
<br>
<br>

## WHAT

ORM is a technique that lets you interact with a relational database using Python objects instead of writing raw SQL queries. Django ORM maps Python classes to database tables.

## WHY

Without ORM, you must write database-specific SQL repeatedly, which is error-prone and hard to maintain. ORM removes SQL boilerplate and makes database operations safer and faster to write.

## WHERE

ORM sits between Django models and the database engine (PostgreSQL, MySQL, SQLite). Django translates ORM queries into SQL and executes them on the database.

## HOW

Each Django model class becomes a database table, and each model field becomes a column. When you use ORM methods like `create()`, `filter()`, or `update()`, Django converts them into SQL queries automatically.

## Simple Example

```python
class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

User.objects.create(name="Alex", age=25)
User.objects.filter(age__gte=18)
```

Django generates and runs the required SQL behind the scenes.

## Key Benefits (Quick Recall for Interviews)

* Database-agnostic
* Prevents SQL injection
* Cleaner, readable code
* Tight integration with models and migrations
