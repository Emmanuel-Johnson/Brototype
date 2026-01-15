## WHAT

POST data validation is the process of checking and cleaning data sent in a POST request before using or saving it.

---

## WHY

POST data comes directly from users and **cannot be trusted**.  
Without validation, you risk:

- Invalid or inconsistent data  
- Security vulnerabilities  
- Database corruption  

---

## WHERE

Validation is performed using **Django Forms and ModelForms**, **not directly inside views**.

---

## ❌ Wrong Way (Manual, Unsafe)

```python
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')  # no validation
        ContactMessage.objects.create(name=name)
```

Problems:
- No validation  
- No cleaning  
- Easy to introduce bugs and security issues  

---

## ✅ Correct Way (Form Validation)

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

Benefits:
- Centralized validation  
- Clean, reusable logic  
- Secure data handling  

---

## What `is_valid()` Does Internally

When `form.is_valid()` is called, Django:

1. Converts raw POST data into Python data types  
2. Runs built-in and custom **field validators**  
3. Executes `clean_<field>()` methods  
4. Executes `clean()` for cross-field validation  
5. Populates `cleaned_data` **or** `errors`  

---

## Example: Custom Validation

```python
from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Only Gmail allowed")
        return email
```

---

## Validation Failure

```python
form.errors
```

- Automatically available in the template  
- Page is re-rendered with error messages  
- Response returns **200 OK** (no redirect)

---

## Interview One-Liner

**POST data should never be trusted—Django Forms validate, clean, and protect data before it reaches your database.**