# Django Cookie Expiry Examples

This document shows different ways to control **cookie expiry** in Django.

---

## 1. Cookie with `max_age` (seconds)

```python
from django.http import HttpResponse

def set_cookie_max_age(request):
    response = HttpResponse("Cookie set for 1 hour")
    response.set_cookie(
        'theme',
        'dark',
        max_age=3600  # 1 hour
    )
    return response
```

The cookie expires after the given number of **seconds**.

---

## 2. Cookie with `expires` (specific date/time)

```python
from datetime import datetime, timedelta
from django.http import HttpResponse

def set_cookie_expires(request):
    response = HttpResponse("Cookie set with expiry date")
    expiry = datetime.utcnow() + timedelta(days=1)
    response.set_cookie(
        'language',
        'en',
        expires=expiry
    )
    return response
```

The cookie expires at a **fixed date and time**.

---

## 3. Session Cookie (Expires on Browser Close)

```python
from django.http import HttpResponse

def set_session_cookie(request):
    response = HttpResponse("Session cookie set")
    response.set_cookie('temp_data', '123')
    return response
```

No `max_age` or `expires` → cookie is deleted when the **browser closes**.

---

## 4. Delete Cookie Immediately

```python
from django.http import HttpResponse

def delete_cookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('theme')
    return response
```

---

## Key Interview Points

- `max_age` → **relative time** (in seconds)
- `expires` → **absolute date/time**
- If both are set, **`max_age` takes priority**
- No expiry → **session cookie**
- Cookies persist only until expiry or manual deletion