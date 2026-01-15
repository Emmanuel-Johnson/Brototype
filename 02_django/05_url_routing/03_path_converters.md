# Path Converters in Django

## 1. WHAT
Path converters are a feature used to capture and type-cast dynamic values from a URL and pass them directly to a Django view.

## 2. WHY
Without path converters, all URL parameters would arrive as plain strings. This forces repetitive validation and manual type conversion inside views, increasing boilerplate code and the risk of errors.

## 3. WHERE
Path converters are defined inside URL patterns in `urls.py`. They operate during URL matching, before the request reaches the view function.

## 4. HOW
Django matches the incoming URL against a pattern containing a converter, validates the URL segment, converts it to the specified type, and then passes it as an argument to the view.

## 5. WHEN
Path converters should be used when URLs include dynamic values such as IDs, slugs, or UUIDs. They should not be used when the value does not affect routing or is better handled through query parameters.

## 6. EXAMPLE
In a product app, the URL `/products/<int:id>/` uses the `int` converter to ensure only numeric IDs are passed to the `product_detail` view.

## 7. PROS & CONS
Path converters simplify validation, improve URL readability, and reduce logic inside views. However, they are limited to predefined patterns and may reject valid requests if the converter is too strict.

## 8. COMMON MISTAKES
Common mistakes include using the wrong converter type and mismatching the parameter name between the URL pattern and the view function.

<br>
<br>
<br>

## Scenario

A product detail page where only numeric product IDs are allowed.

---

## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:id>/', views.product_detail, name='product-detail'),
]
```

---

## views.py

```python
from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})
```

---

## What the path converter does

1. User requests `/products/25/`  
2. `<int:id>` ensures the value `25` is numeric  
3. Django converts `"25"` into integer `25`  
4. `product_detail(request, id=25)` is executed  
5. Invalid URLs like `/products/abc/` fail URL matching and return **404 automatically**