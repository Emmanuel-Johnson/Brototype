In Python, access control is implemented by naming conventions rather than enforced modifiers. The following explains the conventions and their typical use.

## Public Members
- Accessible from anywhere.
- Default behavior in Python (no underscore prefix).

Example:
```python
class Person:
    def __init__(self):
        self.name = "Alex"   # public variable

    def greet(self):        # public method
        print("Hello")

p = Person()
print(p.name)
p.greet()
```

> Interview line:  
> "By default, all members in Python are public."

## Protected Members
- Indicated by a single leading underscore: _name
- Intended for internal use within a class and its subclasses (convention only).
- Still accessible from outside, but discouraged.

Example:
```python
class Employee:
    def __init__(self):
        self._salary = 50000

e = Employee()
print(e._salary)   # allowed, but not recommended
```

> Important: "Protected members are a convention, not a restriction."  
> Interview-safe line: "A single underscore indicates internal or subclass-level use."

## Private Members
- Indicated by a double leading underscore: __name
- Triggers name mangling to reduce accidental access/overriding in subclasses.
- Not true privacy — it makes access harder, not impossible.

Example:
```python
class Bank:
    def __init__(self):
        self.__balance = 1000

b = Bank()
# print(b.__balance)  # AttributeError
# Internally becomes: b._Bank__balance
print(b._Bank__balance)  # possible but breaks encapsulation
```

> Interview gold: "Private members use name mangling, not true privacy."

## Why Name Mangling Exists
- Avoids accidental overriding in subclasses.
- Makes accidental external access less likely while preserving flexibility.

> Strong line: "Python emphasizes responsibility over restriction."

## Comparison

| Type      | Prefix   | Accessibility (convention)                    |
|-----------|----------|-----------------------------------------------|
| Public    | name     | Everywhere                                     |
| Protected | _name    | Class & subclasses (by convention)            |
| Private   | __name   | Class only (via name mangling)                |

## Can Private Members Be Accessed?
Yes, but not recommended.

```python
print(b._Bank__balance)  # works, breaks encapsulation
```

> Interview-safe wording: "Private members can be accessed indirectly, but it breaks encapsulation."

## Python Philosophy
- "We are all consenting adults" — Python trusts developers to follow conventions rather than enforce strict access control.

> Interview flex: "Python relies on conventions rather than strict access modifiers."

## When to Use Each
- Public → normal usage and API surface.
- Protected → internal or inheritance-based logic.
- Private → sensitive data or to avoid name clashes in complex hierarchies.

## One-line Interview Summary
"Python supports public, protected, and private members using naming conventions: public is the default, protected uses a single underscore, and private uses double underscores with name mangling."
