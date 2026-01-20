## 1. WHAT

**ASGI (Asynchronous Server Gateway Interface)** is a standard interface
used to run Python web frameworks like **Django** in an asynchronous way
and handle long‑lived connections.

------------------------------------------------------------------------

## 2. WHY

**WSGI cannot efficiently handle real‑time features** like:

-   WebSockets\
-   Long polling\
-   Server‑sent events

Without ASGI, implementing async tasks and concurrent connections
becomes complex and inefficient.

------------------------------------------------------------------------

## 3. WHERE

ASGI sits **between the ASGI server and the Django application**,
managing both HTTP requests and async protocols.

Example stack:

    Client → Nginx → Uvicorn / Daphne (ASGI server) → Django

------------------------------------------------------------------------

## 4. HOW

1.  ASGI server receives a request or event\
2.  Event is passed to the Django ASGI application\
3.  Django processes it **synchronously or asynchronously**\
4.  Response/event is sent back through the server

ASGI supports **multiple protocols**, not just HTTP.

------------------------------------------------------------------------

## 5. WHEN

Use **ASGI** when:

-   You need **WebSockets**
-   You need real‑time features (chat, notifications)
-   You want async views or background consumers
-   You expect many concurrent connections

Do **NOT** use ASGI when:

-   App is purely synchronous
-   Simplicity is the main goal
-   No real‑time features are required

------------------------------------------------------------------------

## 6. EXAMPLE

A Django chat application using **WebSockets** with **Django Channels**
runs on ASGI to handle many live connections efficiently.

``` python
# project/asgi.py
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

application = get_asgi_application()
```

An ASGI server like **Daphne** or **Uvicorn** loads this file.

------------------------------------------------------------------------

## 7. PROS & CONS

### ✅ Pros

-   Supports async code
-   Handles WebSockets
-   High concurrency
-   Modern real‑time workloads

### ❌ Cons

-   More complex than WSGI
-   Blocking code hurts performance
-   Requires async‑safe libraries

------------------------------------------------------------------------

## 8. COMMON MISTAKES

❌ Assuming ASGI makes all Django code async\
❌ Using blocking ORM calls inside async views\
❌ Forgetting async safety when calling external APIs

------------------------------------------------------------------------

## One‑Line Summary

> **ASGI enables Django to handle async code, WebSockets, and real‑time
> features efficiently.**