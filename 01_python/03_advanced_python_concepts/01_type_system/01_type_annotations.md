Type annotations in Python are a way to explicitly specify the expected data types of variables, function parameters, and return values.

Python is dynamically typed, so you don't have to declare types. Type annotations are optional hints that make code clearer, safer, and more maintainable.

## Why type annotations exist

They help with:
- Code readability — other developers instantly know what type is expected
- Early bug detection — tools like linters and mypy catch mistakes before runtime
- Better IDE support — autocomplete, suggestions, and warnings
- Large codebases — easier collaboration and refactoring

**Important:** Python does NOT enforce types at runtime — they are hints, not rules.

## Basic variable annotation

```python
age: int = 25
price: float = 99.9
name: str = "Alice"
is_active: bool = True
```

Here, `age` is expected to be an integer, but Python won’t stop you from assigning a different type later.

## Function annotations (very common in interviews)

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `a: int` → parameter type  
- `b: int` → parameter type  
- `-> int` → return type

This makes the function contract explicit.

## Annotations do NOT enforce types

```python
def greet(name: str) -> str:
    return "Hello " + name

greet(10)   # logically wrong, but Python allows it
```

Python won’t raise an error here unless the operation itself fails. Type checking happens via tools, not the interpreter.

## Common built-in generic types

```python
from typing import List, Tuple, Dict, Set

numbers: List[int] = [1, 2, 3]
person: Dict[str, int] = {"age": 25}
coords: Tuple[int, int] = (10, 20)
unique_ids: Set[int] = {1, 2, 3}
```

These annotations describe the types contained in the containers.

## Optional & Union types

```python
from typing import Optional, Union

def get_user(age: Optional[int]) -> str:
    return "Valid" if age else "Invalid"

def process(value: Union[int, str]) -> None:
    print(value)
```

- `Optional[int]` means `int` or `None`.  
- `Union[int, str]` allows either `int` or `str`.

## Type annotations vs type casting (interview trap)

Type annotation → tells what type should be  
Type casting → converts value to another type

```python
x: int = "10"     # Annotation (no conversion)
y = int("10")     # Casting (conversion)
```

## Where type annotations are used most

- Backend frameworks (Django, FastAPI)  
- APIs  
- Large codebases and team projects  
- Static analysis with tools like mypy

## One-line interview summary

“Type annotations in Python provide optional static typing that improves code clarity, documentation, and tooling support, without affecting runtime behavior.”
