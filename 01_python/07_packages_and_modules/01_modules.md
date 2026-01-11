## What is a Module in Python?

In Python, a **module** is simply a file that contains Python code — such as functions, classes, and variables — which can be reused across multiple programs.

Modules help:
- Organize code  
- Promote reusability  
- Improve maintainability  

---

## Why Modules Are Important

Without modules, all code would exist in a single file, making applications hard to read, test, and maintain.

Modules allow us to:
- Break large programs into smaller files  
- Reuse code across projects  
- Avoid naming conflicts  
- Improve readability and structure  

---

## Creating a Module

Any `.py` file can act as a module.

### Example: `math_utils.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

---

## Importing a Module

There are several ways to import modules.

### Import the entire module
```python
import math_utils
math_utils.add(2, 3)
```

### Import specific members
```python
from math_utils import add
add(2, 3)
```

### Use an alias
```python
import math_utils as mu
mu.add(2, 3)
```

---

## Built-in Modules

Python comes with many built-in modules such as:
- `math`
- `sys`
- `os`
- `datetime`

### Example:
```python
import math
print(math.sqrt(16))
```

These modules provide optimized and reliable functionality.

---

## The `__name__ == "__main__"` Pattern

When a Python file is run directly, its `__name__` is set to `"__main__"`.

```python
if __name__ == "__main__":
    print("Running directly")
```

This prevents code from executing when the file is imported as a module.

---

## Module Search Path

When importing a module, Python searches in:
1. The current directory  
2. Standard library directories  
3. Paths listed in `sys.path`  

This is why proper module structure and environment configuration matter.

---

## Packages vs Modules

- **Module** → A single Python file  
- **Package** → A collection of modules organized in directories, usually containing an `__init__.py` file  

---

## Best Practices

- Keep modules small and focused  
- Use meaningful module names  
- Avoid wildcard imports (`from module import *`)  
- Group related functionality together  

---

## Common Interview Mistakes

- Confusing modules with packages  
- Forgetting the `__main__` guard  
- Overusing wildcard imports  

---

## Strong Interview Closing Line

> So in Python, modules allow us to organize, reuse, and maintain code effectively by separating functionality into reusable files.