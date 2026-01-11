# Keyword Argument Validation

This function checks for an invalid keyword argument named `err` and raises an error if it is found.

```python
def validate_kwargs(**kwargs):
    if 'err' in kwargs:
        raise ValueError("Keyword argument 'err' is not allowed")
