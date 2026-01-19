## 1. WHAT
`ForeignKey` is a Django model field used to create a **one-to-many relationship** between two database tables.  
It links one record in a model to a single record in another model.

---

## 2. WHY
It solves the problem of **data duplication** and **manual joins** when related data is stored separately.  
Without it, managing relationships like *“many books belong to one author”* becomes repetitive and error-prone.

---

## 3. WHERE
It exists in the **model layer** of Django’s MVT architecture and maps directly to a **foreign key constraint** in the database.  
During a request, Django ORM uses it to fetch and join related data efficiently.

---

## 4. HOW
1. Define a `ForeignKey` in a model pointing to another model.  
2. Django creates a foreign key column in the database.  
3. The ORM allows access to related objects using simple attribute access.

---

## 5. WHEN
Use it when **one object logically belongs to another**, such as:
- Orders → Customer  
- Books → Author  

Do **not** use it for many-to-many relationships; use `ManyToManyField` instead.

---

## 6. EXAMPLE
In an e-commerce project, a `Product` model can have a `ForeignKey` to a `Category` model so multiple products belong to one category.

---

## 7. PROS & CONS

### Pros
- Enforces relational integrity  
- Simplifies queries across related models  
- Reduces data duplication  

### Cons
- Improper use can cause extra database queries  
- Deleting related data must be handled carefully  

---

## 8. COMMON MISTAKES
- Forgetting to define `on_delete` behavior  
- Using `ForeignKey` where a many-to-many relationship is required  

<br>
<br>
<br>

## What is a ForeignKey?

A **ForeignKey** is used to create a **many-to-one relationship** between two models.

👉 Many objects in one model can be related to **one object** in another model.

---

## Real-life Examples

- Many **Books** belong to one **Publisher**
- Many **Orders** belong to one **Customer**

---

## Basic Syntax

```python
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
```

---

## What This Means

- **Book** → child table  
- **Publisher** → parent table  
- Each **Book** has **one Publisher**  
- One **Publisher** can have **many Books**

---

## `on_delete` (Very Important)

Defines what happens to child records when the parent is deleted.

### Common Options

```python
models.CASCADE      # delete related objects
models.PROTECT      # prevent deletion
models.SET_NULL     # set FK to NULL (null=True required)
models.SET_DEFAULT  # set to default value
models.DO_NOTHING   # database handles it
```

### Example: SET_NULL

```python
publisher = models.ForeignKey(
    Publisher,
    on_delete=models.SET_NULL,
    null=True
)
```

---

## Accessing Data (Both Directions)

### From Child → Parent

```python
book = Book.objects.get(id=1)
print(book.publisher.name)
```

---

### From Parent → Child (Reverse Relation)

Django automatically creates a reverse manager.

```python
publisher = Publisher.objects.get(id=1)
publisher.book_set.all()
```

---

## Custom Reverse Name (`related_name`)

```python
publisher = models.ForeignKey(
    Publisher,
    on_delete=models.CASCADE,
    related_name="books"
)
```

Now you can use:

```python
publisher.books.all()
```

---

## ForeignKey in Queries

### Filter Books by Publisher

```python
Book.objects.filter(publisher=publisher)
```

or

```python
Book.objects.filter(publisher__name="O'Reilly")
```

---

## Using `select_related()` with ForeignKey

Since **ForeignKey is many-to-one**, use `select_related()` for better performance.

```python
books = Book.objects.select_related("publisher")

for book in books:
    print(book.title, book.publisher.name)
```

➡ Avoids the **N+1 query problem**.

---

## Database-Level View

Behind the scenes:

- Django creates a column **`publisher_id`** in the `Book` table
- Stores the **primary key** of the `Publisher`

---

## When to Use ForeignKey

Use **ForeignKey** when:

- One object belongs to **exactly one** other object

### Examples

- `product → category`
- `order → customer`
- `comment → post`