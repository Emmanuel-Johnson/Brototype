## 1️⃣ Model Relationships

-   **Author ↔ Book** → `ManyToMany`
-   **Publisher → Book** → `ForeignKey` (One-to-Many)
-   **Product → Variant** → `OneToMany` (ForeignKey)

------------------------------------------------------------------------

## 2️⃣ Models (`models.py`)

``` python
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
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Variant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='variants'
    )
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.name}"
```

------------------------------------------------------------------------

## 3️⃣ Sample Data to Practice

``` python
# authors
john = Author.objects.create(name="John")
sam = Author.objects.create(name="Sam")
alex = Author.objects.create(name="Alex")

# publishers
p1 = Publisher.objects.create(name="Penguin")
p2 = Publisher.objects.create(name="O'Reilly")

# books
b1 = Book.objects.create(title="Django Basics", pages=300, price=500, publisher=p1)
b2 = Book.objects.create(title="Advanced Django", pages=450, price=800, publisher=p2)
b3 = Book.objects.create(title="Python ORM", pages=250, price=400, publisher=p1)

b1.authors.add(john)
b2.authors.add(sam)
b3.authors.add(john, sam)

# products & variants
phone = Product.objects.create(name="Phone")
Variant.objects.create(product=phone, name="64GB", price=15000)
Variant.objects.create(product=phone, name="128GB", price=18000)
Variant.objects.create(product=phone, name="256GB", price=21000)
```

------------------------------------------------------------------------

## 4️⃣ Important ORM Queries

### ✅ Books written by **John OR Sam**

``` python
from django.db.models import Q

books = Book.objects.filter(
    Q(authors__name="John") | Q(authors__name="Sam")
).distinct()
```

------------------------------------------------------------------------

### ✅ Total pages written by **Sam**

``` python
from django.db.models import Sum

total_pages = Book.objects.filter(
    authors__name="Sam"
).aggregate(total_pages=Sum('pages'))
```

Result:

``` python
{'total_pages': 700}
```

------------------------------------------------------------------------

### ✅ Total number of books per author

``` python
from django.db.models import Count

authors = Author.objects.annotate(
    book_count=Count('books')
)
```

------------------------------------------------------------------------

### ✅ Highest priced variant per product

``` python
from django.db.models import Max

products = Product.objects.annotate(
    max_price=Max('variants__price')
)
```

------------------------------------------------------------------------

## 5️⃣ Joins Summary

-   FK Join → `book.publisher`
-   M2M Join → `book.authors`
-   Reverse FK → `publisher.books`
-   Reverse M2M → `author.books`

------------------------------------------------------------------------

## 6️⃣ Big Picture (Interview Gold)

-   **ForeignKey** → One-to-Many
-   **ManyToManyField** → Join table
-   **annotate()** → Per row calculation
-   **aggregate()** → Single result
-   **related_name** → Reverse access
-   **ORM joins happen at DB level**