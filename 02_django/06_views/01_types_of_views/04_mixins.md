## 1. WHAT
Mixins are reusable classes used to add specific functionality to Django class-based views without rewriting the same code.

## 2. WHY
Mixins solve the problem of repeated logic across multiple views, such as authentication or permission checks. Without them, the same logic would need to be duplicated in many views.

## 3. WHERE
Mixins are used in the view layer alongside class-based views. They participate in request handling before or during the view’s main logic.

## 4. HOW
A mixin class defines reusable behavior, and the view inherits from the mixin along with a base view class. Django then executes the mixin’s methods as part of the request flow.

## 5. WHEN
Mixins should be used when multiple views share common behavior. They are not suitable for large or tightly coupled business logic.

## 6. EXAMPLE
In an admin panel, `LoginRequiredMixin` is added to a view to restrict access to authenticated users only.

## 7. PROS & CONS
Mixins promote code reuse, cleaner views, and better separation of concerns. However, using many mixins can make the method resolution order harder to understand.

## 8. COMMON MISTAKES
Common mistakes include using an incorrect mixin order and choosing mixins when simple helper functions would be clearer.

<br>
<br>
<br>

## Practical Example (Login Required)

### Without Mixin (bad & repetitive)

```python
class DashboardView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        return render(request, 'dashboard.html')
```

---

### With Mixin (clean)

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
```

---

## Mixin + Generic View (Real‑world Pattern)

**Only logged‑in users can submit contact messages**

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import ContactMessage

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'message']
    template_name = 'contact.html'
    success_url = '/contact/'
```

---

## Common Built‑in Mixins (Must‑know)

- `LoginRequiredMixin` → user must be logged in  
- `PermissionRequiredMixin` → permission‑based access  
- `UserPassesTestMixin` → custom access condition  
- `SuccessMessageMixin` → flash success messages  

---

## Order Matters (INTERVIEW TRAP)

```python
class MyView(LoginRequiredMixin, CreateView):
    ...
```

✅ **Mixins must come before the view class**, or they will not work correctly.

---

## Mental Model

- **Views** define *what page this is*  
- **Mixins** define *who can access it* and *extra behavior*