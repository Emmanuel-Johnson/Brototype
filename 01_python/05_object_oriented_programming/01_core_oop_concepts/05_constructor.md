“In Python, a constructor is a special method named `__init__`.  
It is automatically called when an object is created, and it is used to initialize the object’s data.”

## What is `__init__`?
- `__init__` stands for initialize.  
- Runs once per object creation.  
- Used to set initial values of instance variables.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

> Interview line: “__init__ initializes the state of an object at the time of creation.”

## When is `__init__` called?
```python
p1 = Person("Alex", 25)
```
Internally, Python does:
```python
Person.__init__(p1, "Alex", 25)
```

> Interview gold: “The constructor is invoked automatically when an object is instantiated.”

## Role of `self` in the constructor
- `self` refers to the current object.  
- Allows attaching data to the object:
```python
self.name = name
```

Key line: “Without `self`, variables inside `__init__` would be local, not part of the object.”

## Why do we need a constructor?
Constructors are used to:
- Initialize instance variables.  
- Ensure an object starts in a valid state.  
- Reduce repetitive setup code.

Example:
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
```

> Interview line: “Constructors ensure every object starts with a consistent initial state.”

## Can a class exist without `__init__`?
Yes.
```python
class A:
    pass

obj = A()
```
- Python provides a default constructor.  
- No instance variables are initialized.

> Interview note: “If no constructor is defined, Python uses a default one.”

## Can we have multiple constructors?
- Python does not support method overloading directly.  
- Use default arguments or variable-length arguments instead.

Example:
```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
```

> Interview line: “Python handles constructor flexibility using default or variable arguments.”

## Constructor vs Regular Method

| Constructor (`__init__`) | Regular Method |
|---|---|
| Called automatically | Called manually |
| Initializes object | Performs actions |
| Runs once per object | Can run multiple times |

## Advanced interview point
- `__init__` does not create the object — `__new__` does.  
- `__init__` only initializes it.

Flex line: “`__new__` creates the object, while `__init__` initializes it.”

## One-line interview summary
“The `__init__` method is a special constructor in Python that runs automatically during object creation to initialize instance variables and set up the object’s state.”
