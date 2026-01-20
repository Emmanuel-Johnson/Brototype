# Gunicorn --- Explained Simply

**Gunicorn (Green Unicorn)** is a Python **WSGI HTTP server** used to
run Django (and other Python web apps) in production.

It sits between the web server and Django.

------------------------------------------------------------------------

## Gunicorn's purpose

-   Runs your Django app\
-   Handles incoming HTTP requests\
-   Manages multiple worker processes\
-   Talks to Django using **WSGI**

**Flow:**

    Client → Nginx → Gunicorn → Django (WSGI)

------------------------------------------------------------------------

## Why Gunicorn is needed

### Django's built-in server

-   ❌ Single-threaded\
-   ❌ Not secure\
-   ❌ Not production-ready

### Gunicorn

-   ✅ Production-ready\
-   ✅ Fast\
-   ✅ Handles concurrency\
-   ✅ Battle-tested

------------------------------------------------------------------------

## How Gunicorn works (important)

### Master process

-   Manages workers

### Worker processes

-   Handle requests\
-   Each worker handles **one request at a time** (sync workers)

```{=html}
<!-- -->
```
    Gunicorn
     ├── Master
     ├── Worker 1 → request
     ├── Worker 2 → request
     └── Worker 3 → idle

------------------------------------------------------------------------

## Worker types (key concept)

### 1. Sync (default)

-   Blocking\
-   Best for normal Django apps

### 2. Async (gevent / eventlet)

-   Cooperative concurrency\
-   Still **WSGI**\
-   ❌ Not WebSockets-friendly

------------------------------------------------------------------------

## Gunicorn vs ASGI servers

  Feature           Gunicorn               Uvicorn / Daphne
  ----------------- ---------------------- ------------------
  Interface         WSGI                   ASGI
  WebSockets        ❌                     ✅
  Async support     ❌                     ✅
  Django Channels   ❌                     ✅
  Typical use       Standard Django apps   Real-time apps

------------------------------------------------------------------------

## Can Gunicorn run ASGI?

-   ❌ Gunicorn itself is **WSGI**
-   ⚠️ It can wrap **Uvicorn workers**, but:
    -   You're effectively using an ASGI server
    -   This is an advanced setup

------------------------------------------------------------------------

## Typical production setup

### Classic Django app

    Nginx → Gunicorn → Django

### Real-time Django app (Channels)

    Nginx → Uvicorn / Daphne → Django Channels

------------------------------------------------------------------------

## Interview one-liner

**Gunicorn** is a production-grade **WSGI server** used to run Django
applications behind a web server like Nginx.

------------------------------------------------------------------------

### Final mental map

    Nginx → Gunicorn (WSGI) → Django

When real-time enters the picture, **Gunicorn steps aside for ASGI
servers**.