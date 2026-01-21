## 1. WHAT

Validators in the Django REST ecosystem are rules used to verify API
input data before it is accepted or saved.\
They ensure incoming request data follows expected formats, limits, and
business constraints.

## 2. WHY

APIs receive untrusted input from clients, which can be invalid or
inconsistent.\
Without validators, validation logic gets duplicated across views and
serializers, increasing errors.

## 3. WHERE

Validators live inside Django REST Framework serializers and model
fields.\
They run during request validation, before data is saved or a response
is returned.

## 4. HOW

Request data is passed to a serializer.\
The serializer runs field-level and object-level validators, raising
errors if rules fail.

## 5. WHEN

Use validators for reusable, rule-based API checks like value ranges or
formats.\
Do not use them for long-running processes or complex multi-model
workflows.

## 6. EXAMPLE

A registration API uses a validator to ensure password length and
strength.\
Another validator ensures a product price is greater than zero before
saving.

## 7. PROS & CONS

They improve API reliability, consistency, and security with minimal
code.\
However, overusing validators can make serializers harder to read and
maintain.

## 8. COMMON MISTAKES

Placing heavy database logic inside validators.\
Using validators instead of object-level validation for cross-field
checks.