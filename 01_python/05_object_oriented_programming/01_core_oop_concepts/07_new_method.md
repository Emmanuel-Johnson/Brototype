“In Python, `__new__` is a special method responsible for creating a new object.  
It is called before `__init__`, and it returns the newly created instance.”

## What is `__new__`?
- `__new__` is a static method
- It creates and returns a new instance of the class
- It runs before `__init__`

```py
class MyClass:
    def __new__(cls):
        print("__new__ called")
        return super().__new__(cls)

    def __init__(self):
        print("__init__ called")
```

> “__new__ creates the object, while __init__ initializes it.”

## Execution order
When an object is created:
```py
obj = MyClass()
```
Order of calls:
1. `__new__` → creates object  
2. `__init__` → initializes object

Important:
> If `__new__` does not return an instance, `__init__` will not run.

## Why use `__new__`?
Common use cases:
- Subclassing immutable types (`int`, `str`, `tuple`)
- Controlling object creation
- Implementing Singleton pattern
- Returning an object of a different class

Example with an immutable type:
```py
class MyInt(int):
    def __new__(cls, value):
        return super().__new__(cls, value)
```

> “`__new__` is required when modifying immutable object creation.”

## Difference between `__new__` and `__init__`

| `__new__` | `__init__` |
|---|---|
| Creates object | Initializes object |
| Returns instance | Returns nothing |
| Static method | Instance method |
| Runs first | Runs after |

## What if `__new__` returns something else?
```py
class A:
    def __new__(cls):
        return "Hello"
```
- The created object will be a string
- `__init__` will NOT execute

> “`__new__` can completely change the object being created.”

## Real-world usage
- Most developers never override `__new__`
- Use it only for advanced use cases

> “`__new__` is rarely used in day-to-day coding but important for advanced object control.”

## Common interview mistakes
- ❌ Thinking `__new__` is optional for immutable types  
- ❌ Forgetting to return `super().__new__(cls)`  
- ❌ Mixing responsibilities of `__new__` and `__init__`

## One-line summary
“`__new__` is a special method in Python that creates and returns a new instance of a class, and it is called before `__init__` during object creation.”
