## 1. WHAT

Mixins are reusable Django REST Framework classes used to add specific
API behaviors like list, create, update, or delete.\
They allow developers to compose API views by combining small, focused
pieces of logic.

## 2. WHY

Many APIs repeat the same CRUD-related logic across different views.\
Without mixins, this logic must be rewritten or copied, increasing code
duplication and maintenance effort.

## 3. WHERE

Mixins are used at the view layer, usually combined with
GenericAPIView.\
They sit between HTTP requests and serializers, handling common actions.

## 4. HOW

You combine one or more mixins with GenericAPIView.\
Each mixin provides a method, such as list() or create(), that handles
part of the request flow.

## 5. WHEN

Use mixins when you need fine-grained control over which CRUD operations
a view supports.\
Do not use them when a fully generic view already fits your use case.

## 6. EXAMPLE

A product API uses ListModelMixin and CreateModelMixin to list and add
products.\
This avoids writing separate logic for GET and POST requests.

## 7. PROS & CONS

They promote code reuse, clarity, and flexible API composition.\
However, combining many mixins can reduce readability and make behavior
harder to trace.

## 8. COMMON MISTAKES

Using mixins without understanding which HTTP methods they support.\
Adding unnecessary mixins instead of choosing the appropriate generic
view.