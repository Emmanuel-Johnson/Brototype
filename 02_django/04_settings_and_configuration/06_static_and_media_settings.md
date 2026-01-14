## Big Picture Mental Model 🧠

**Static files → Developer-provided assets**  
**Media files → User-uploaded assets**

---

## 🧊 1. Static Files (STATIC)

### What they are
- Files **you write**
- **Don’t change at runtime**

### Examples
- CSS  
- JavaScript  
- Images (logos, icons)  
- Fonts  

---

### Typical Static Settings (`settings.py`)

```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

### Meaning of Each Setting 👇

#### 🔹 `STATIC_URL`
- URL prefix used in the browser  

Example:
```
http://example.com/static/css/style.css
```

#### 🔹 `STATICFILES_DIRS`
- Where Django looks **during development**
- Your **project-level static folder**

Structure:
```
project/
├── static/
│   ├── css/
│   └── js/
```

#### 🔹 `STATIC_ROOT`
- Used **only in production**
- `collectstatic` command dumps all static files here

Command:
```bash
python manage.py collectstatic
```

👉 **Nginx / Apache serves this folder directly**  
(Django steps aside)

---

## 🖼️ 2. Media Files (MEDIA)

### What they are
- Files **users upload**
- **Change at runtime**

### Examples
- Profile photos  
- Product images  
- PDFs uploaded by users  

---

### Media Settings (`settings.py`)

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

### Meaning 👇

#### 🔹 `MEDIA_URL`
- URL prefix to access uploaded files  

Example:
```
http://example.com/media/profile_pics/user1.jpg
```

#### 🔹 `MEDIA_ROOT`
- Folder where files are **physically stored**

Structure:
```
project/
├── media/
│   ├── profile_pics/
│   └── product_images/
```

---

## 🔗 Connecting Media to Models

Example:

```python
class Profile(models.Model):
    image = models.ImageField(upload_to='profile_pics/')
```

Uploaded file path:
```
media/profile_pics/image.jpg
```

---

## 🧪 Development vs Production

### ✅ Development
In `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

✔ Django serves media  
✔ Simple & convenient  

---

### 🚀 Production (IMPORTANT)
- Django **does NOT** serve static/media
- **Nginx / Apache** serves them

Flow:
```
Browser → Nginx → /static & /media
Browser → Gunicorn → Django (dynamic pages only)
```

---

## 🧠 One-line Memory Trick

**Static = shipped with code**  
**Media = uploaded by users**

Or even simpler 😄

- **Static → Developer stuff**  
- **Media → User stuff**