“In Python, the `@property` decorator allows us to access a method like an attribute. It is used to implement encapsulation, validation, and controlled access to class data.”

## What is `@property`?

- Converts a method into a read-only attribute (unless a setter is provided)  
- Called without parentheses  
- Keeps attribute-style access

Example:

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

p = Person(25)
print(p.age)   # not p.age()
```

> “@property lets methods behave like attributes.”

## Why do we need `@property`?

Problem ❌:

```python
p.age = -5  # no validation, breaks object integrity
```

Solution ✅:

`@property` lets you add validation and keep a clean public interface.

## Getter, setter, and deleter

Getter:

```python
@property
def age(self):
    return self._age
```

Setter:

```python
@age.setter
def age(self, value):
    if value < 0:
        raise ValueError("Age cannot be negative")
    self._age = value
```

Deleter:

```python
@age.deleter
def age(self):
    del self._age
```

> Interview gold 🏆: “@property supports getter, setter, and deleter methods.”

## Why use `_age` (protected variable)?

- Prevents recursion when implementing getters/setters  
- Indicates internal use (implementation detail)

> “The actual data is stored in a protected variable, not the property itself.”

## `@property` vs normal methods

Traditional (less Pythonic):

- `get_age()`
- `set_age(value)`

Pythonic:

- `p.age`
- `p.age = 30`

> “@property avoids Java-style getters and setters.”

## Read-only properties

If no setter is defined:

```python
@property
def age(self):
    return self._age
```

- The attribute becomes read-only  
- Assignment raises an `AttributeError`

> “Properties can enforce read-only access.”

## Benefits of `@property`

- Encapsulation  
- Validation  
- Cleaner API  
- Backward compatibility  
- Future-proof design

“You can refactor internals without changing how users access attributes.”

## When should you use `@property`?

Use it when:
- You need validation
- Logic is involved in access
- You want to hide implementation details

Avoid it when:
- Simple, plain data attributes are enough

> One-line interview summary:  
> “The `@property` decorator allows controlled access to object attributes using attribute-style syntax, enabling encapsulation and validation in a Pythonic way.”
