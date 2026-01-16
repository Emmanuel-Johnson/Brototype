## WHAT  
Middleware is a layer in Django used to process requests and responses globally before they reach views. It allows cross-cutting logic to run for every request.

## WHY  
Many concerns like authentication, security, and logging apply to all views. Without middleware, this logic would be repeated in every view and become hard to maintain.

## WHERE  
Middleware sits between the web server and Django views in the request–response cycle. Each request passes through middleware before the view and each response passes back through it.

## HOW  
Django receives a request and passes it through middleware classes in order. The view is executed if allowed. The response then passes back through the same middleware in reverse order.

## WHEN  
Middleware should be used for global behavior affecting many views. It should not be used for business logic specific to a single feature or page.

## EXAMPLE  
Django’s authentication middleware attaches the logged-in user to `request.user` for every request.

## PROS & CONS  
Middleware keeps code centralized, reusable, and clean. However, too many middleware can slow requests and make debugging harder.

## COMMON MISTAKES  
Placing heavy database logic inside middleware is a common mistake. Using middleware for view-specific logic reduces clarity and flexibility.

<br>
<br>
<br>

# Middleware

## What is Middleware?

**Middleware** is a layer in Django that processes a request **before it reaches the view** and processes the response **before it is sent back to the client**.  
It acts like a chain of filters around every **request–response cycle**.

---

## Where Middleware Fits

```
Request → Middleware → View → Middleware → Response
```

Each middleware looks at the request on the way in and the response on the way out.

---

## What Middleware Can Do

Each middleware can:

- Modify the request  
- Stop the request early and return a response  
- Modify the response  

---

## Built-in Middleware Examples

- **SecurityMiddleware** → adds security-related headers  
- **SessionMiddleware** → enables session support  
- **AuthenticationMiddleware** → attaches `request.user`  
- **CsrfViewMiddleware** → provides CSRF protection  

---

## Custom Middleware Example

```python
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before view")
        response = self.get_response(request)
        print("After view")
        return response
```

### Add Middleware in `settings.py`

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'app.middleware.SimpleMiddleware',
]
```

---

## Middleware vs Decorators

- **Middleware** → runs on **every request**  
- **Decorators** → apply to **specific views only**  

---

## Key Interview Points

- Middleware runs **globally**
- Order in `MIDDLEWARE` **matters**
- Can **short-circuit** requests (return response early)
- Common uses: authentication, logging, security, throttling
- Works for both **FBV** and **CBV**

<br>
<br>
<br>

# Request / Response Middleware Flow

In Django, the **request–response middleware flow** describes how an HTTP request travels through middleware, reaches the view, and how the response travels back through middleware before reaching the browser.

---

## High-Level Flow

```
Browser
  ↓
Request
  ↓
Middleware (top → bottom)
  ↓
URL Resolver
  ↓
View
  ↓
Middleware (bottom → top)
  ↓
Response
  ↓
Browser
```

---

## Detailed Step-by-Step Flow

### 1. Incoming Request

- Browser sends an HTTP request  
- Django creates an `HttpRequest` object  

---

### 2. Request Middleware (Top → Bottom)

Middleware listed in `MIDDLEWARE` runs **in order**.

Each middleware can:

- Modify the request  
- Block the request by returning a response  

```python
def __call__(self, request):
    # request phase
```

---

### 3. URL Resolution

- Django matches the URL to a view using `urls.py`

---

### 4. View Execution

- The matched view (FBV or CBV) runs  
- Business logic is executed  
- A response is returned  

---

### 5. Response Middleware (Bottom → Top)

- Middleware runs again in **reverse order**
- Each middleware can modify the response  

```python
response = self.get_response(request)
# response phase
```

---

### 6. Final Response

- Django sends the `HttpResponse` back to the browser  

---

## Visual Order Example

If middleware order is:

```python
MIDDLEWARE = [
    'A',
    'B',
    'C',
]
```

### Execution Order

```
Request  → A → B → C → View
Response ← A ← B ← C ← View
```

---

## Key Interview Points

- Request phase → **top to bottom**
- Response phase → **bottom to top**
- Middleware can **short-circuit** the request
- Order matters for authentication, sessions, and CSRF
- `AuthenticationMiddleware` depends on `SessionMiddleware`

<br>
<br>
<br>

# Default Django Middleware

Default Django middleware are the middleware classes that Django includes by default when you create a new project.  
They handle **security, sessions, authentication, CSRF protection**, and common request/response processing.

---

## Default Middleware List (Typical)

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

---

## What Each Middleware Does

### 1. SecurityMiddleware
- Adds security-related HTTP headers  
- Protects against common attacks (SSL, HSTS, etc.)  

### 2. SessionMiddleware
- Enables session support  
- Reads and writes session data for each request  

### 3. CommonMiddleware
- Handles common web operations  
- URL normalization (trailing slash), basic request handling  

### 4. CsrfViewMiddleware
- Protects against CSRF attacks  
- Validates CSRF tokens for unsafe HTTP methods  

### 5. AuthenticationMiddleware
- Attaches `request.user` to every request  
- Enables login/logout and permission checks  

### 6. MessageMiddleware
- Enables Django’s messaging framework  
- Used for flash messages (success, error)  

### 7. XFrameOptionsMiddleware
- Prevents clickjacking attacks  
- Controls whether the site can be embedded in an iframe  

---

## Order Matters (Important Interview Point)

- `SessionMiddleware` must come **before** `AuthenticationMiddleware`  
- `AuthenticationMiddleware` depends on session data  
- `CsrfViewMiddleware` must come **after** `SessionMiddleware`  

---

## Key Interview Points

- Middleware runs on **every request**
- Default middleware covers most **security needs**
- Removing middleware can break features **silently**
- Order in `MIDDLEWARE` is **critical**

<br>
<br>
<br>

# Custom Middleware

## What is Custom Middleware?

**Custom middleware** in Django is user-defined middleware used to execute custom logic **before a request reaches the view** and/or **after the response is returned**.  
It is useful when logic must run **globally for all requests**.

---

## When to Use Custom Middleware

- Logging requests  
- Custom authentication checks  
- Blocking requests (IP-based, time-based access)  
- Measuring request/response time  
- Adding custom headers  

---

## Basic Custom Middleware Example

### 1. Create Middleware File

```python
# app/middleware.py

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view (request phase)
        print("Request received")

        response = self.get_response(request)

        # After view (response phase)
        print("Response sent")

        return response
```

---

### 2. Register Middleware

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'app.middleware.CustomMiddleware',
]
```

---

## Blocking a Request in Middleware

```python
from django.http import HttpResponseForbidden

class BlockMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Access denied")
        return self.get_response(request)
```

This **short-circuits** the request and prevents the view from executing.

---

## Middleware vs Decorators

- **Middleware** → global (runs on all requests)  
- **Decorators** → applied to specific views  
- Middleware is best for **cross-cutting concerns**  

---

## Key Interview Points

- Middleware runs on **every request**
- Can modify **request or response**
- Can **short-circuit** request flow
- Order in `MIDDLEWARE` **matters**
- Works with both **FBV** and **CBV**