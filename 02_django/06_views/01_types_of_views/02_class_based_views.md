## 1. WHAT
Class-Based Views are a way to build Django views using Python classes, organizing request-handling logic into reusable and structured components.

## 2. WHY
CBVs reduce repetition when handling common patterns such as CRUD operations. Without them, similar logic would need to be rewritten across multiple function-based views.

## 3. WHERE
Class-based views live in the view layer of Django’s MVT architecture. After URL routing, Django instantiates the class and processes the request through it.

## 4. HOW
A URL is mapped to a CBV using `as_view()`. Django then routes the request to the appropriate class method, such as `get()` or `post()`, and returns the response.

## 5. WHEN
CBVs should be used for standard patterns like list, create, update, or delete views. They are less suitable for very simple or highly custom logic where function-based views are clearer.

## 6. EXAMPLE
In an LMS project, a `CourseListView` CBV displays all courses using Django’s built-in `ListView`.

## 7. PROS & CONS
CBVs encourage reuse, cleaner structure, and faster development through generic views. However, they can be harder to understand initially, and excessive abstraction may hide important logic.

## 8. COMMON MISTAKES
Common mistakes include misunderstanding the CBV method flow and overusing CBVs when a simple function-based view would be more readable.

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
from .views import ContactView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]
```

---

## views.py

```python
from django.views import View
from django.shortcuts import render, redirect
from .models import ContactMessage

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect('contact')
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

## What this shows clearly (CBV)

- View logic is organized inside a **class**, not a function  
- HTTP methods are cleanly separated into `get()` and `post()`  
- `request` is still explicitly available  
- Cleaner structure as logic grows  
- Easy to extend later using **mixins, inheritance, authentication**, etc.