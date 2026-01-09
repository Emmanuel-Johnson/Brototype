A decorator is a function that modifies another function’s behavior without changing its source code. They work because functions are first-class objects (you can pass them as arguments and return them). Decorators wrap a function, add logic before/after execution, and return the modified function.

---

## 1. Basic decorator

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
```

What happens:
- `say_hello` is passed to `my_decorator`
- `wrapper()` runs instead of the original function
- the original function still executes inside the wrapper

---

## 2. Decorator with arguments

```python
def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi")

greet()
```

Explanation:
- `repeat(3)` returns a decorator
- that decorator wraps `greet`
- the function runs 3 times

---

## 3. Decorator that accepts any function arguments

```python
def log_args(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    return a + b

print(add(2, 3))
```

Why this matters:
- Makes the decorator generic
- Works for any function signature
- Common in logging, authentication, validation

---

## 4. Decorator to handle ZeroDivisionError

```python
def handle_zero_division(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Cannot divide by zero"
    return wrapper

@handle_zero_division
def divide(a, b):
    return a / b

print(divide(10, 0))
```

Interview tip:
- Demonstrates exception handling outside business logic

---

## 5. Decorator to convert string return value to lowercase

```python
def to_lowercase(func):
    def wrapper():
        result = func()
        return result.lower()
    return wrapper

@to_lowercase
def get_text():
    return "HELLO WORLD"

print(get_text())
```

Key point:
- Decorator modifies the return value (useful for formatting/sanitization)

---

## 6. Decorator to prepend a string

```python
def prepend_string(prefix):
    def decorator(func):
        def wrapper():
            return prefix + func()
        return wrapper
    return decorator

@prepend_string("Hello ")
def name():
    return "Python"

print(name())
```

What this shows:
- Decorator with arguments
- Return value modification
- Common in response formatting

---

### One-line summary
Decorators in Python wrap functions to extend or modify behavior without changing the original code. They rely on closures and are widely used for logging, authentication, validation, and error handling.
