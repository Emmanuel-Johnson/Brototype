## WSGI --- Purpose

**WSGI (Web Server Gateway Interface)** is the standard interface
between a Python web application and a web server for **synchronous**
requests.

### Purpose

-   Lets web servers (Nginx + Gunicorn/uWSGI) talk to Python frameworks
    (Django, Flask)
-   Handles traditional **HTTP request → response**
-   One request is processed at a time per worker (blocking)

### What it's good for

-   Normal web pages\
-   CRUD apps\
-   REST APIs\
-   Forms, admin panels

### Mental model

    Browser → Web Server → WSGI → Django → Response

### Limitations

-   ❌ No WebSockets\
-   ❌ Poor at long-lived connections\
-   ❌ Blocking I/O

------------------------------------------------------------------------

## ASGI --- Purpose

**ASGI (Asynchronous Server Gateway Interface)** is the next-generation
interface for Python web apps that supports **async** and **multiple
protocols**.

### Purpose

-   Supports async code
-   Supports more than HTTP
-   Allows concurrent handling of requests

### What it's good for

-   WebSockets (chat apps)
-   Real-time notifications
-   Live dashboards
-   Long polling
-   Background async tasks

### Mental model

    Browser → Web Server → ASGI → Django → Response / WebSocket

### Capabilities

-   ✅ HTTP\
-   ✅ WebSockets\
-   ✅ Async views\
-   ✅ Non-blocking I/O

------------------------------------------------------------------------

## Django-specific clarity (important)

-   Django supports **both**
-   Default = **WSGI**
-   If you use:
    -   WebSockets
    -   Django Channels
    -   Async views seriously

    → you need **ASGI**

------------------------------------------------------------------------

## One-line comparison

| Feature        | WSGI          | ASGI            |
|---------------|---------------|-----------------|
| Nature        | Synchronous   | Asynchronous    |
| Protocols     | HTTP only     | HTTP + WebSockets |
| Concurrency   | Limited       | High            |
| Real-time apps| ❌            | ✅              |
| Django default| ✅            | ❌ (opt-in)     |


------------------------------------------------------------------------

## Exam / Interview one-liner

**WSGI** is for traditional synchronous Python web apps, while **ASGI**
is for async, real-time, and multi-protocol applications.