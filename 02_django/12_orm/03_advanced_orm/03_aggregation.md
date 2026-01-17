## WHAT

Aggregation is the process of performing calculations on a set of database records and returning a summarized result.

## WHY

It allows heavy calculations to be done at the database level, which is faster and more efficient than processing data in Python.

## WHERE

Aggregation is performed on Django QuerySets using the `aggregate()` method along with aggregate functions.

---

## aggregate() — Django ORM

### WHAT

`aggregate()` is a QuerySet method that returns summary values for the entire QuerySet.

### HOW

It executes a single SQL query and returns the result as a dictionary.

### Example

```python
from django.db.models import Avg

Product.objects.aggregate(avg_price=Avg('price'))
```

**Output:**

```python
{'avg_price': 450.0}
```

### Important Interview Points

* Returns a dictionary
* Always returns one result
* Does not return model instances
* Uses SQL aggregate functions internally

---

## Aggregate Functions — Django ORM

Common aggregate functions used with `aggregate()`:

* `Count()` → total number of records
* `Sum()` → sum of a numeric field
* `Avg()` → average value
* `Max()` → maximum value
* `Min()` → minimum value

### Example

```python
from django.db.models import Count, Sum

Order.objects.aggregate(
    total_orders=Count('id'),
    total_amount=Sum('amount')
)
```

---

## Interview One-Liner

> "Aggregation summarizes data at the database level using `aggregate()` and functions like Count, Sum, Avg, Max, and Min."
