# CORS (Cross-Origin Resource Sharing)

## WHAT  
CORS (Cross-Origin Resource Sharing) is a browser security mechanism used to control which external domains can access a Django server’s resources. It allows safe cross-origin API requests.

## WHY  
Browsers block cross-origin requests by default for security. Without CORS configuration, frontend apps on different domains cannot communicate with Django APIs.

## WHERE  
CORS is handled at the HTTP header level before the view logic runs. In Django, it is usually implemented using middleware.

## HOW  
The browser sends a request indicating its origin. Django responds with CORS headers specifying allowed origins, methods, and headers. The browser allows or blocks the request based on this response.

## WHEN  
CORS should be used when a frontend and backend run on different domains. It should not be enabled broadly for all origins in production.

## EXAMPLE  
A React app hosted on one domain accesses a Django REST API hosted on another domain using proper CORS headers.

## PROS & CONS  
CORS enables secure frontend–backend communication and fine-grained access control. However, misconfiguration can expose APIs or block valid requests.

## COMMON MISTAKES  
Allowing all origins in production is a common security mistake. Confusing CORS issues with server-side permission errors is also common.

<br>
<br>
<br>

# CORS (Cross-Origin Resource Sharing) – Simple Example

## What is CORS?

**CORS (Cross-Origin Resource Sharing)** is a browser security mechanism that controls whether a web page from one origin can request resources from another origin.

---

## Simple Example Scenario

A frontend application is running on:

```
https://example.com
```

It tries to call an API hosted at:

```
https://api.example.com
```

Because the **origins are different** (subdomain differs), the browser **blocks the request by default**.

---

## Why the Browser Blocks It

Browsers enforce the **Same-Origin Policy** to prevent malicious websites from reading sensitive data from other sites.

Different origin means a difference in **protocol, domain, or port**.

---

## How CORS Fixes This

If the API responds with proper **CORS headers**, the browser allows the response.

Example response header:

```
Access-Control-Allow-Origin: https://example.com
```

This tells the browser:

> “It’s safe to allow requests from example.com.”

---

## Important Point

CORS is enforced by the **browser**, not the server.  
The server only **declares rules**, and the browser decides whether to allow or block the response.

---

## One-Line Interview Takeaway

CORS allows a server to explicitly tell the browser which origins are permitted to access its resources.