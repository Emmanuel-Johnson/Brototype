Magic methods, also called dunder methods (double underscore methods), are special methods in Python that start and end with double underscores, like `__init__` or `__str__`. They let objects define behavior for built-in Python operations.

> "Magic methods let us customize the behavior of objects."

## What are magic (dunder) methods?
- Special methods with the pattern: `__method__`
- Automatically called by Python
- Let custom objects behave like built-in types

Examples: `__init__`, `__str__`, `__len__`, `__add__`, `__eq__`

## Why are they called "magic"?
You normally don't call them directly — Python calls them behind the scenes.

Example:
```py
print(obj)
# internally calls:
obj.__str__()
```

> "Magic methods are triggered implicitly by Python syntax."

## Commonly used magic methods

### `__init__` — Constructor
Called when an object is created.
```py
class Person:
    def __init__(self, name):
        self.name = name
```
> "__init__ initializes the object."

### `__str__` — String representation
Defines what `print(object)` shows.
```py
class Person:
    def __str__(self):
        return "Person object"
```
> "`__str__` provides a user-friendly string representation."

### `__repr__` — Developer representation
Used for debugging and unambiguous representation.
```py
def __repr__(self):
    return "Person(name='Alex')"
```
> "`__repr__` is meant for developers, `__str__` for users."

### `__len__` — Length
Called when `len()` is used.
```py
class MyList:
    def __len__(self):
        return 10
```
> "len(obj) internally calls `obj.__len__()`."

### Operator overloading (`__add__`, `__eq__`, ...)
```py
class Point:
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```
> "Magic methods enable operator overloading."

## Comparison operators
- `__eq__`  — `==`
- `__lt__`  — `<`
- `__gt__`  — `>`

Example:
```py
def __eq__(self, other):
    return self.value == other.value
```
> "Comparison magic methods define how objects are compared."

## Object lifecycle magic methods
- `__new__` → creates object  
- `__init__` → initializes object  
- `__del__` → cleanup before destruction

> "`__new__` creates the object, `__init__` initializes it."

## Why use magic methods?
They allow:
- Custom object behavior
- Cleaner syntax
- Integration with Python features
- More readable and Pythonic code

> "Magic methods make user-defined objects feel like native Python objects."

## Common interview mistakes
- Calling magic methods directly
- Overusing operator overloading
- Confusing `__str__` and `__repr__`

Correct approach: "Use magic methods only when they make behavior intuitive."

## When should you use them?
Use magic methods when:
- You want custom objects to work with built-in functions
- You want natural syntax (`+`, `==`, `len()`)

Avoid when behavior becomes confusing or misleading.

## One-line interview summary
"Magic or dunder methods are special methods in Python that let objects respond to built-in operations, enabling custom behavior and operator overloading."
