# STATIC_ROOT vs MEDIA_ROOT in Django

## STATIC_ROOT

### What is STATIC_ROOT?

`STATIC_ROOT` is the directory where **all static files are collected** when you run:

```bash
python manage.py collectstatic
```

### Example

```python
STATIC_ROOT = BASE_DIR / "staticfiles"
```

### Key Points

- Used **only in production**
- Target directory for `collectstatic`
- Contains:
  - CSS
  - JavaScript
  - Images (logos, icons)
- Django does **not** serve files from here in production

---

## MEDIA_ROOT

### What is MEDIA_ROOT?

`MEDIA_ROOT` is the directory where **user-uploaded files** are stored.

### Example

```python
MEDIA_ROOT = BASE_DIR / "media"
```

### Key Points

- Used in **development & production**
- Stores:
  - Profile pictures
  - Product images
  - Uploaded files
- Used by `FileField` / `ImageField`

---

## Side-by-Side Comparison

| Feature | STATIC_ROOT | MEDIA_ROOT |
|------|-------------|------------|
| Purpose | Collected static files | User uploads |
| Created by | Developer | User |
| Changes at runtime | ❌ No | ✅ Yes |
| `collectstatic` | ✅ Yes | ❌ No |
| Stored in Git | ❌ No | ❌ No |
| Django serves (prod) | ❌ No | ❌ No |

---

## Related Settings (Important)

```python
STATIC_URL = "/static/"
MEDIA_URL = "/media/"
```

- These are **URL paths**
- Not file system paths

---

## Typical Project Structure

```text
project/
 ├── static/        # app-level static files
 ├── staticfiles/   # STATIC_ROOT (after collectstatic)
 ├── media/         # MEDIA_ROOT (uploads)
```

---

## Common Mistakes

❌ Using `STATIC_ROOT` for uploads  
❌ Expecting Django to serve `STATIC_ROOT` in production  
❌ Confusing `STATIC_ROOT` with `STATICFILES_DIRS`  
❌ Committing `media/` or `staticfiles/` to Git  

---

## Interview One-Liners

- **STATIC_ROOT** → `collectstatic` destination  
- **MEDIA_ROOT** → user uploads storage  
- Static ≠ Media  
- Django serves **neither** in production  

---

## Quick Summary

- `STATIC_ROOT` = collected static assets
- `MEDIA_ROOT` = uploaded files
- Both are file system paths
- Used for different purposes