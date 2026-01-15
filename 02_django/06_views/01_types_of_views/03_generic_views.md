## 1. WHAT
Generic Views are a set of pre-built Django class-based views used to handle common tasks such as displaying lists, detail pages, and basic CRUD operations.

## 2. WHY
Generic views eliminate the need to repeatedly write the same logic for common patterns. Without them, developers must manually implement similar code for listing, creating, or editing data.

## 3. WHERE
Generic views are part of Django’s view layer and are built on top of class-based views. After URL routing, the generic view processes the request using Django’s built-in behavior.

## 4. HOW
A suitable generic view such as `ListView` or `CreateView` is selected and configured with a model or queryset. Django then automatically handles the request and returns the response.

## 5. WHEN
Generic views should be used for standard CRUD-based pages with minimal custom logic. They are not ideal when the request flow or business logic is highly customized.

## 6. EXAMPLE
In a blog application, a `PostListView` extends `ListView` to display all blog posts without writing custom query or rendering logic.

## 7. PROS & CONS
Generic views speed up development, reduce boilerplate code, and encourage consistency. However, heavy customization can make them harder to understand and debug.

## 8. COMMON MISTAKES
Common mistakes include not understanding the default behavior of generic views and forcing complex business logic into them instead of using custom views.

<br>
<br>
<br>

## Scenario

Same contact page implemented using a **Generic View** instead of manually handling `get()` and `post()`.

Django provides `CreateView` to handle common form patterns automatically.

---

## urls.py

```python
from django.urls import path
from .views import ContactCreateView

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
]
```

---

## views.py

```python
from django.views.generic import CreateView
from .models import ContactMessage

class ContactCreateView(CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'message']
    template_name = 'contact.html'
    success_url = '/contact/'
```

---

## contact.html

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
```

---

## What Django is doing for you

- Automatically handles **GET** → displays the form  
- Automatically handles **POST** → validates and saves data  
- Automatically creates a **ModelForm** from the model  
- Automatically calls `form.save()`  
- Redirects after success using `success_url`

---

## Common Generic Views (Interview must-know)

- `ListView` → list of objects  
- `DetailView` → single object  
- `CreateView` → create form  
- `UpdateView` → edit form  
- `DeleteView` → delete confirmation