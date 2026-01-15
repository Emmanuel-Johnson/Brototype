# include() in Django

## 1. WHAT
`include()` is a function used to connect one URL configuration file to another, allowing Django to load URL patterns from multiple apps.

## 2. WHY
Without `include()`, all URL patterns would be defined in a single file, making it long, repetitive, and hard to maintain. This approach does not scale well as the project grows.

## 3. WHERE
`include()` is used inside the main or parent `urls.py` file during URL dispatching, before Django resolves the final view in the request–response cycle.

## 4. HOW
First, Django matches a URL prefix in the parent `urls.py`. It then hands off the remaining path to the included app’s `urls.py`, where the final view is resolved.

## 5. WHEN
`include()` should be used when an application has multiple related URLs or when the app is reusable across projects. It is usually unnecessary for very small apps with only one or two routes.

## 6. EXAMPLE
In a project with a blog app, the URL prefix `/blog/` is mapped using `include()` so that all blog-related URLs are managed inside `blog/urls.py`.

## 7. PROS & CONS
`include()` improves modularity, readability, and scalability of URL configurations. However, excessive nesting can make the URL flow harder to trace while debugging.

## 8. COMMON MISTAKES
Common mistakes include forgetting to create the app’s `urls.py` file and misaligning URL prefixes, which can lead to unexpected 404 errors.

<br>
<br>
<br>

## Scenario

A project has multiple apps (blog, shop). Each app manages its own URLs instead of cluttering the main URL configuration.

---

## project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
]
```

---

## blog/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog-list'),
    path('<int:id>/', views.blog_detail, name='blog-detail'),
]
```

---

## blog/views.py

```python
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})
```

---

## How include() works internally

1. Request comes to `/blog/5/`  
2. Django matches `blog/` in the main URL configuration  
3. Remaining path `5/` is passed to `blog.urls`  
4. `<int:id>` matches the value `5`  
5. `blog_detail(request, id=5)` is called and the response is returned