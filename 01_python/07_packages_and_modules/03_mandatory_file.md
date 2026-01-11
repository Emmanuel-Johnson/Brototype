## What is `__init__.py`?

In Python, `__init__.py` is a special file used to mark a directory as a package.

Historically, Python required this file for a folder to be recognized as a package, and even today it plays an important role in package design and initialization.

---

## Why `__init__.py` Exists

The main purposes of `__init__.py` are:

- To tell Python that a directory is a package  
- To run initialization code when the package is imported  
- To control what is exposed from the package  

---

## Basic Example

```
my_package/
├── __init__.py
├── math_utils.py
├── string_utils.py
```

When we import `my_package`, Python automatically executes `__init__.py`.

---

## Simple `__init__.py`

```python
# my_package/__init__.py
print("Package initialized")
```

This code runs **once** when the package is first imported.

---

## Exposing Package-Level APIs

`__init__.py` can be used to expose selected functions or classes.

```python
# my_package/__init__.py
from .math_utils import add
```

Now users can write:

```python
from my_package import add
```

This creates a clean and user-friendly interface.

---

## Package Variables

We can define package-level variables inside `__init__.py`.

```python
# my_package/__init__.py
VERSION = "1.0.0"
```

This allows shared configuration across modules.

---

## Controlling Imports with `__all__`

`__init__.py` can define `__all__` to control wildcard imports.

```python
__all__ = ["add", "VERSION"]
```

This determines what gets imported when using:

```python
from my_package import *
```

---

## Is `__init__.py` Still Mandatory?

Since Python 3.3, Python supports **namespace packages**, where `__init__.py` is not strictly required.

However, in practice:

- Most real-world projects still include it  
- It provides clarity, compatibility, and control  
- Many tools and frameworks expect it  

---

## Best Practices

- Keep `__init__.py` lightweight  
- Avoid heavy logic inside it  
- Use it to define public APIs  
- Don’t abuse wildcard imports  

---

## Common Interview Traps

❌ Thinking `__init__.py` is a constructor — it’s not  
❌ Putting business logic inside `__init__.py`  
❌ Assuming it’s always mandatory  

---

## Strong Interview Closing Line

> So `__init__.py` marks a directory as a Python package, runs initialization code, and defines what the package exposes, making it a key part of clean package design.