## What is `related_name`?

`related_name` defines the **name used to access the reverse relationship** from the related model.

👉 It tells Django:  
**“From the other side, what should I call this relationship?”**

---

## Without `related_name` (Default Behavior)

### Example: ForeignKey

```python
class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE
    )
```

### Accessing Reverse Relation

```python
publisher = Publisher.objects.get(id=1)
publisher.book_set.all()
```

- `book_set` is **auto-generated** by Django
- Works, but not very readable

---

## With `related_name`

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name="books"
    )
```

### Now Access Using

```python
publisher.books.all()
```

✅ Much cleaner and more readable.

---

## Works With All Relationship Fields

`related_name` can be used with:

- `ForeignKey`
- `OneToOneField`
- `ManyToManyField`

---

## OneToOneField Example

```python
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
```

### Access

```python
user.profile
```

(No `.all()` because it’s one-to-one)

---

## ManyToManyField Example

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(
        Author,
        related_name="books"
    )
```

### Access

```python
author.books.all()
```

---

## Why `related_name` Is Important

### 1. Readability

```python
publisher.books.all()     # clear
publisher.book_set.all()  # ugly
```

---

### 2. Avoid Reverse Name Clashes

If multiple fields point to the **same model**:

```python
class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    delivery_person = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="deliveries"
    )
```

Without `related_name`, Django throws an **error**.

---

## Disable Reverse Relation

Use:

```python
related_name="+"
```

### Example

```python
user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="+"
)
```

Now:

- ❌ No reverse access from `User`

---

## `related_query_name`

Used for **reverse filtering in queries**.

```python
publisher = models.ForeignKey(
    Publisher,
    on_delete=models.CASCADE,
    related_name="books",
    related_query_name="book"
)
```

### Query Example

```python
Publisher.objects.filter(book__title__icontains="django")
```

---

## Best Practices

- Use **plural names** for `ForeignKey` & `ManyToManyField`
- Use **singular names** for `OneToOneField`
- Always set `related_name` in **reusable apps**
- Keep names **short, clear, and meaningful**

---

## Quick Summary

- `related_name` = reverse relationship name
- Avoids `*_set`
- Prevents conflicts
- Improves readability
- Works with **FK, O2O, and M2M**