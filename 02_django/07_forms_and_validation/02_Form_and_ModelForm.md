# Django Form 

## WHAT

A **Form** in Django is a Python class used to **collect, validate, and clean user input** coming from an HTTP request.

---

## WHY

Directly using `request.POST` mixes validation logic with view logic and easily leads to bugs.  
Django Forms provide:

- Built-in validation  
- Clean error messages  
- Sanitized data (`cleaned_data`)  
- Better security and maintainability  

---

## WHERE

Forms sit **between the template and the view** and are used in:

- Function-Based Views (FBVs)  
- Class-Based Views (CBVs)  
- Generic Views  

Whenever user input is involved, forms should be used.

---

## Basic Form (`forms.Form`)

Used when data is **not tied to a database model**.

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

---

## Using Form in a View

```python
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

---

## Template Usage

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
```

---

## Key Internals (Interview Gold)

- `is_valid()` → runs validation  
- `cleaned_data` → sanitized Python data  
- `errors` → validation error messages  
- `clean_<field>()` → field-level validation  
- `clean()` → form-wide validation  

---

## Form vs ModelForm

- **Form** → manual saving, more control  
- **ModelForm** → auto-save to DB, less boilerplate code

<br>
<br>
<br>

# Django ModelForm

## WHAT

A **ModelForm** is a Django form class that is automatically generated from a model, mapping form fields directly to model fields.

---

## WHY

Writing forms and save logic separately for models causes duplication and inconsistencies.  
ModelForms:

- Remove boilerplate code  
- Ensure validation matches model constraints  
- Simplify CRUD operations  

---

## WHERE

ModelForms are used in **views** (FBVs, CBVs, Generic Views) whenever user input directly **creates or updates database objects**.

---

## Basic ModelForm

```python
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
```

---

## Using ModelForm in a Function-Based View (FBV)

```python
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

---

## How Saving Works (Important)

```python
obj = form.save(commit=False)
obj.source = "website"
obj.save()
```

- `commit=False` creates the object **without saving to the database**
- Useful when you need to modify the instance before saving

---

## Validation Flow

- **Field validation** → model field rules (max_length, null, blank, etc.)  
- `clean_<field>()` → custom field-level validation  
- `clean()` → cross-field validation  

---

## ModelForm vs Form (Interview Favorite)

- **Form** → full control, manual save logic  
- **ModelForm** → faster CRUD, less code, consistent validation  

---

## Generic View Shortcut

```python
from django.views.generic import CreateView

class ContactCreateView(CreateView):
    model = ContactMessage
    fields = ['name', 'email', 'message']
```

Django internally **creates a ModelForm for you**.