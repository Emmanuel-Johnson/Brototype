# Rate Limiting

## WHAT  
Rate limiting is a mechanism used to restrict how many requests a client can make to a Django application within a given time window. It protects the system from abuse and overload.

## WHY  
Without rate limiting, APIs can be abused through excessive requests, causing performance issues or downtime. Manually controlling request frequency in each view would be repetitive and unreliable.

## WHERE  
Rate limiting is applied at the API or middleware layer before view logic executes. In Django, it is commonly used with Django REST Framework or custom middleware.

## HOW  
Django tracks requests per user or IP over time. If the request count exceeds the defined limit, further requests are blocked or delayed. Allowed requests continue normally.

## WHEN  
Rate limiting should be used on public APIs, login endpoints, and sensitive operations. It should not be too strict on internal or trusted system-to-system calls.

## EXAMPLE  
A login API allows only five attempts per minute to prevent brute-force attacks.

## PROS & CONS  
Rate limiting improves security, stability, and fair resource usage. However, overly strict limits can block legitimate users and require careful tuning.

## COMMON MISTAKES  
Setting limits too low without considering real traffic is common. Relying only on IP-based limits can be ineffective behind proxies or NATs.
