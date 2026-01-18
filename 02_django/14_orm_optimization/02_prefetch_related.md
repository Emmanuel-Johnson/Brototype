## 1. WHAT
`prefetch_related` is a Django ORM optimization method used to fetch related objects in separate queries and join them in Python.

## 2. WHY
Without `prefetch_related`, accessing many-to-many or reverse foreign key relations causes repeated database hits inside loops. This leads to slow performance and inefficient query patterns.

## 3. WHERE
It is applied at the QuerySet level, usually in views or service logic, before sending data to templates, serializers, or APIs during request handling.

## 4. HOW
First, Django runs the main query for the base model. Then it runs additional queries for related models. Finally, it matches and caches related objects in memory.

## 5. WHEN
Use it for `ManyToManyField` and reverse `ForeignKey` relationships when related data is needed. Do not use it for simple foreign keys where `select_related` is better.

## 6. EXAMPLE
In a blog app, fetching `Post` objects with their `Comment` lists using  
`Post.objects.prefetch_related('comments')` avoids querying comments inside a loop.

## 7. PROS & CONS
It prevents N+1 queries and works well for complex relationships, improving readability and performance. However, it uses more memory and runs multiple queries.

## 8. COMMON MISTAKES
Using `prefetch_related` when related data is never accessed is wasteful. Another mistake is using it instead of `select_related` for foreign key relationships.

<br>
<br>
<br>

# Django `prefetch_related()`

`prefetch_related()` is a Django ORM optimization tool used to reduce
database queries for **multi-valued relationships**.

------------------------------------------------------------------------

## What it does

`prefetch_related()` fetches related objects using **separate queries**
and then joins them in **Python**.

It is used for: - `ManyToManyField` - Reverse `ForeignKey` relationships
(one-to-many)

------------------------------------------------------------------------

## Without `prefetch_related()` (Problem)

``` python
authors = Author.objects.all()

for author in authors:
    print(author.books.all())
```

### Queries

-   1 query → authors\
-   N queries → books per author

This results in the **N+1 problem**.

------------------------------------------------------------------------

## With `prefetch_related()` (Solution)

``` python
authors = Author.objects.prefetch_related('books')

for author in authors:
    print(author.books.all())
```

### Queries

-   ✅ 1 query → authors\
-   ✅ 1 query → all related books

Django maps books to authors **in memory**.

------------------------------------------------------------------------

## What happens internally

``` sql
SELECT * FROM author;
SELECT * FROM book WHERE author_id IN (1, 2, 3, ...);
```

No SQL `JOIN` is used --- Python performs the matching.

------------------------------------------------------------------------

## Key differences from `select_related()`

  Feature             select_related   prefetch_related
  ------------------- ---------------- ------------------
  Relationship type   FK, OneToOne     M2M, reverse FK
  SQL JOIN            Yes              No
  Number of queries   1                Usually 2
  Memory usage        Lower            Higher

------------------------------------------------------------------------

## Common examples

``` python
Author.objects.prefetch_related('books')
User.objects.prefetch_related('groups')
Post.objects.prefetch_related('comments')
```

------------------------------------------------------------------------

## Interview one-liner

`prefetch_related()` avoids N+1 queries for multi-valued relationships
by fetching related objects in separate queries and combining them in
Python.

<br>
<br>
<br>

# Django `prefetch_related()` --- Many-to-Many Example

## Models (Many-to-Many)

``` python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
```

------------------------------------------------------------------------

## Without `prefetch_related()` (Problem)

``` python
books = Book.objects.all()

for book in books:
    print(book.title)
    for author in book.authors.all():
        print(author.name)
```

This causes: - 1 query to fetch books - 1 additional query **per book**
to fetch authors

This is the classic **N+1 query problem**.

------------------------------------------------------------------------

## With `prefetch_related()` (Solution)

``` python
books = Book.objects.prefetch_related('authors')

for book in books:
    print(book.title)
    for author in book.authors.all():
        print(author.name)
```

------------------------------------------------------------------------

## What happens internally

Django executes **2 queries total**: - One query for `Book` - One query
for `Author`

The ORM then links books and authors **in Python memory**, so accessing
`book.authors.all()` does not trigger extra queries.

------------------------------------------------------------------------

## When to use

Use `prefetch_related()` for **ManyToMany** and **reverse ForeignKey**
relationships, where SQL `JOIN`s are inefficient or not possible.

<br>
<br>
<br>

# Django `prefetch_related()` – Clean Example Setup

This example shows a **simple, interview‑friendly model structure** that clearly demonstrates how `prefetch_related()` works with `ManyToMany`, `ForeignKey`, and nested relations.

---

## Models

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)

    authors = models.ManyToManyField(
        Author,
        related_name="books"
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name="books"
    )

    def __str__(self):
        return self.title
```

---

## How this connects to `prefetch_related()`

### 1. Prefetching a ManyToMany field

```python
Book.objects.prefetch_related('authors')
```

This prefetches all authors for the fetched books in **one extra query**, instead of hitting the database once per book.

---

### 2. Prefetching reverse ForeignKey (using `related_name`)

```python
Publisher.objects.prefetch_related('books')
```

Here, `books` comes from the `related_name` on `Book.publisher`. Django fetches all books for all publishers efficiently.

---

### 3. Nested prefetch (reverse FK → M2M)

```python
Publisher.objects.prefetch_related('books__authors')
```

This first prefetches all books for publishers, then prefetches all authors for those books, avoiding the N+1 query problem at both levels.

---

## Interview Tip

* Use `select_related()` for **single‑valued relations** (`ForeignKey`, `OneToOne`).
* Use `prefetch_related()` for **multi‑valued relations** (`ManyToMany`, reverse `ForeignKey`).
* Nested prefetch works only with `prefetch_related()`.

This model setup is ideal for explaining `prefetch_related()` clearly in interviews.
