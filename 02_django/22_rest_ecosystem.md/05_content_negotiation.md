## 1. WHAT

Content negotiation is a mechanism in Django REST Framework used to
decide the format of request and response data.\
It allows an API to serve the same resource as JSON, XML, or other
formats based on the client request.

## 2. WHY

Different clients may require different data formats.\
Without content negotiation, separate endpoints or manual format
handling would be needed, increasing complexity.

## 3. WHERE

Content negotiation occurs in the request--response cycle before
rendering the response.\
It sits between the view logic and the response renderer.

## 4. HOW

The client sends headers like Accept or Content-Type.\
Django REST Framework selects the appropriate parser and renderer to
process the request and format the response.

## 5. WHEN

Use content negotiation when supporting multiple clients or formats from
the same API.\
Do not use it if your API is strictly limited to a single fixed format.

## 6. EXAMPLE

A REST API returns JSON to a web client and XML to an external system.\
The response format is chosen automatically based on the Accept header.

## 7. PROS & CONS

It increases API flexibility, reusability, and client compatibility.\
However, it adds configuration complexity and can make debugging harder.

## 8. COMMON MISTAKES

Misconfiguring renderers or parsers leading to unexpected formats.\
Ignoring client headers and assuming a default response format.