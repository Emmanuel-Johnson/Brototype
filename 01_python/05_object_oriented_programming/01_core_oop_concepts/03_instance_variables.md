“In Python, instance variables are variables that belong to a specific object. They store data that is unique to each instance of a class.”

## What are instance variables?
- Defined inside methods (usually `__init__`)
- Accessed using `self`
- Each object gets its own copy

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

> Interview line: “Instance variables represent the state of an object.”

## How are they created?
- Created when an object is instantiated and `__init__` executes.

```python
p1 = Person("Alex", 25)
p2 = Person("John", 30)

# p1.name -> "Alex"
# p2.name -> "John"
```

> Key point: “Instance variables are initialized at runtime per object.”

## Why `self`?
- `self` refers to the current object and indicates which object’s data is being accessed or modified.
- Example: `self.name = name`

> Interview gold: “Without self, Python treats the variable as local to the method.”

## Instance variables are object-specific
```python
p1.age = 25
p2.age = 30
```
Changing one object’s instance variables does not affect others.

> Important line: “Each instance maintains its own independent state.”

## Accessing instance variables
- Inside the class: use `self`
- Outside the class: use the object reference, e.g. `print(p1.name)`

## Instance variables vs class variables

```python
class Student:
    college = "ABC College"   # class variable

    def __init__(self, name):
        self.name = name      # instance variable
```

| Instance Variable | Class Variable |
|-------------------|----------------|
| Object-specific   | Shared         |
| Created with `self` | Defined in class |
| Stored per object | Single copy    |

> Interview line: “Instance variables belong to objects, class variables belong to the class.”

## Can instance variables be created outside `__init__`?
Yes:
```python
p1.city = "Delhi"
```
But: Best practice is to define instance variables inside `__init__`.

## Memory perspective (advanced)
- Instance variables are stored in the instance namespace (`__dict__`)
- Each object has its own memory allocation

> Optional: “They are stored in the instance dictionary.”

## One-line interview summary
“Instance variables are object-specific variables defined using `self`, created at runtime, and used to maintain the state of each object independently.”
