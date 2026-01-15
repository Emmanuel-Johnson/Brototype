# URL Patterns in Django

## 1. WHAT
URL patterns are the configuration used to define how specific URL paths are matched and connected to Django views that handle incoming requests.

## 2. WHY
Without URL patterns, Django would not know which view to execute for a given request. This would force developers to write repetitive path-checking logic inside views, making the code messy and difficult to scale.

## 3. WHERE
URL patterns live in `urls.py` and are part of Django’s URL dispatcher. They are evaluated after middleware processing and before the selected view is executed in the request–response cycle.

## 4. HOW
Django first loads the list of URL patterns from `urls.py`. It then checks each pattern in order against the incoming request path and executes the matched view, passing any captured parameters.

## 5. WHEN
URL patterns should be used whenever a view needs to be accessible through a URL. They should not be used for serving static or media files in production, as that is handled by the web server.

## 6. EXAMPLE
In a blog project, the URL pattern `/posts/<int:id>/` maps to a `post_detail` view, which uses the ID to fetch and display a single blog post.

## 7. PROS & CONS
URL patterns keep request handling clean, readable, and easy to extend while naturally supporting dynamic URLs. However, in large projects, URL files can become complex if patterns are not properly modularized.

## 8. COMMON MISTAKES
Common mistakes include using incorrect path converters, mismatching URL parameters with view arguments, and placing all app URLs directly in the main `urls.py` instead of using `include()`.

<br>
<br>
<br>

## Scenario

A blog app where each post has its own detail page like  
`/posts/10/`.

---

## project/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('blog.urls')),
]
```

---

## blog/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.post_detail, name='post-detail'),
]
```

---

## blog/views.py

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})
```

---

## What happens internally

1. User requests `/posts/10/`  
2. Django matches `posts/` in the main URL configuration  
3. Control is passed to `blog.urls`  
4. `<int:id>` captures the value `10`  
5. `post_detail(request, id=10)` is executed and the response is returned