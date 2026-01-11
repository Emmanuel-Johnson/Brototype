"In Python, exceptions are runtime errors that occur while a program is executing. To handle these safely and prevent crashes, Python provides the `try / except / else / finally` construct."

## try block
The `try` block contains code that may raise an exception.

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
```

If any error occurs inside the `try` block, Python immediately stops execution there and looks for a matching `except` block.

## except block
The `except` block handles specific exceptions.

```python
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
```

This allows the program to handle errors gracefully instead of crashing.

### Multiple exceptions
You can catch multiple exceptions together:

```python
except (ZeroDivisionError, ValueError):
    print("Invalid operation")
```

Useful when different exceptions require the same handling logic.

## else block
The `else` block runs only if no exception occurs in the `try` block.

```python
else:
    print("Result:", result)
```

This separates successful-execution logic from error-handling logic, improving readability.

## finally block
The `finally` block always executes, whether an exception occurs or not.

```python
finally:
    print("Execution completed")
```

Commonly used for cleanup operations (closing files, releasing locks, closing DB connections).

## Full example

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid number")
else:
    print("Result:", result)
finally:
    print("Program finished")
```

## Execution flow
- If an exception occurs → matching `except` runs → `finally` runs  
- If no exception occurs → `else` runs → `finally` runs  
- `finally` always executes

## Important interview points
- `else` runs only when no exception occurs  
- `finally` runs in all cases  
- Avoid using bare `except`  
- Catch specific exceptions for better debugging

✅ Strong interview closing line  
"So `try` contains risky code, `except` handles errors, `else` runs on success, and `finally` guarantees cleanup — together they make Python programs reliable and production-ready."
