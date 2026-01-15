# Django View Arguments – Practical Example

## URL Example

```
/orders/15/
```

---

## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:order_id>/', views.order_detail, name='order-detail'),
]
```

---

## views.py

```python
def order_detail(request, order_id):
    return render(request, 'order_detail.html', {'order_id': order_id})
```

---

## How arguments reach the view

1. Django matches the incoming URL against the URL pattern  
2. `<int:order_id>` captures the value `15`  
3. Django passes the value as `order_id` to the view  
4. `request` is always passed as the **first argument**

---

## Types of view arguments

- `request` → `HttpRequest` object  
- **Path parameters** → values captured from the URL  
- **Keyword arguments** → named parameters from the URL pattern

---

## Key points (Interview-ready)

- Argument names must **match URL parameter names**  
- Order matters for **positional arguments**  
- Path parameters are **already type-cast**  
- View logic depends directly on these arguments