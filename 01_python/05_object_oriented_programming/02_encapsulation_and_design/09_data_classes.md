“In Python, data classes simplify creating classes that mainly store data. They automatically generate common methods like `__init__`, `__repr__`, and `__eq__`, reducing boilerplate.”

## What problem do data classes solve?
Traditional classes used for simple data containers become verbose when you add constructors, comparisons, and reprs.

Example (traditional):
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

> “Data classes reduce repetitive boilerplate code in data-holding classes.”

## What is a data class?
Use the `@dataclass` decorator. Python generates `__init__`, `__repr__`, `__eq__`, and more automatically.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

Now:
```python
p = Person("Alex", 25)
print(p)  # Person(name='Alex', age=25)
```

> “Data classes automatically create constructor and comparison methods.”

## Why type annotations matter
Fields are defined using type hints. This improves readability and tooling (linters, IDEs). Type hints are not enforced at runtime but are highly useful.

> “Type hints make data classes self-documenting.”

## Comparison support (`__eq__`)
```python
p1 = Person("Alex", 25)
p2 = Person("Alex", 25)
print(p1 == p2)  # True
```
Equality is based on field values, not object identity.

## Default values
```python
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    role: str = "Developer"
```

> “Data classes support default values just like function parameters.”

## Immutable data classes
Make objects immutable with `frozen=True`:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 10  # raises FrozenInstanceError
```

> “Frozen data classes create immutable objects.”

## Custom behavior
You can still add methods and custom logic:
```python
@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height
```
Data classes enhance, not replace, normal classes.

## When to use data classes
Use data classes when:
- A class mainly stores data
- You want clean, readable code
- You need comparison/representation methods

Avoid when:
- Heavy business logic is involved
- Complex inheritance hierarchies are required

> “Data classes are ideal for plain data objects.”

## Data classes vs named tuples
- Data classes are mutable by default
- Support methods and more flexible structure
- Often more readable and extensible

## Common interview mistakes
- Thinking data classes are immutable by default ❌  
- Assuming type hints are enforced ❌  
- Using data classes for complex logic-heavy classes ❌

Correct mindset: “Use data classes for data, not behavior-heavy objects.”

## One-line interview summary
“Data classes provide a concise way to define data-holding classes in Python by automatically generating common methods like `__init__`, `__repr__`, and `__eq__`.”
