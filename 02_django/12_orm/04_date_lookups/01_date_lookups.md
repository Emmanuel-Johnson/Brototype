## WHAT

Date lookups are field lookups used to filter records based on specific parts of date or datetime fields.

## WHY

They make it easy to query data by year, month, day, or weekday without writing raw SQL.

## WHERE

Date lookups are used with `DateField` and `DateTimeField` inside Django QuerySets.

## HOW

Django extracts date components at the database level and applies them in filters.

---

## Common Date Lookups

### year

Filters records from a specific year.

```python
Order.objects.filter(created_at__year=2025)
```

### month

Filters records from a specific month (1–12).

```python
Order.objects.filter(created_at__month=1)
```

### day

Filters records from a specific day of the month.

```python
Order.objects.filter(created_at__day=15)
```

### weekday

Filters records by day of the week.

* 1 = Sunday
* 7 = Saturday

```python
Order.objects.filter(created_at__weekday=1)
```

---

## Important Interview Points

* Works with `DateField` and `DateTimeField`
* Executes at the database level
* Database-agnostic
* Uses SQL date extraction functions internally

---

## Interview One-Liner

> "Date lookups allow filtering records by specific date parts like year, month, day, and weekday in Django ORM."
