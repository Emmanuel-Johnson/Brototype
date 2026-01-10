“In Python, `@staticmethod` and `@classmethod` are decorators used to define methods related to a class but that behave differently from instance methods. They help organize logic that doesn’t depend on object-specific data.”

## Quick context

In a class, we have three types of methods:

- Instance methods → use `self`  
- Class methods → use `cls`  
- Static methods → use neither `self` nor `cls`

Interview line:  
“The difference lies in what data the method can access.”

---

## @classmethod

### What is a class method?
- Defined using `@classmethod`  
- Takes `cls` as the first parameter  
- Operates on class-level data  
- Can modify class variables

```python
class Student:
    college = "ABC College"

    @classmethod
    def change_college(cls, name):
        cls.college = name

# Usage
Student.change_college("XYZ College")
```

Interview line:  
“Class methods work with the class itself, not individual objects.”

### Why use `@classmethod`?
Used for:
- Modifying class variables
- Factory methods / alternative constructors

Example (factory method):

```python
class Person:
    def __init__(self, age):
        self.age = age

    @classmethod
    def from_birth_year(cls, year):
        return cls(2025 - year)
```

Interview gold 🏆:  
“Class methods are often used as alternative constructors.”

---

## @staticmethod

### What is a static method?
- Defined using `@staticmethod`  
- Takes no `self` and no `cls`  
- Behaves like a normal function that lives inside the class for logical grouping

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Usage
MathUtils.add(10, 20)
```

Interview line:  
“Static methods don’t access class or instance data.”

### Why use `@staticmethod`?
Used when:
- Logic is related to the class but does not need access to class or instance state
- Utility or helper functions

Strong line:  
“Static methods improve code organization, not data access.”

---

## Key differences: `@staticmethod` vs `@classmethod`

| Feature                | `@staticmethod` | `@classmethod` |
|-----------------------:|:---------------:|:--------------:|
| First parameter        | None            | `cls`          |
| Access class variables | ❌ No           | ✅ Yes         |
| Modify class state     | ❌ No           | ✅ Yes         |
| Common use             | Utility logic   | Factory / config |

Interview killer line:  
“Use `@classmethod` when you need class context, and `@staticmethod` when you don’t.”

---

## Calling via objects
Yes, they can be called on instances, but best practice is to call them on the class:

```python
Student.change_college("XYZ")
MathUtils.add(5, 6)
```

Interview-safe line:  
“They should be called using the class name for clarity.”

---

## Common interview mistakes
- ❌ Using `@staticmethod` when `cls` is needed  
- ❌ Confusing class methods with instance methods  
- ❌ Thinking static methods can access class variables

Correct understanding ✅:  
“Only class methods have access to class-level data.”

---

## When to choose what (decision rule)
- Need object data → instance method  
- Need class data → class method  
- Need no data → static method

One-line interview summary:  
“`@classmethod` operates on class-level data using `cls`, while `@staticmethod` is a utility method that doesn’t access class or instance state.”
