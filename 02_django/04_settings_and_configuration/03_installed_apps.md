## 📦 What Is INSTALLED_APPS?

In Django, **INSTALLED_APPS** is the registry of everything your project can use.

👉 If an app isn’t listed here, **Django pretends it doesn’t exist**.

---

## 🎯 Purpose

`INSTALLED_APPS` tells Django:

- Which apps are active  
- Where to look for:
  - Models (database tables)  
  - Admin registrations  
  - Templates  
  - Static files  
  - Signals  
  - Translations  
- Which migrations to apply  

In short:

> **“These are the features my project is built from.”**

---

## 🧱 Typical Structure

```python
INSTALLED_APPS = [
    # Django built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',

    # Your apps
    'accounts',
    'products',
    'orders',
]
```

---

## 🧩 Types of Apps

### 1️⃣ Django Built-in Apps (`django.contrib.*`)

These give Django its out-of-the-box power:

- `admin` → admin panel  
- `auth` → users, permissions  
- `sessions` → login sessions  
- `messages` → flash messages  
- `staticfiles` → CSS & JS handling  

👉 Remove one → **that feature stops working**.

---

### 2️⃣ Third-Party Apps

Installed via `pip`:

```bash
pip install djangorestframework
```

Enable it:

```python
INSTALLED_APPS += ['rest_framework']
```

Examples:
- `rest_framework` → APIs  
- `crispy_forms` → better forms  
- `django_filters` → filtering  

---

### 3️⃣ Your Custom Apps

Apps you create using:

```bash
python manage.py startapp blog
```

Then enable:

```python
INSTALLED_APPS += ['blog']
```

⚠️ If you forget this:

- Models won’t migrate  
- Admin won’t show  
- Signals won’t run  
- Templates may not load  

---

## 🔢 Order Matters (Sometimes)

App order can affect:

- Template overriding  
- Static file priority  
- Signal loading  

### Rule of Thumb:
```
Django built-in apps
→ Third-party apps
→ Your apps
```

👉 Your apps last = they can override others.

---

## ❌ Common Mistakes

- ❌ Creating an app but not adding it  
- ❌ Typos in app name  
- ❌ Adding the same app twice  
- ❌ Removing an app without handling migrations  
- ❌ Putting prod-only apps in dev settings  

---

## 🧠 Mental Model

> **INSTALLED_APPS is like a plugboard 🔌**  
> Only plugged-in modules get power. Others are ignored.