# WSGI vs ASGI

## Feature Comparison

| Feature | WSGI | ASGI |
|------|------|------|
| **Full form** | Web Server Gateway Interface | Asynchronous Server Gateway Interface |
| **Type** | Synchronous | Asynchronous |
| **Request handling** | One request per worker (blocking) | Many requests concurrently (non-blocking) |
| **Protocols supported** | HTTP only | HTTP, WebSockets, background tasks |
| **Real-time support** | ❌ No | ✅ Yes |
| **WebSockets** | ❌ Not supported | ✅ Supported |
| **Long-lived connections** | ❌ Poor | ✅ Designed for it |
| **Performance** | Good for normal apps | Better for high-concurrency apps |
| **Django default** | ✅ Yes | ❌ Optional |
| **Common servers** | Gunicorn, uWSGI | Daphne, Uvicorn |
| **Async views** | ❌ No | ✅ Yes |

------------------------------------------------------------------------

## Simple flow difference

### WSGI (blocking)

    Request → Worker → Django → Response
    (wait until finished)

### ASGI (non-blocking)

    Request → Event Loop → Django → Response
    (many handled at once)

------------------------------------------------------------------------

## When to use what

### Use WSGI when:

-   Normal websites
-   REST APIs
-   Admin dashboards
-   No real-time features

### Use ASGI when:

-   Chat applications
-   Live notifications
-   Streaming data
-   WebSockets
-   High concurrency

------------------------------------------------------------------------

## Django reality (important)

-   Django runs perfectly on **WSGI**
-   **ASGI is not mandatory**
-   Switch to ASGI only when you need async features
-   **Django Channels = ASGI required**

------------------------------------------------------------------------

## Interview one-liner

**WSGI** handles synchronous HTTP requests, while **ASGI** handles
asynchronous, real-time, and multi-protocol communication.