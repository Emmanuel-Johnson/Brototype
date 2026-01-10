> “In Python, `super()` and `super().__init__()` are related but not the same. `super()` gives access to the parent class, while `super().__init__()` specifically calls the parent class constructor.”

## What is `super()`?
- Returns a proxy object.
- Lets you call methods of the next class in the MRO (method resolution order).
- Does not call anything by itself.

Example:
```py
super()
```

> Interview line: “`super()` only returns a reference to the parent class—it doesn’t execute any method.”

## What is `super().__init__()`?
- Calls the constructor of the parent class.
- Used to initialize parent class state.
- Most common usage of `super()`.

Example:
```py
super().__init__()
```

> Interview line: “`super().__init__()` is used to initialize the parent class part of a child object.”

## Execution flow example
```py
class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")
```

Output:
```
Parent init
Child init
```

Key point:
> “The parent constructor runs before the child constructor completes.”

## Why `super().__init__()` is important
Without calling it:
```py
class Child(Parent):
    def __init__(self):
        print("Child init")
```
- Parent attributes are not initialized — can cause runtime errors.

> Interview warning: “Skipping `super().__init__()` may leave the object in an incomplete state.”

## `super()` vs direct parent call
Bad (fragile):
```py
Parent.__init__(self)
```
Best:
```py
super().__init__()
```
Why?
- Direct calls break in multiple inheritance and hard-code the parent class.
- `super()` supports cooperative inheritance and follows the MRO.

> Interview gold: “`super()` supports cooperative inheritance and follows MRO.”

## Role in multiple inheritance
- Python follows MRO.
- `super()` ensures each class is initialized once.

> “`super().__init__()` ensures correct constructor chaining in multiple inheritance.”

## Python 3 simplification
- In Python 3 you can call `super()` without arguments:
```py
super().__init__()
```

> Interview-safe line: “In Python 3, `super()` can be called without arguments.”

## Common interview mistakes
- Thinking `super()` automatically calls the constructor.
- Forgetting `super().__init__()`.
- Believing `super()` always refers to the direct parent.

Correct view:
> “`super()` follows the MRO, not just the immediate parent.”

## One-line difference (interview summary)
> “`super()` gives access to the parent class, while `super().__init__()` explicitly calls the parent constructor.”

Final interview summary:
> “`super()` is a mechanism to access parent class methods following MRO, and `super().__init__()` is used to initialize the parent part of an object during inheritance.”
