# URL Routing in Django

## 1. WHAT
URL routing is the mechanism used to map an incoming URL to a specific Django view that handles the request and returns a response.

## 2. WHY
Without URL routing, handling requests would require large conditional blocks that manually check request paths. This quickly becomes repetitive, error-prone, and hard to maintain as the application grows.

## 3. WHERE
URL routing sits early in Django’s request–response cycle, after middleware processing and before the view logic. Django’s URL dispatcher determines which view should handle the request.

## 4. HOW
Django reads the URL patterns defined in `urls.py`, matches the incoming request path against those patterns, and then calls the mapped view while passing any captured parameters.

## 5. WHEN
URL routing is used for every web request that requires structured handling by Django.

## 6. EXAMPLE
In an e-commerce project, the URL `/products/42/` is routed to a `product_detail` view, which receives `42` as the product ID and returns the corresponding product page.

## 7. PROS & CONS
URL routing keeps request handling clean, readable, and scalable while supporting dynamic URLs easily. However, poorly organized URL files can become difficult to manage, and incorrect patterns may cause routing conflicts.

## 8. COMMON MISTAKES
Common mistakes include forgetting trailing slashes or mismatching URL parameters with view arguments, which can result in 404 errors or runtime exceptions.

<br>
<br>
<br>

## Scenario

User opens a product detail page like  
`/products/42/` → Django routes it to a view → product with ID **42** is shown.

---

## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/', views.product_detail, name='product-detail'),
]
```

---

## views.py

```python
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
```

---

## What happens step-by-step

1. Browser requests `/products/42/`  
2. Django checks `urls.py`  
3. `<int:product_id>` matches the value `42`  
4. Django calls `product_detail(request, product_id=42)`  
5. View fetches the product and returns the rendered page