## 1️⃣ Django Project Structure

A **project** is the entire website (settings, configuration, URLs, apps).

After running:

```bash
django-admin startproject myproject
```

You’ll usually see:

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

---

## 📄 What Each File Means

### manage.py
- Command-line utility  
- Used to run server, migrations, create apps, etc.

Examples:
```bash
python manage.py runserver
python manage.py makemigrations
```

---

### 📁 myproject/ (Inner Folder)
This is the **project configuration package**.

---

### __init__.py
- Tells Python this folder is a package  
- Usually empty  

---

### settings.py
Global configuration of your project:

- Installed apps  
- Database settings  
- Middleware  
- Templates  
- Static & media files  

👉 Think of this as the **project brain / settings panel**.

---

### urls.py
Main URL router.

- Connects URLs to apps or views  

Example:
```python
path('users/', include('users.urls'))
```

---

### wsgi.py
- Used in production  
- Connects Django to servers like **Gunicorn**  

---

### asgi.py
- Used for async features  
- WebSockets, real-time apps  

---

## 2️⃣ Django App Structure

An **app** is a feature/module inside the project  
(e.g., users, products, orders).

Created using:

```bash
python manage.py startapp myapp
```

Structure:

```
myapp/
├── migrations/
│   └── __init__.py
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

## 3️⃣ Explanation of Each App File

### 📁 migrations/
- Stores database migration files  
- Tracks changes to models  

👉 Django uses this to update database schema.

---

### __init__.py
- Marks folder as a Python package  

---

### models.py
Defines database tables.

- Each class = one table  

Example:
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
```

👉 This is your **database layer**.

---

### views.py
Contains business logic.

- Handles requests and returns responses  

Example:
```python
def home(request):
    return HttpResponse("Hello")
```

👉 This is where requests are processed.

---

### urls.py (You Add This Manually)
Maps URLs to views.

Example:
```python
path('', views.home)
```

👉 Acts like a **traffic controller**.

---

### admin.py
Registers models for Django Admin panel.

Example:
```python
admin.site.register(Product)
```

👉 Lets you manage data visually at `/admin`.

---

### apps.py
App configuration file.

- App name & metadata  

Example:
```python
class MyAppConfig(AppConfig):
    name = 'myapp'
```

👉 Used when adding the app to `INSTALLED_APPS`.

---

### tests.py
Used to write unit tests for your app.

Example:
```python
class ProductTest(TestCase):
    ...
```

👉 Helps ensure your app works correctly.