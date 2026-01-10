> “In Python, class variables are variables that belong to the class itself, not to individual objects. They are shared across all instances of that class.”

## What are class variables?
- Defined inside the class, but outside methods
- Created once and shared by all instances
- Typical use: constants, counters, shared configuration

Example:
```py
class Student:
    college = "ABC College"   # class variable
```

## Accessing class variables
- Recommended: via class name (clearer)
- Also accessible via an instance (reads the class variable unless overridden)

Examples:
```py
Student.college   # "ABC College"
s1 = Student()
s1.college        # "ABC College"
```

Best practice:
> Class variables should be accessed using the class name for clarity.

## Class variable vs instance variable

```py
class Student:
    college = "ABC College"    # class variable

    def __init__(self, name):
        self.name = name       # instance variable
```

| Class Variable | Instance Variable |
|---|---|
| Belongs to class | Belongs to object |
| Shared by all instances | Unique per instance |
| Single copy | Separate copies per object |
| Defined outside methods | Defined using self inside methods |

Interview note:
> “Instance variables store object-specific state, while class variables store shared state.”

## What happens when you modify a class variable?
```py
Student.college = "XYZ College"   # updates class variable for all instances
```
But:
```py
s1.college = "Private College"    # creates an instance attribute `college` for s1 only
```
- Assigning via an object shadows the class variable; it does not change the class attribute.

Important:
> Assigning via an object shadows the class variable.

## Why use class variables?
- Constants
- Counters (shared across instances)
- Shared configuration or default values

Example:
```py
class Employee:
    company = "Google"
```

Interview line:
> “Class variables are used when data must be common across all instances.”

## Memory perspective (advanced)
- Stored in the class namespace (class.__dict__)
- Only one allocation for the class variable; instances reference it unless they override it

Optional note:
> Class variables are stored in the class dictionary, not the instance dictionary.

## Common interview mistake
Mistake: “Class variables are copied into each object.”  
Correct: “Class variables are shared; only instance variables are per-object.”

## One-line summary
> “Class variables are class-level attributes shared by all objects, created once, and used for common data across instances.”
