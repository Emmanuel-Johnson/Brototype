## 1. WHAT

Generic API views are pre-built Django REST Framework views used to
handle common CRUD operations with minimal code.\
They combine generic logic with serializers and querysets to quickly
build APIs.

## 2. WHY

Most APIs repeat the same patterns for listing, creating, retrieving,
updating, and deleting data.\
Without generic views, developers must write similar boilerplate logic
in every API view.

## 3. WHERE

Generic API views sit at the view layer of the Django REST
request--response cycle.\
They connect incoming HTTP requests to serializers and database
querysets.

## 4. HOW

You define a queryset and a serializer class.\
The generic view handles request parsing, validation, database
operations, and response formatting automatically.

## 5. WHEN

Use generic API views for standard CRUD-based APIs with predictable
behavior.\
Do not use them when the API flow is highly customized or non-standard.

## 6. EXAMPLE

A ListCreateAPIView is used to list all products and create a new
product.\
A RetrieveUpdateDestroyAPIView handles view, update, and delete for a
single product.

## 7. PROS & CONS

They reduce boilerplate, speed up development, and follow REST best
practices.\
However, they can hide logic and become restrictive for complex
workflows.

## 8. COMMON MISTAKES

Overriding too many methods instead of switching to a custom APIView.\
Not understanding default behaviors like permissions, pagination, or
filtering.