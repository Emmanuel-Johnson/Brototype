# reverse() in Django

## 1. WHAT
`reverse()` is a function used to generate a URL from a named URL pattern instead of hard-coding the path.

## 2. WHY
Hard-coding URLs makes code fragile when paths change. Without `reverse()`, URLs must be updated in multiple places, which is repetitive, error-prone, and difficult to maintain.

## 3. WHERE
`reverse()` is used in views, models, signals, and other backend logic. It works during response preparation, before Django sends the final response to the client.

## 4. HOW
Django looks up the URL pattern by its name, fills in any required parameters, and then returns the resolved URL as a string.

## 5. WHEN
`reverse()` should be used whenever URLs need to be generated dynamically in Python code. It should not be used inside templates, where the `{% url %}` template tag is preferred.

## 6. EXAMPLE
After creating an order, a view uses  
`reverse('order_detail', args=[order.id])`  
to redirect the user to the order detail page.

## 7. PROS & CONS
`reverse()` improves maintainability, prevents broken links, and keeps URLs consistent across the application. However, incorrect URL names or missing parameters can cause runtime errors.

## 8. COMMON MISTAKES
Common mistakes include forgetting to name URL patterns and passing arguments that do not match the URL definition.

<br>
<br>
<br>

## Scenario

After creating an order, the user should be redirected to  
`/orders/12/` **without hard-coding the URL**.

---

## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:id>/', views.order_detail, name='order_detail'),
]
```

---

## views.py (create order)

```python
from django.shortcuts import redirect
from django.urls import reverse
from .models import Order

def create_order(request):
    order = Order.objects.create(user=request.user)

    url = reverse('order_detail', args=[order.id])
    return redirect(url)
```

---

## views.py (target view)

```python
from django.shortcuts import render
from .models import Order

def order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'order_detail.html', {'order': order})
```

---

## What happens internally

1. Order is created → `order.id = 12`  
2. `reverse('order_detail', args=[12])` is called  
3. Django looks up the URL pattern named `order_detail`  
4. Django generates the URL `/orders/12/`  
5. User is redirected to the correct order detail page

<br>
<br>
<br>

# reverse_lazy() in Django

## 1. WHAT
`reverse_lazy()` is a function used to generate a URL from a named URL pattern, but it delays the actual URL resolution until the value is accessed.

## 2. WHY
`reverse()` resolves URLs immediately, which can fail when URL configurations are not fully loaded yet. Without `reverse_lazy()`, import-time errors can occur in class-based views or settings files.

## 3. WHERE
`reverse_lazy()` is commonly used in class-based views, decorators, and settings files. It is evaluated during configuration or class loading, before the request–response cycle begins.

## 4. HOW
Django stores the URL name and parameters without resolving them at first. When the value is accessed at runtime, Django resolves it into the final URL string.

## 5. WHEN
`reverse_lazy()` should be used when URLs are required at import time, such as `success_url` in class-based views. It should not be used when an immediate URL string is needed inside a function-based view.

## 6. EXAMPLE
In a `CreateView`,  
`success_url = reverse_lazy('product_list')`  
ensures the redirect URL is resolved only after the application is fully loaded.

## 7. PROS & CONS
`reverse_lazy()` prevents circular import issues, works well with class-based views, and improves startup safety. However, it delays error detection and can be confusing if an immediate URL string is expected.

## 8. COMMON MISTAKES
Common mistakes include using `reverse_lazy()` unnecessarily in normal views and forgetting that resolution errors appear only at runtime instead of at import time.

<br>
<br>
<br>

## Scenario

After successfully creating a product using a **class-based view**, the user should be redirected to the product list page.

---

## urls.py

```python
from django.urls import path
from .views import ProductCreateView, ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductCreateView.as_view(), name='product_add'),
]
```

---

## views.py

```python
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
```

---

## Why reverse_lazy() is required here

- `success_url` is evaluated **when the class is loaded**
- `reverse()` would try to resolve the URL **too early**
- `reverse_lazy()` delays URL resolution until **runtime**, after URL configs are ready

---

## What happens internally

1. Django loads the class definition  
2. `reverse_lazy('product_list')` is stored as a lazy object  
3. Form is submitted successfully  
4. Django resolves the URL  
5. User is redirected to `/products/`