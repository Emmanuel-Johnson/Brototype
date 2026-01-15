## WHAT

Changing a response status code means explicitly setting the HTTP status on the response object instead of relying on Django’s default behavior.

---

## WHY

Default status codes are not always correct for every situation.  
Explicitly setting status codes improves:

- API correctness  
- Frontend handling  
- Debugging clarity  
- Interview explanations  

---

## WHERE

Status codes are changed inside **views** (FBV, CBV, Generic Views) by passing a `status` argument to the response object.

---

## Function-Based View

```python
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Created", status=201)
```

---

## JsonResponse (Most Common for APIs)

```python
from django.http import JsonResponse

def api_view(request):
    return JsonResponse(
        {"message": "Invalid input"},
        status=400
    )
```

---

## Redirect with Custom Status

```python
from django.shortcuts import redirect

return redirect('contact', permanent=True)  # 301
```

> Default redirect status is **302**

---

## Class-Based View

```python
from django.views import View
from django.http import HttpResponse

class HealthCheckView(View):
    def get(self, request):
        return HttpResponse("OK", status=200)
```

---

## Generic Views (Override When Needed)

### Change success status in `CreateView` (API-style)

```python
from django.views.generic import CreateView
from django.http import HttpResponse

class ContactCreateView(CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'message']

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse("Created", status=201)
```

---

## Common Mistakes (Interview Traps)

- Assuming `redirect()` returns **200** → it returns **302**  
- Forgetting to set status codes in API responses  
- Returning **200 OK** for error cases instead of **4xx**