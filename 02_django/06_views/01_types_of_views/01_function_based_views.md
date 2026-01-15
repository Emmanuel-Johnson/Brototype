## 1. WHAT
Function-Based Views are a way to write Django views as plain Python functions that handle an HTTP request and return an HTTP response.

## 2. WHY
They provide a simple and direct way to implement request logic. Without function-based views, even very simple request–response handling would require more complex abstractions.

## 3. WHERE
Function-based views live in the view layer of Django’s MVT architecture. After URL routing resolves a request, it is passed directly to the mapped function for processing.

## 4. HOW
A URL pattern maps to a function-based view. The function receives the request object, performs logic such as handling GET or POST data, and returns an HTTP response.

## 5. WHEN
Function-based views should be used for simple pages, custom workflows, or when fine-grained control is required. They are less suitable for repetitive CRUD patterns where class-based views reduce boilerplate.

## 6. EXAMPLE
In a contact page, a function-based view handles a GET request to display the form and a POST request to process and save the submitted user message.

## 7. PROS & CONS
Function-based views are easy to read, quick to write, and highly flexible. However, as complexity grows, they can become repetitive and harder to maintain.

## 8. COMMON MISTAKES
Common mistakes include placing too much business logic inside the view and failing to properly handle different HTTP methods.

<br>
<br>
<br>

## Scenario

A contact page that:

- Shows a form on **GET**
- Processes and saves data on **POST**

---

## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
]
```

---

## views.py

```python
from django.shortcuts import render, redirect
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect('contact')

    return render(request, 'contact.html')
```

---

## contact.html

```html
<form method="POST">
    {% csrf_token %}
    <input type="text" name="name">
    <input type="email" name="email">
    <textarea name="message"></textarea>
    <button type="submit">Send</button>
</form>
```

---

## What this shows clearly

- Plain **Python function** used as a Django view  
- `request` is always the **first argument**  
- Manual handling of **GET vs POST** logic  
- Full control over request processing and response