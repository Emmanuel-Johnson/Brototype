In Django, **context** and **context processors** are how data reaches templates.

👉 Think of it like this:

- **Context** → data you pass manually  
- **Context processors** → data Django adds automatically  

---

## 1️⃣ What Is Context?

**Context** is a dictionary of data sent from a **View** to a **Template**.

### Example (View → Template)

```python
def home(request):
    return render(request, "home.html", {
        "username": "Emmanuel",
        "is_logged_in": True
    })
```

### Use in Template

```html
<h1>Hello {{ username }}</h1>

{% if is_logged_in %}
  <p>Welcome back!</p>
{% endif %}
```

🧠 **Context = page-specific data**

---

## 2️⃣ What Are Context Processors?

A **context processor** is a function that automatically injects variables into **every template**.

- You don’t need to pass them from each view  
- Used for **global data**  

---

## Built-in Context Processors (Important Ones)

Django provides these by default:

| Context Processor | What It Provides |
|------------------|-----------------|
| `request` | request object |
| `auth` | user, permissions |
| `messages` | flash messages |
| `static` | static file URLs |
| `csrf` | CSRF token |

### Example Usage (Template)

```html
{% if user.is_authenticated %}
  Hello {{ user.username }}
{% endif %}
```

⚡ No view code needed!

---

## 3️⃣ Custom Context Processor (Very Important)

### Step 1: Create a Function

```python
# app/context_processors.py
def site_info(request):
    return {
        "site_name": "MyShop",
        "support_email": "support@myshop.com"
    }
```

---

### Step 2: Register It

```python
# settings.py
TEMPLATES = [
    {
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "app.context_processors.site_info",
            ],
        },
    },
]
```

---

### Step 3: Use in Any Template

```html
<footer>
  {{ site_name }} | {{ support_email }}
</footer>
```

🧠 Once registered → **available everywhere**

---

## Context vs Context Processor (Interview Gold)

| Feature | Context | Context Processor |
|------|--------|------------------|
| Scope | Single view | All templates |
| Passed manually | ✅ | ❌ |
| Automatic | ❌ | ✅ |
| Use case | Page-specific | Global data |

---

## Where Context Processors Are Used

✔ Navbar user info  
✔ Site name & branding  
✔ Cart item count  
✔ Notifications  
✔ Logged-in user data  

---

## Performance Tip ⚠️

- Context processors run on **every request**
- Keep them **light**
- Avoid database queries unless cached

---

## Simple Mental Model 🧩

- **Context** → “This page needs this data”  
- **Context processor** → “Every page needs this data”  

---

## 🎯 One-Line Interview Answer

> **“Context is data passed from a view to a template, while context processors automatically inject global data into all templates in Django.”**