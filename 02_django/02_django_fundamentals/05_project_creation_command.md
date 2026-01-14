## 🏗️ Project Creation Command

```bash
django-admin startproject project_name
```

### Example:
```bash
django-admin startproject mysite
```

### 📁 This creates:

```
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

## 📦 App Creation Command

👉 Run this **inside the project folder** (where `manage.py` exists):

```bash
python manage.py startapp app_name
```

### Example:
```bash
python manage.py startapp users
```

### 📁 This creates:

```
users/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

## ⚠️ Important Next Step (Don’t Forget!)

After creating an app, register it in `settings.py`:

```python
INSTALLED_APPS = [
    'users',
]
```

---

## 🎯 Interview One-Liner

> **“`startproject` creates the Django project structure, and `startapp` creates a modular application inside the project.”**