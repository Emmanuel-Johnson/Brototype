## 1. WHAT

**WSGI (Web Server Gateway Interface)** is a standard interface used to
connect Python web frameworks like **Django** with web servers so they
can handle HTTP requests and responses.

------------------------------------------------------------------------

## 2. WHY

Without WSGI, every framework would need custom logic to talk to
different web servers, causing:

-   Code duplication
-   Tight coupling
-   Poor portability

WSGI solves this by defining **one common contract** between servers and
frameworks.

------------------------------------------------------------------------

## 3. WHERE

WSGI sits **between the web server and the Django application**, acting
as the bridge in the request--response flow.

Example stack:

    Client → Nginx → Gunicorn (WSGI server) → Django

------------------------------------------------------------------------

## 4. HOW

1.  Web server receives an HTTP request
2.  Request is passed to the WSGI server
3.  WSGI server calls the Django WSGI application
4.  Django processes the request and returns a response
5.  Response flows back through the same path

------------------------------------------------------------------------

## 5. WHEN

Use **WSGI** when:

-   Running **traditional synchronous Django apps**
-   Serving standard HTTP request--response workloads
-   Deploying Django in production (Gunicorn, uWSGI, etc.)

Do **NOT** use WSGI when:

-   You need WebSockets
-   You need long-lived async connections
-   You're building real-time features

------------------------------------------------------------------------

## 6. EXAMPLE

In a Django project:

``` python
# project/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_wsgi_application()
```

A server like **Gunicorn** loads this file to serve the app in
production.

------------------------------------------------------------------------

## 7. PROS & CONS

### ✅ Pros

-   Simple and stable
-   Mature ecosystem
-   Widely supported
-   Easy to deploy

### ❌ Cons

-   Synchronous by design
-   Not suitable for async-heavy workloads
-   Cannot handle WebSockets

------------------------------------------------------------------------

## 8. COMMON MISTAKES

❌ Confusing **WSGI** with **ASGI** ❌ Using WSGI for WebSocket-based
features ❌ Running Django's built-in development server in production

------------------------------------------------------------------------

## One-Line Summary

> **WSGI is the standard bridge that allows synchronous Django apps to
> talk to web servers in production.**