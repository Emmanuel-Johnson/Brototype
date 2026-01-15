## WHAT

A redirect is an HTTP response that tells the browser  
**“this resource lives at another URL”**, instructing it to make a **new request** to that URL.

---

## WHY

Redirects are used to:

- Prevent duplicate form submissions  
- Enforce clean and consistent URLs  
- Guide users after actions like **login, logout, or form submission**

---

## WHERE

Redirects are returned from **views** (FBVs, CBVs, Generic Views) using:

- `redirect()`  
- `HttpResponseRedirect`  

---

## Basic Redirect (Most Common)

```python
from django.shortcuts import redirect

return redirect('contact')
```

- Uses **URL name**, not hardcoded path  
- Internally uses `reverse()`  
- Returns **HTTP 302** by default  

---

## Redirect to a Hardcoded Path

```python
return redirect('/contact/')
```

⚠️ Works, but **not recommended** — breaks if URLs change.

---

## Permanent Redirect

```python
return redirect('home', permanent=True)
```

- Returns **HTTP 301**  
- Cached by browsers → use carefully  

---

## Redirect with Data (POST → GET Pattern)

```python
def contact_view(request):
    if request.method == "POST":
        # save data
        return redirect('contact')  # avoids resubmission
```

This is the classic **PRG pattern (Post / Redirect / Get)**.

---

## CBV Example

```python
from django.views import View
from django.shortcuts import redirect

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')
```

---

## Generic Views (Automatic Redirects)

- `CreateView`, `UpdateView`, `DeleteView`  
- Redirect after success using `success_url`

```python
class ContactCreateView(CreateView):
    success_url = '/contact/'
```

---

## Redirect vs Render (INTERVIEW FAVORITE)

- `render()` → returns **200**, same request  
- `redirect()` → returns **302**, new request