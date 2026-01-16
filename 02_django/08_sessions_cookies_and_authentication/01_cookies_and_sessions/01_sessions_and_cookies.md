# Django Sessions

## WHAT  
Django Sessions is a mechanism used to store user-specific data across multiple HTTP requests. It helps the server remember information about a user between page loads.

## WHY  
HTTP is stateless, so the server forgets everything after each request. Without sessions, handling login state, carts, or step-based flows becomes repetitive and error-prone.

## WHERE  
Sessions work at the middleware level in Django’s request–response cycle. The session data is accessed inside views via the request object.

## HOW  
Django creates a session ID and stores it in a cookie on the client. The actual session data is stored server-side (database, cache, or file). On each request, Django uses the session ID to retrieve the user’s data.

## WHEN  
Sessions are used for authenticated users, shopping carts, and temporary user state. They should not be used for large data or long-term storage like user preferences.

## EXAMPLE  
After login, Django stores the user’s ID in the session so the user remains logged in across different pages.

## PROS & CONS  
Sessions improve user experience and security by keeping data server-side and reducing repeated queries. However, they consume server resources and can affect performance if overused.

## COMMON MISTAKES  
Storing large objects or sensitive data directly in sessions is a common mistake. Forgetting to clear session data on logout can also cause security issues.

<br>
<br>
<br>

# Simple Django Session Example

## 1. Enable Sessions (Default)

In `settings.py`, sessions are already enabled in most projects:

```python
INSTALLED_APPS = [
    'django.contrib.sessions',
]
```

```python
MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
]
```

---

## 2. Setting Session Data

```python
from django.http import HttpResponse

def set_session(request):
    request.session['user_name'] = 'Emmanuel'
    request.session['login_count'] = 1
    return HttpResponse("Session set")
```

This stores data on the server and links it to the user via a **session ID cookie**.

---

## 3. Getting Session Data

```python
def get_session(request):
    name = request.session.get('user_name')
    count = request.session.get('login_count')
    return HttpResponse(f"Name: {name}, Count: {count}")
```

---

## 4. Updating Session Data

```python
def update_session(request):
    request.session['login_count'] += 1
    return HttpResponse("Session updated")
```

---

## 5. Deleting Session Data

```python
def delete_session(request):
    request.session.pop('user_name', None)
    request.session.flush()  # removes all session data
    return HttpResponse("Session cleared")
```

---

## 6. Real‑World Example (Login‑like Behavior)

```python
from django.shortcuts import redirect

def login_view(request):
    if request.method == "POST":
        request.session['user_id'] = 5
        return redirect('dashboard')

def dashboard(request):
    if not request.session.get('user_id'):
        return redirect('login')
    return HttpResponse("Welcome to dashboard")
```

---

## Key Points to Remember (Interview‑Friendly)

- Session data is stored **server‑side**
- Browser stores only a **session ID cookie**
- Safer than cookies for sensitive data
- Common uses: login state, cart data, user preferences

<br>
<br>
<br>

# Cookies

## WHAT  
Cookies is a client-side storage mechanism used to store small pieces of data in the user’s browser. It helps the server identify or remember a user across requests.

## WHY  
HTTP requests are stateless, so the server cannot recognize returning users by default. Without cookies, maintaining login state, preferences, or session tracking becomes difficult.

## WHERE  
Cookies live in the user’s browser and travel with every HTTP request to the server. In Django, they are set and read in the response–request cycle via the request and response objects.

## HOW  
The server sends a cookie in the HTTP response. The browser stores it and automatically includes it in future requests. Django reads the cookie value from the incoming request.

## WHEN  
Cookies are used for session IDs, user preferences, and basic tracking. They should not be used to store sensitive or large amounts of data.

## EXAMPLE  
Django stores a session ID in a cookie so the server can identify a logged-in user on each request.

## PROS & CONS  
Cookies are simple, lightweight, and automatically sent with requests. However, they have size limits and can be modified by users, making them insecure for sensitive data.

## COMMON MISTAKES  
Storing passwords or sensitive data in cookies is a serious mistake. Relying on cookies alone without server-side validation is also risky.

<br>
<br>
<br>

# Django Cookies – Simple Example

In Django, cookies are used to store small pieces of data on the **client (browser)** and are sent back to the server with every request.

---

## 1. Setting a Cookie

```python
from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("Cookie set")
    response.set_cookie(
        key='user_name',
        value='Emmanuel',
        max_age=3600  # 1 hour
    )
    return response
```

The data is stored in the **browser**.

---

## 2. Getting a Cookie

```python
def get_cookie(request):
    name = request.COOKIES.get('user_name')
    return HttpResponse(f"User name: {name}")
```

---

## 3. Deleting a Cookie

```python
def delete_cookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('user_name')
    return response
```

---

## 4. Cookie with Security Flags

```python
def secure_cookie(request):
    response = HttpResponse("Secure cookie set")
    response.set_cookie(
        'session_token',
        'abc123',
        httponly=True,
        secure=True,
        samesite='Lax'
    )
    return response
```

This prevents JavaScript access and reduces **CSRF risk**.

---

## 5. Real-World Example (Remember Me)

```python
from django.shortcuts import redirect

def login_view(request):
    response = redirect('dashboard')
    response.set_cookie('remember_me', 'yes', max_age=7*24*60*60)
    return response

def dashboard(request):
    if request.COOKIES.get('remember_me') != 'yes':
        return redirect('login')
    return HttpResponse("Welcome back")
```

---

## Key Interview Points

- Cookies are stored in the **browser**
- Limited size (≈ **4KB**)
- Can be modified by users → **not secure**
- Used for preferences, language, theme, tracking
- Django sessions internally use cookies to store **session ID**