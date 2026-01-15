## WHAT

Returning HTTP status codes means sending a response with a numeric code that tells the client whether a request succeeded, failed, or needs further action.

---

## WHY

Without proper status codes, clients (browsers, APIs, frontend apps) can’t reliably understand what happened.  
Status codes enable clear communication, easier debugging, and correct frontend behavior.

---

## WHERE

Status codes are returned from **views** (FBVs, CBVs, Generic Views) using Django response classes like:

- `HttpResponse`
- `JsonResponse`
- Helpers like `get_object_or_404()`

---

## Basic example (FBV)

```python
from django.http import HttpResponse

def simple_view(request):
    return HttpResponse("OK", status=200)
```

---

## Common Practical Cases

### 1. Form submitted successfully

```python
return redirect('contact')   # returns HTTP 302 (Redirect)
```

---

### 2. Bad request / validation failure

```python
from django.http import HttpResponseBadRequest

return HttpResponseBadRequest("Invalid data")  # 400
```

---

### 3. Object not found

```python
from django.shortcuts import get_object_or_404

obj = get_object_or_404(ContactMessage, id=1)  # returns 404 automatically
```

---

### 4. Forbidden access

```python
from django.http import HttpResponseForbidden

return HttpResponseForbidden("Not allowed")  # 403
```

---

### 5. JSON / API response

```python
from django.http import JsonResponse

return JsonResponse(
    {"message": "Created"},
    status=201
)
```

---

## CBV Example

```python
from django.views import View
from django.http import HttpResponse

class PingView(View):
    def get(self, request):
        return HttpResponse("pong", status=200)
```

---

## Generic Views (Handled for You)

- `CreateView` → **302 Redirect** after success  
- `DeleteView` → **302 Redirect**  
- `DetailView` → **200 OK**  
- `get_object_or_404()` → **404 Not Found** automatically  

---

## Interview Cheat-Sheet

- **200** → OK  
- **201** → Created  
- **302** → Redirect  
- **400** → Bad Request  
- **403** → Forbidden  
- **404** → Not Found  
- **500** → Server Error