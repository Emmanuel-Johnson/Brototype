In Python exception handling, the `else` block defines code that should run only if no exception occurs in the `try` block. It separates normal execution logic from error-handling logic, improving readability and maintainability.

## Why `else` exists
Without `else`, success logic often gets mixed inside the `try` block, reducing clarity. The `else` block expresses what should happen when everything goes right.

## Basic syntax
```py
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)
```
In this example, the `else` block executes only if the conversion to integer succeeds.

## Execution flow
- If an exception occurs → matching `except` runs → `else` is skipped.  
- If no exception occurs → `else` runs.  
- `else` never runs if an exception happens.

## `else` vs code inside `try`
Place only code that may fail inside `try`; put success logic in `else` for clarity.

Less clean:
```py
try:
    num = int("10")
    print(num)
except ValueError:
    print("Error")
```

Cleaner:
```py
try:
    num = int("10")
except ValueError:
    print("Error")
else:
    print(num)
```

This separation expresses intent more clearly.

## Using `else` with multiple exceptions
```py
try:
    x = int(input())
    result = 10 / x
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
```
`else` runs only if both operations succeed.

## `else` with `finally`
The `else` block runs only on success, while `finally` runs no matter what.
```py
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())
finally:
    # Ensure file exists before closing in real code; consider using `with` instead.
    try:
        file.close()
    except UnboundLocalError:
        pass
```
Use `finally` (or `with`) for reliable resource cleanup.

## When to use `else`
- To separate risky code from safe code  
- When success logic should not be inside `try`  
- To write cleaner, more maintainable code

## Common interview traps
- ❌ Thinking `else` runs after `except` — it doesn't.  
- ❌ Using `else` when it’s not needed.  
- ❌ Putting risky code inside `else`.

> “In Python exception handling, `else` clearly expresses successful execution by running only when no exception occurs, improving readability and maintainability.”
