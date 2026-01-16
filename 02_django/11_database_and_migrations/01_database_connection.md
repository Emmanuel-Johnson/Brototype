# Database Connection

## What is a Database Connection?

A **database connection** is the link between a backend application and the database that allows the app to read, write, update, and delete data.  
In Django, database connections are handled automatically by **Django’s ORM**.

---

## Database Connection in Django

Django connects to the database using the configuration defined in `settings.py`.

### Example (PostgreSQL)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## How Django Manages Connections

- Django opens a database connection **only when needed**
- The same connection is reused during the request
- At the end of the request, Django closes or reuses the connection
- Connection pooling is handled by the **database** or external tools

Developers usually **do not open or close connections manually**.

---

## Request–Database Flow

```
Request → View → ORM → Database
                   ↓
               Connection
```

---

## Example Using ORM

```python
from .models import Product
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return HttpResponse(products)
```

Django automatically uses the database connection when ORM queries are executed.

---

## Database Connection Types in Django

- **SQLite** → file-based, auto-managed (used in development)
- **PostgreSQL / MySQL** → TCP-based connections
- Production applications commonly use **PostgreSQL**

---

## Common Interview Points

- Django manages database connections automatically
- Configuration is done in `DATABASES`
- ORM abstracts raw SQL queries
- Connections are handled per request
- Database schema is managed using **migrations**