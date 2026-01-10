> “In Python, an object is a real-world instance of a class. It represents an entity that has state (data) and behavior (methods).”

## What is an Object?
An object is created from a class and occupies memory.

- **Class** → blueprint  
- **Object** → actual implementation of that blueprint

> “If a class is a blueprint, an object is the real thing created from it.”

## How is an Object Created?
Objects are created by calling the class name like a function.

```python
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alex")
```

- `Person` → class  
- `p1` → object (instance)  
- `Person("Alex")` → object creation

## Object Contains Two Things
Every object has:
- **Attributes** → data stored in the object  
- **Methods** → functions that operate on that data

Examples:
```python
p1.name        # attribute
p1.greet()     # method
```

> “Objects combine data and behavior in a single unit.”

## Instance Variables Belong to Objects
```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("John")
s2 = Student("Emma")
```
- `s1.name` and `s2.name` are different — each object has its own copy of instance variables.

Key point: “Each object maintains its own state.”

## How Objects Call Methods
When you call:
```python
p1.greet()
```
Internally Python does:
```python
Person.greet(p1)
```

Interview gold line: “The object is passed automatically as `self` to instance methods.”

## Objects Have Identity, Type, and Value
Every Python object has:
- **Identity** → memory address (`id(obj)`)  
- **Type** → class (`type(obj)`)  
- **Value** → data stored

Example:
```python
id(p1)
type(p1)
```

> “Python objects are characterized by identity, type, and value.”

## Everything in Python Is an Object
Integers, strings, lists, functions — all are objects.
```python
x = 10
print(type(x))   # <class 'int'>
```

> “Python is a fully object-oriented language where everything is an object.”

## Difference Between Class and Object

| Class            | Object                  |
|------------------|-------------------------|
| Blueprint        | Instance                |
| No memory        | Occupies memory         |
| Defined once     | Created multiple times  |

One-line interview summary:

> “An object in Python is an instance of a class that contains data and behavior, occupies memory, and represents a real-world entity.”
