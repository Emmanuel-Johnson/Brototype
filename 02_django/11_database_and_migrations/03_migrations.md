# Django Migrations

## 1. What Are Migrations?

**Migrations** in Django are a version-controlled way to manage **database schema changes**.  
They allow you to create, modify, and delete database tables and columns by tracking changes made in `models.py`, without writing raw SQL.

**In simple terms:** migrations keep your models and database in sync.

---

## 2. Migration Commands

### Create Migrations

```bash
python manage.py makemigrations
```

- Detects changes in `models.py`
- Creates migration files

---

### Apply Migrations

```bash
python manage.py migrate
```

- Applies migration files to the database

---

### View Migration Status

```bash
python manage.py showmigrations
```

- Shows which migrations are applied or pending

---

### Roll Back a Migration

```bash
python manage.py migrate app_name 0002
```

- Rolls back to a specific migration

---

### Create an Empty Migration

```bash
python manage.py makemigrations app_name --empty
```

- Used for custom or data migrations

---

## 3. How Migrations Work

1. You modify `models.py`  
2. Django compares models with existing migrations  
3. `makemigrations` creates a new migration file  
4. Migration files contain **Python operations**, not raw SQL  
5. `migrate` converts these operations into SQL  
6. Applied migrations are recorded in:

```
django_migrations
```

Each migration depends on the previous one and runs **in order**.

---

## 4. Adding a New Column via Migration

### Step 1: Update Model

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)  # new column
```

---

### Step 2: Create Migration

```bash
python manage.py makemigrations
```

Django generates something like:

```python
migrations.AddField(
    model_name='product',
    name='stock',
    field=models.IntegerField(default=0),
)
```

---

### Step 3: Apply Migration

```bash
python manage.py migrate
```

The new column is added **without data loss**.

---

## Key Interview Points

- Migrations are **version control for database schema**
- Stored as **Python files**
- Applied migrations are tracked in the database
- Safe way to update schema in production
- Avoid editing **already applied migrations** manually