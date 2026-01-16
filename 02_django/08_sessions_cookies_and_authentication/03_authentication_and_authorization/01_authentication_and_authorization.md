# Authentication

## What is Authentication?

**Authentication** is the process of verifying who a user is before allowing access to protected parts of an application.  
It answers the question: **“Are you really who you claim to be?”**

---

## How Authentication Works (High Level)

1. User submits credentials (username/password)  
2. Server verifies credentials  
3. If valid, server marks the user as authenticated  
4. User can now access protected resources  

---

## Authentication in Django

Django provides a **built-in authentication system** that handles users, passwords, sessions, and permissions.

---

## Login Example

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def login_view(request):
    user = authenticate(username='admin', password='1234')
    if user:
        login(request, user)  # creates session
        return redirect('dashboard')
```

---

## Checking Authentication

```python
from django.http import HttpResponse
from django.shortcuts import redirect

def dashboard(request):
    if request.user.is_authenticated:
        return HttpResponse("Welcome")
    return redirect('login')
```

---

## Logout Example

```python
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # clears session
    return redirect('login')
```

---

## Common Authentication Types (Interview Important)

### 1. Session-Based Authentication

- User info stored in **server-side session**
- Session ID stored in a cookie
- **Default in Django**
- Stateful

### 2. Token-Based Authentication (JWT)

- Server returns a token
- Client sends token on each request
- Common in REST APIs
- Stateless

### 3. OAuth / Social Login

- Login using Google, GitHub, etc.
- Authentication delegated to a third party

---

## Authentication vs Authorization (Classic Question)

- **Authentication** → Who are you?  
- **Authorization** → What are you allowed to do?  

### Example

- Login → authentication  
- Admin-only page → authorization  

---

## Key Interview Points

- Authentication establishes **identity**
- Django uses **session-based authentication** by default
- Passwords are **hashed**, never stored in plain text
- Middleware automatically attaches `request.user`
- Logout destroys the **session**, not just cookies

<br>
<br>
<br>

# Authorization

## What is Authorization?

**Authorization** is the process of determining what an authenticated user is allowed to do.  
It answers the question: **“Do you have permission to access this resource or perform this action?”**

---

## Authorization Flow

1. User logs in → authenticated  
2. System checks user’s permissions or role  
3. Access is granted or denied based on rules  

**Authentication must happen before authorization.**

---

## Authorization in Django

Django provides authorization using **permissions**, **groups**, and **roles** (implemented via groups).

---

## 1. Permission-Based Authorization

Django automatically creates permissions for each model:

- `add`
- `change`
- `delete`
- `view`

### Example

```python
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

@permission_required('app.view_product', raise_exception=True)
def product_list(request):
    return HttpResponse("Product list")
```

---

## 2. Group-Based Authorization (Roles)

Groups act like roles such as **Admin**, **Editor**, or **User**.

### Example

```python
from django.http import HttpResponse

def dashboard(request):
    if request.user.groups.filter(name='Admin').exists():
        return HttpResponse("Admin dashboard")
    return HttpResponse("User dashboard")
```

---

## 3. Using `@login_required`

This ensures authentication and is often used as the **first authorization gate**.

```python
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def profile(request):
    return HttpResponse("Profile page")
```

---

## 4. Class-Based View Authorization

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from django.http import HttpResponse

class ProductView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'app.view_product'

    def get(self, request):
        return HttpResponse("Product view")
```

---

## Authentication vs Authorization (One-Line)

- **Authentication** → Who you are  
- **Authorization** → What you can do  

---

## Key Interview Points

- Authorization always comes **after authentication**
- Django permissions are **model-based**
- Groups simplify permission management
- **Superusers** bypass all permission checks
- Unauthorized access returns **403 Forbidden**