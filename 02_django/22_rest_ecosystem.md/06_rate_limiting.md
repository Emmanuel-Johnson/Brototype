## 1. WHAT

Rate limiting is a technique used to control how many requests a client
can make to a Django API in a given time period.\
It prevents excessive or abusive API usage.

## 2. WHY

APIs can be overwhelmed by too many requests from a single user or bot.\
Without rate limiting, servers may slow down, crash, or become
vulnerable to abuse.

## 3. WHERE

Rate limiting is applied at the API layer, usually in Django REST
Framework.\
It runs before the view logic processes the request.

## 4. HOW

Each request is tracked per user, IP, or token.\
If the request count exceeds a defined limit, the API returns a
throttling error.

## 5. WHEN

Use rate limiting for public APIs, authentication endpoints, or costly
operations.\
Do not use strict limits for internal or trusted system-to-system APIs.

## 6. EXAMPLE

A login API allows only 5 attempts per minute per IP.\
Further requests are blocked temporarily to prevent brute-force attacks.

## 7. PROS & CONS

It improves security, stability, and fair usage of APIs.\
However, incorrect limits can block legitimate users or affect user
experience.

## 8. COMMON MISTAKES

Setting limits too low without considering real usage patterns.\
Applying the same throttle rules to all endpoints blindly.