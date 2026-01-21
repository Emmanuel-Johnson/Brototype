## 1. WHAT

Serializers are components in Django REST Framework used to convert
complex data like Django models into JSON and back.\
They also validate and transform incoming request data into Python
objects.

## 2. WHY

APIs need a clean way to read and write structured data between client
and server.\
Without serializers, validation, parsing, and data conversion logic
becomes repetitive and hard to maintain.

## 3. WHERE

Serializers sit between views and models in the request--response
cycle.\
They handle input validation before saving to the database and format
output before sending responses.

## 4. HOW

Incoming request data is passed to a serializer for validation.\
If valid, it is converted to Python objects or saved as a model, and
output is serialized to JSON.

## 5. WHEN

Use serializers when building APIs that accept or return structured
data.\
Do not use them for simple template-based Django views that don't expose
APIs.

## 6. EXAMPLE

In a user API, a serializer validates email and username fields.\
It converts the User model instance into JSON for frontend consumption.

## 7. PROS & CONS

They centralize validation, reduce boilerplate, and keep APIs
consistent.\
However, complex serializers can become hard to read and may affect
performance if misused.

## 8. COMMON MISTAKES

Putting business logic inside serializers instead of services or
models.\
Using overly nested serializers without considering query performance.