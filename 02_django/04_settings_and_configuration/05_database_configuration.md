## 🗄️ What Is Database Configuration?

In Django, database configuration is done using the **`DATABASES`** setting in `settings.py`.

It tells Django **where your data lives** and **how to talk to it**.

---

## 🎯 Purpose

Database configuration allows Django to:

- Store models as database tables  
- Read and write application data  
- Run migrations  
- Power authentication, sessions, admin, etc.

👉 **Without a database, Django is basically read-only.**

---

## 🧱 Default Configuration (SQLite)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Why SQLite by Default?
- Zero setup  
- File-based  
- Perfect for learning & development  

⚠️ **Not recommended for production**.

---

## 🛢️ Common Database Engines

| Database | ENGINE Value |
|--------|--------------|
| SQLite | django.db.backends.sqlite3 |
| PostgreSQL ✅ | django.db.backends.postgresql |
| MySQL | django.db.backends.mysql |
| Oracle | django.db.backends.oracle |

👉 **PostgreSQL is the most popular production choice.**

---

## 🐘 PostgreSQL Example (Production-Style)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

📦 Required package:
```bash
pip install psycopg2-binary
```

---

## 🔐 Using Environment Variables (Best Practice)

❌ Never hardcode credentials.

```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
```

✅ Safer  
✅ Production-ready  
✅ Works with Docker & cloud platforms  

---

## 🔄 How Django Uses the Database

1️⃣ You define models  
2️⃣ Django creates migrations  
3️⃣ `migrate` creates tables  
4️⃣ ORM handles queries  
5️⃣ Database stores actual data  

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ⚠️ Security Implications

- ❌ Exposed DB credentials → data breach  
- ❌ Weak DB passwords → full access  
- ❌ Public DB ports → attacks  
- ❌ Same DB for dev & prod → risky  

👉 **Treat your database like the heart of your app.**

---
