## 1. Django Session

A **Django session** is a server-side mechanism used to store user-specific data across multiple HTTP requests.  
Instead of storing data in the browser, Django stores it on the **server** and sends only a **session ID** to the client as a cookie.  
This helps maintain state in the otherwise stateless **HTTP protocol**.

### Example

```python
from django.http import HttpResponse

def set_session(request):
    request.session['user_name'] = 'Emmanuel'
    return HttpResponse("Session created")
```

<br>
<br>
<br>

## 2. Django Session Management

**Session management** refers to how Django creates, stores, updates, expires, and deletes sessions.  
Django handles this automatically using **middleware** and a **session backend** (database, cache, file, or cache+db).

### Key Responsibilities

- Generating a unique session ID  
- Storing session data securely on the server  
- Sending the session ID via cookies  
- Expiring sessions based on time or logout  

### Example (Logout)

```python
from django.shortcuts import redirect

def logout_view(request):
    request.session.flush()  # deletes session data + session ID
    return redirect('login')
```

Session data is usually stored in the database table:

```
django_session
```

<br>
<br>
<br>

## 3. Session-Based Authentication

**Session-based authentication** is a login mechanism where, after successful authentication, the user’s identity is stored in a session.  
On every request, Django checks the session to verify whether the user is authenticated.

This is the **default authentication mechanism** used by Django.

### Authentication Flow

1. User submits login credentials  
2. Django verifies credentials  
3. User ID is stored in the session  
4. Session ID is sent as a cookie  
5. Every request uses this session ID to identify the user  

### Example

```python
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect

def login_view(request):
    user = authenticate(username='admin', password='1234')
    if user:
        login(request, user)  # stores user ID in session
        return redirect('dashboard')

def dashboard(request):
    if request.user.is_authenticated:
        return HttpResponse("Welcome")
    return redirect('login')
```

---

## Key Interview Comparison Points

- Sessions are **server-side**, cookies are **client-side**
- Session-based authentication is **stateful**
- Django automatically handles session security
- Logout clears the **session**, not just cookies