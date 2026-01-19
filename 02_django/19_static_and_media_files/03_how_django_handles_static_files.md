# How Django Handles Static Files

## What Are Static Files?

Static files are files that **do not change at runtime**, such as:

- CSS  
- JavaScript  
- Images (logos, icons)  
- Fonts  

---

## 1️⃣ Static Files in Development (`DEBUG = True`)

### Folder Structure

Each app can have its own `static` folder:

```text
app/
 └── static/
     └── app/
         ├── style.css
         └── logo.png
```

---

### Settings Used

```python
STATIC_URL = "/static/"
```

(Optional)

```python
STATICFILES_DIRS = [BASE_DIR / "static"]
```

---

### What Django Does

- Django finds static files using **STATICFILES_FINDERS**
- Serves them **automatically**
- No web server needed

When you open:

```
/static/app/style.css
```

Django looks through:

- App-level `static/` folders  
- `STATICFILES_DIRS`

---

## 2️⃣ Static Files Discovery (Finders)

Django uses **finders** to locate static files:

- **AppDirectoriesFinder** → app `static/` folders  
- **FileSystemFinder** → `STATICFILES_DIRS`  

⚠️ You usually don’t need to change this.

---

## 3️⃣ `collectstatic` (Production Step)

In production, **Django does not serve static files**.

You must run:

```bash
python manage.py collectstatic
```

---

### What `collectstatic` Does

- Finds static files from:
  - App `static/` folders
  - `STATICFILES_DIRS`
- Copies them into **one directory**:

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

### Result

```text
staticfiles/
 ├── admin/
 ├── app/
 ├── css/
 └── js/
```

---

## 4️⃣ Serving Static Files in Production

### Django’s Role

❌ Django does **NOT** serve static files  
✅ Django only **collects** them

---

### Who Serves Static Files?

- Nginx  
- Apache  
- CDN (CloudFront, Cloudflare)

Example request:

```
/static/app/style.css
```

➡ Served **directly by the web server**

---

## 5️⃣ Static Files in Templates

### Load Static

```django
{% load static %}
```

### Use Static Files

```django
<link rel="stylesheet" href="{% static 'app/style.css' %}">
```

---

## 6️⃣ Why Django Separates Static Handling

- Better performance
- Lower server load
- Easier caching
- CDN support

---

## Common Mistakes

❌ Expecting Django to serve static files in production  
❌ Forgetting `collectstatic`  
❌ Hardcoding `/static/` paths  
❌ Mixing static and media files  

---

## Interview One-Liners

- Django serves static files **only in development**
- `collectstatic` gathers static assets
- Production uses **web servers or CDNs**

---

## Quick Summary

- Dev → Django serves static files  
- Prod → Django collects, web server serves  
- `STATIC_ROOT` is the final destination  
- `{% static %}` is the correct way to link files