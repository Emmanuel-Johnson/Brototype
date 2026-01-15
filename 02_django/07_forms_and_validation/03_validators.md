## WHAT
Validators are callable functions or classes that check whether a field’s value meets specific rules and raise an error if it doesn’t.

## WHY
Hard-coding validation logic inside views leads to duplication and poor reuse. Validators centralize rules, improve reuse, and enforce data integrity.

## WHERE
Validators are mainly used in models and forms, and run automatically during form validation and model saving.

## Built-in Validators (Examples)
```python
from django.core.validators import MinValueValidator, MaxValueValidator

age = models.IntegerField(
    validators=[MinValueValidator(18), MaxValueValidator(60)]
)
```

Common built-ins:
- EmailValidator
- URLValidator
- RegexValidator
- MinLengthValidator
- MaxLengthValidator

## Custom Validator (Function)
```python
from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError("Value must be even")

age = models.IntegerField(validators=[validate_even])
```

## Validator in Forms
```python
from django import forms
from django.core.validators import MinLengthValidator

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        validators=[MinLengthValidator(3)]
    )
```

## When Validators Run
- During form.is_valid()
- During model.full_clean()
- Automatically when using ModelForm

## Validators vs clean Methods
- Validators → single-field, reusable rules
- clean_<field>() → field logic needing context
- clean() → cross-field validation

## Interview One-Liner
Validators are reusable, field-level rules that enforce data integrity at the form and model level.