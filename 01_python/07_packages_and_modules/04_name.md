## What is `__name__` in Python?

In Python, `__name__` is a special built-in variable that tells us how a Python file is being executed — whether it is run directly or imported as a module.

---

## What `__name__` Represents

Every Python file has a `__name__` variable.

- If the file is run directly, `__name__` is set to `"__main__"`  
- If the file is imported, `__name__` is set to the module’s name  

---

## Basic Example

```python
# file1.py
print(__name__)
```

If we run `file1.py` directly, the output is:

```
__main__
```

If we import it from another file, the output becomes:

```
file1
```

---

## Why `__name__ == "__main__"` Is Important

The most common use of `__name__` is the **main guard**.

```python
if __name__ == "__main__":
    main()
```

This ensures that certain code runs **only when the file is executed directly**, and not when it’s imported.

---

## Real-World Example

```python
# calculator.py
def add(a, b):
    return a + b

def main():
    print(add(2, 3))

if __name__ == "__main__":
    main()
```

- When `calculator.py` is run directly, `main()` executes  
- When it’s imported into another file, only the functions are available — no unwanted execution  

---

## Why This Matters in Real Projects

Without the `__main__` guard:

- Code may execute unintentionally on import  
- Unit testing becomes harder  
- Modules become less reusable  

This pattern is widely used in libraries, scripts, and frameworks.

---

## How Python Sets `__name__`

When Python starts execution, it assigns `"__main__"` to the entry-point script.

All other imported files receive their module names automatically.

---

## Common Interview Misconceptions

❌ Thinking `__name__` is a function  
❌ Thinking `__main__` is a keyword  
❌ Forgetting that imported files still execute top-level code  

---

## Best Practices

- Always use `__name__ == "__main__"` for runnable scripts  
- Keep reusable logic outside the main block  
- Use it to make modules test-friendly  

---

## Strong Interview Closing Line

> So `__name__` allows Python to distinguish between a file being run directly and being imported, and the `__main__` guard ensures clean, reusable, and predictable code execution.