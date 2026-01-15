## WHAT

Checking the request method means inspecting `request.method` to know which HTTP action  
(GET, POST, PUT, DELETE, etc.) the client is performing.

---

## WHY

Different HTTP methods represent different intentions.  
Without checking the method, you can’t safely separate **reading data (GET)** from  
**changing data (POST)**, which leads to messy logic and security issues.

---

## WHERE

- Mainly done in **Function-Based Views (FBVs)**  
- Also used in low-level **Class-Based Views (CBVs)**  
- In **Generic Views**, Django handles method checking internally

---

## Function-Based View (Manual Check)

```python
def contact_view(request):
    if request.method == "POST":
        # process form
        ...
        return redirect('contact')

    # GET request
    return render(request, 'contact.html')
```

**Explanation**
- Developer manually checks `request.method`
- Same function handles both GET and POST
- Becomes harder to manage as logic grows

---

## Class-Based View (Method-Based Dispatch)

```python
from django.views import View

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        # process form
        return redirect('contact')
```

**Django internally**
- Reads `request.method`
- Calls `get()` for GET requests
- Calls `post()` for POST requests

Cleaner separation than FBVs.

---

## Generic Views (No Manual Checking)

```python
from django.views.generic import CreateView

class ContactCreateView(CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'message']
```

**Here, Django automatically**
- Routes **GET** → displays the form  
- Routes **POST** → validates and saves data  
- Calls the correct internal method automatically

---

## Interview Mental Model

- **FBV** → You manually check `request.method`  
- **CBV** → Django dispatches requests to methods  
- **Generic Views** → Django handles the entire flow