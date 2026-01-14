## 🧩 What Is MIDDLEWARE?

In Django, **MIDDLEWARE** is a pipeline of components that process **every request before it reaches the view** and **every response before it goes back to the browser**.

👉 Think of it as **security + logic checkpoints** for each request.

---

## 🎯 Purpose of Middleware

Middleware allows Django to:

- Add security (CSRF, clickjacking, HTTPS)  
- Manage sessions & authentication  
- Modify requests and responses  
- Apply global logic (logging, locale, custom headers)  

📌 **Middleware runs automatically on every request.**

---

## 🧱 Default MIDDLEWARE Example

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

## 🔄 Request–Response Flow

```
Request
  ↓
SecurityMiddleware
  ↓
SessionMiddleware
  ↓
CommonMiddleware
  ↓
CsrfViewMiddleware
  ↓
AuthenticationMiddleware
  ↓
MessageMiddleware
  ↓
View
  ↑
MessageMiddleware
  ↑
AuthenticationMiddleware
  ↑
CsrfViewMiddleware
  ↑
CommonMiddleware
  ↑
SessionMiddleware
  ↑
SecurityMiddleware
Response
```

👉 **Order matters** — top → bottom on request, bottom → top on response.

---

## 🧠 What Each Middleware Does (Simple)

### 🔐 SecurityMiddleware
- HTTPS enforcement  
- HSTS headers  
- Secure cookies  

---

### 🗂️ SessionMiddleware
- Enables `request.session`  
- Stores user session data  

⚠️ Must come **before AuthenticationMiddleware**.

---

### 🌐 CommonMiddleware
- Handles trailing slashes  
- Adds ETag headers  
- Blocks bad user agents  

---

### 🛡️ CsrfViewMiddleware
- Protects against CSRF attacks  
- Required for POST forms  

---

### 👤 AuthenticationMiddleware
- Adds `request.user`  
- Handles logged-in state  

---

### 💬 MessageMiddleware
- Enables flash messages  
- Uses sessions or cookies  

---

### 🖼️ XFrameOptionsMiddleware
- Prevents clickjacking  
- Controls iframe embedding  

---

## ⚠️ Security Implications

- ❌ Wrong order → broken authentication / CSRF  
- ❌ Removing CSRF middleware → serious vulnerability  
- ❌ Removing SecurityMiddleware → weaker HTTPS protection  

👉 **Middleware mistakes can expose your entire app.**

---

## ✍️ Custom Middleware Example

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

Add it to `settings.py`:

```python
MIDDLEWARE += ['myapp.middleware.SimpleMiddleware']
```

---

## 🧠 Mental Model

> **Middleware is like an airport security line ✈️**  
> Every passenger (request) must pass all checkpoints, both entering and leaving.