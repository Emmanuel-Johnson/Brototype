# Django Query Parameters – Practical Example

## URL Example

```
/products/?category=shoes&page=2
```

---

## views.py

```python
def product_list(request):
    category = request.GET.get('category')
    page = request.GET.get('page', 1)   # default value

    return render(request, 'products.html', {
        'category': category,
        'page': page
    })
```

---

## How it works

1. Browser sends a **GET request** with query parameters  
2. Django collects query parameters inside `request.GET`  
3. `request.GET` behaves like a dictionary  
4. All values retrieved from `request.GET` are **strings**

---

## Key points (Interview-ready)

- Query parameters are accessed using `request.GET`  
- They are **optional** and do **not affect URL routing**  
- Commonly used for **filtering, searching, and pagination**  
- **Not suitable for sensitive data**

<br>
<br>
<br>


# Django Path Parameters – Practical Example

## URL Example

```
/users/42/
```

---

## urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>/', views.user_detail, name='user-detail'),
]
```

---

## views.py

```python
def user_detail(request, user_id):
    # user_id is already an integer
    return render(request, 'user_detail.html', {'user_id': user_id})
```

---

## How it works

1. Django matches the incoming URL against defined URL patterns  
2. `<int:user_id>` captures the value `42` from the URL  
3. Django automatically converts it to an integer  
4. The value is passed directly to the view as `user_id`

---

## Key points (Interview-ready)

- Path parameters are part of the **URL structure**  
- They are accessed via **view function arguments**  
- Automatically **type-cast** using path converters  
- They **affect URL routing**