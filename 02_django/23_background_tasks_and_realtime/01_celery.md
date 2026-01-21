# Celery in Django

## 1. WHAT

Celery is an asynchronous task queue used to run background jobs outside
the main Django request--response cycle.\
It helps Django handle long-running or delayed tasks without blocking
user requests.

## 2. WHY

Without Celery, slow tasks like emails, reports, or API calls block
requests and degrade performance.\
Handling retries, scheduling, and parallel execution manually becomes
complex and error-prone.

## 3. WHERE

Celery sits beside Django, not inside the request thread.\
Flow is typically: Client → Django → message broker → Celery worker →
result backend (optional).

## 4. HOW

Django sends a task message to a broker like Redis or RabbitMQ.\
Celery workers listen to the broker, execute the task asynchronously,
and optionally store results.

## 5. WHEN

Use Celery for background, time-consuming, or retry-based tasks.\
Do not use it for tasks that must finish immediately within a single
HTTP request.

## 6. EXAMPLE

When a user signs up, Django responds instantly.\
Celery sends the welcome email and processes post-signup logic in the
background.

## 7. PROS & CONS

It improves performance, scalability, and reliability of background
work.\
However, it adds infrastructure complexity and requires broker and
worker management.

## 8. COMMON MISTAKES

Using Celery for simple synchronous logic that doesn't need async
execution.\
Running tasks that depend on request-specific state like sessions or
open DB transactions.