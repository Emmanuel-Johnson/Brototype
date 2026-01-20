## Browser Cache

The browser cache is where the browser stores copies of responses (HTML, CSS, JS, images) so it doesn’t have to re-download them every time.  
If a resource hasn’t changed, the browser serves it directly from cache, making pages load much faster and reducing server load.

## Cache Headers

Cache headers are HTTP response headers that tell the browser whether, how, and for how long to cache a response.  
Common ones are `Cache-Control` (rules like `max-age`, `no-cache`), `ETag` (content version), and `Last-Modified` (timestamp) to decide if cached data is still valid.

## Django Caching Basics

Django caching is a server-side mechanism to store expensive results (views, queries, templates) and reuse them instead of recomputing.  
It can cache at multiple levels—per-view, per-template, per-query, or entire pages—using backends like memory, Redis, or database, improving performance and scalability.

## How They Work Together (Big Picture)

Browser cache avoids hitting the server at all.  
Django caching speeds things up when the server is hit.  
Together, they reduce latency, server load, and response time in production apps.
