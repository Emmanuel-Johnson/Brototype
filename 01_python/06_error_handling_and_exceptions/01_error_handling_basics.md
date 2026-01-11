In Python, error handling is the process of managing runtime errors so a program doesn’t crash unexpectedly and can respond gracefully to problems.

Python uses exceptions to represent errors. When something goes wrong — like dividing by zero or accessing a missing file — Python raises an exception object.

## Why error handling matters
- Prevent crashes
- Show meaningful error messages
- Recover or continue execution
- Write more robust and production-ready code

## Basic try–except block
The core mechanism is the `try` / `except` block.

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
```

Here, Python executes the `try` block. If an exception occurs, control jumps to the matching `except` block, preventing the program from crashing.

## Catching multiple exceptions
You can catch different exceptions separately or together.

```python
try:
    # some code that may raise ValueError or ZeroDivisionError
    ...
except (ValueError, ZeroDivisionError):
    print("Invalid operation")
```

This is useful when multiple errors require the same handling.

## The else block
The `else` block runs only if no exception occurs.

```python
try:
    num = int("10")
except ValueError:
    print("Error")
else:
    print("Conversion successful")
```

This helps separate normal logic from error-handling logic.

## The finally block
The `finally` block always executes, whether an exception occurs or not.

```python
try:
    file = open("data.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing resources")
    file.close()
```

`finally` is commonly used for cleanup operations like closing files or database connections.

## Raising exceptions manually
You can raise exceptions using the `raise` keyword.

```python
def withdraw(amount):
    if amount < 0:
        raise ValueError("Amount must be positive")
```

This enforces business rules and validates input.

## Custom exceptions
For larger applications, define custom exception classes.

```python
class InsufficientBalanceError(Exception):
    pass
```

Custom exceptions improve readability and make handling more specific.

## Best practices
- Catch specific exceptions; avoid bare `except`
- Avoid swallowing errors silently
- Use `finally` (or context managers) for cleanup
- Raise meaningful error messages

## Summary
Python error handling uses exceptions with `try`, `except`, `else`, `finally`, and `raise` to build fault-tolerant and maintainable applications.
