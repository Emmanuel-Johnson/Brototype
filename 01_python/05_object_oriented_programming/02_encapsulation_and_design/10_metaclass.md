> “In Python, a metaclass is a class whose instances are classes themselves.  
> Just like a class defines how objects are created, a metaclass defines how classes are created.”

## Big picture (very important)
Think in layers:
- Object → instance of a class  
- Class → instance of a metaclass

Interview killer line:
> Objects are created from classes, and classes are created from metaclasses.

## Default metaclass
By default, all classes use the built-in metaclass: `type`.

Example:
```python
class A:
    pass

print(type(A))  # <class 'type'>
```

Interview line:
> In Python, `type` is the default metaclass.

## How classes are created internally
When Python sees:
```python
class MyClass:
    pass
```
it internally does something like:
```python
MyClass = type("MyClass", (), {})
```

Key insight:
> `type` can dynamically create classes.

## What is a custom metaclass?
A custom metaclass lets you:
- Control class creation
- Modify class attributes
- Enforce rules at class definition time

Defined by inheriting from `type`:
```python
class MyMeta(type):
    pass
```

## Using a metaclass
```python
class MyClass(metaclass=MyMeta):
    pass
```

Interview line:
> A metaclass is assigned using the `metaclass` keyword.

## __new__ and __init__ in metaclasses
Metaclasses typically override:
- `__new__` → creates the class
- `__init__` → initializes the class

Example:
```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, attrs)
```

Key line:
> Metaclass `__new__` runs when the class is created, not when an object is created.

## Why use metaclasses?
Common use cases:
- Framework internals (Django, SQLAlchemy)
- API enforcement
- Automatic method or class registration
- Validation of class structure

Interview-safe line:
> Metaclasses are mainly used in frameworks and advanced libraries.

## Example use cases (conceptual)
- Enforce that every subclass implements a specific method  
- Automatically register subclasses in a registry  
- Inject attributes or methods into classes

Strong line:
> Metaclasses enforce rules at the class level.

## Metaclass vs class decorator
- Class decorator → modifies a class after creation  
- Metaclass → controls the class during creation

Interview gold:
> Metaclasses work at a lower level than class decorators.

## Should you use metaclasses often?
Honest advice:
> No. Metaclasses are powerful but complex and should be used sparingly.

Rule of thumb:
- Try class decorators first
- Use metaclasses only when necessary

## Common interview mistakes
- ❌ Thinking metaclasses create objects  
- ❌ Overusing metaclasses  
- ❌ Confusing metaclass with inheritance

Correct understanding:
> Metaclasses control class creation, not object creation.

## One-line interview summary
> A metaclass in Python defines how classes are created, just as a class defines how objects are created, and the default metaclass is `type`.
