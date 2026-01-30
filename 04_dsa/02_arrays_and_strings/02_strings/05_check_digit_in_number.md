```python
number = 12345
digit = 8

def check_number_contains_digit(number, digit):
    while number:
        if digit == number % 10:
            return True
        number //= 10
    return False
    
print(check_number_contains_digit(number, digit))
```