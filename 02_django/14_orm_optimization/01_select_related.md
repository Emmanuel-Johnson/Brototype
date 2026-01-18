## 1. WHAT
`select_related` is a Django ORM optimization method used to fetch related objects in the same database query using SQL JOINs.

## 2. WHY
Without `select_related`, accessing foreign key data causes multiple extra queries (the N+1 query problem). This makes code slower and repetitive when looping over related objects.

## 3. WHERE
It is used at the QuerySet level, typically in the view or service layer, before data is passed to serializers, templates, or APIs in the request–response cycle.

## 4. HOW
First, you specify the foreign key fields in `select_related()`. Django then creates a single SQL query with JOINs, and related objects are populated automatically when accessed.

## 5. WHEN
Use it when working with `ForeignKey` or `OneToOneField` relationships and you know related data will be accessed. Do not use it for `ManyToManyField` or large unused relations.

## 6. EXAMPLE
In an e-commerce app, fetching `Order` objects along with their `User` details using  
`Order.objects.select_related('user')` avoids extra queries when showing order lists.

## 7. PROS & CONS
It reduces database queries and improves performance significantly while keeping code clean and efficient. However, it can increase query size and should not be overused unnecessarily.

## 8. COMMON MISTAKES
Using `select_related` with `ManyToManyField` relationships is incorrect. Another mistake is using it when related fields are not actually accessed, which wastes resources.

<br>
<br>
<br>

# Django `select_related()`

`select_related()` is a Django ORM performance tool.\
Simple idea: it reduces database queries by using SQL JOINs.

------------------------------------------------------------------------

## What it does

`select_related()` fetches related objects in the same database query
instead of hitting the database again for each object.

It works only for **ForeignKey** and **OneToOneField** relationships
(single-valued relations).

------------------------------------------------------------------------

## Without `select_related()` (Problem)

``` python
orders = Order.objects.all()

for order in orders:
    print(order.user.username)
```

### Queries

-   1 query → fetch orders\
-   N queries → fetch user for each order

This is the classic **N+1 problem**.

------------------------------------------------------------------------

## With `select_related()` (Solution)

``` python
orders = Order.objects.select_related('user')

for order in orders:
    print(order.user.username)
```

### Queries

-   ✅ 1 single query using JOIN

Django generates SQL similar to:

``` sql
SELECT order.*, user.*
FROM order
INNER JOIN user ON order.user_id = user.id;
```

------------------------------------------------------------------------

## When to use

Use `select_related()` when:

-   You access `ForeignKey` or `OneToOneField`
-   You are looping over a queryset
-   You want to avoid extra database hits

### Examples

``` python
Book.objects.select_related('author')
Profile.objects.select_related('user')
Order.objects.select_related('user', 'product')
```

------------------------------------------------------------------------

## When NOT to use

❌ Do not use for `ManyToManyField` or reverse relations.\
Use `prefetch_related()` instead.

------------------------------------------------------------------------

## Interview one-liner

`select_related()` performs SQL joins and fetches related objects in a
single query to avoid N+1 problems.

<br>
<br>
<br>

# Django `select_related()` Example

## Models

``` python
class Publisher(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
```

------------------------------------------------------------------------

## Without `select_related()` (Problem)

``` python
books = Book.objects.all()

for book in books:
    print(book.title, book.publisher.name)
```

Here, Django runs **1 query for books** plus **1 query per book** to
fetch the publisher.

This results in the **N+1 query problem**.

------------------------------------------------------------------------

## With `select_related()` (Solution)

``` python
books = Book.objects.select_related('publisher')

for book in books:
    print(book.title, book.publisher.name)
```

------------------------------------------------------------------------

## What happens internally

Django uses a SQL `JOIN` and fetches both **Book** and **Publisher**
data in a single database query.

Because of this, accessing `book.publisher.name` does **not** hit the
database again.

------------------------------------------------------------------------

## When to use

Use `select_related()` only with **ForeignKey** or **OneToOne**
relationships, when you know you'll access fields from the related
object.