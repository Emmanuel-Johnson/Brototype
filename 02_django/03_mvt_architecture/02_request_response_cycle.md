## ✅ High-Level Flow

```
Client (Browser)
    │
    │  HTTP Request
    ▼
Reverse Proxy / Web Server
(Nginx)
    │
    │  Forwards request
    ▼
Application Server
(Gunicorn / uWSGI)
    │
    │  WSGI call
    ▼
Django Application
    │
    ├─ Middleware (request phase)
    │
    ├─ URL Dispatcher (urls.py)
    │
    ├─ View (views.py)
    │     ├─ Model (database, optional)
    │     └─ Template (HTML, optional)
    │
    ├─ Middleware (response phase)
    │
    ▼
Response Object
    │
    │  Returned via WSGI
    ▼
Gunicorn
    │
    │  Back to reverse proxy
    ▼
Nginx
    │
    │  HTTP Response
    ▼
Client (Browser)
```

---

## 🧠 Step-by-Step (Plain English)

### 1️⃣ Client (Browser)
- User types a URL or clicks a link  
- An **HTTP request** is created

---

### 2️⃣ Nginx (Reverse Proxy / Web Server)
- Accepts the request  
- Handles **SSL / HTTPS**  
- Serves static files (if any)  
- Forwards dynamic requests to **Gunicorn**

---

### 3️⃣ Gunicorn (Application Server)
- Receives request from Nginx  
- Converts HTTP request into **WSGI format**  
- Passes it to Django

---

### 4️⃣ Django Application
Request processing inside Django:

- **Middleware (request phase)** → security, authentication, sessions  
- **URL Dispatcher** → decides which view runs  
- **View** → executes business logic  
- **Model (optional)** → database interaction  
- **Template (optional)** → HTML rendering  
- **Middleware (response phase)** → headers, cookies  

---

### 5️⃣ Response Goes Back
Response travels back through the same layers:

```
Django → Gunicorn → Nginx → Browser
```

---

## 🎯 One-Line Interview Answer

> **“In production, the browser sends a request to Nginx, which acts as a reverse proxy and forwards it to Gunicorn. Gunicorn passes the request to Django via WSGI. Django processes it through middleware, URL routing, views, models, and templates, then sends the response back through Gunicorn and Nginx to the browser.”**