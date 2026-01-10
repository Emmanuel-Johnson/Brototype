> “In Python, a class is a blueprint for creating objects.  
> It allows us to bundle data (attributes) and behavior (methods) together into a single unit.”

## What is a Class?
A class defines what an object will look like and what it can do.

- Class → blueprint  
- Object → real instance created from the class

Example: `Car` is a class; `BMW` or `Audi` are objects of that class.

## Why Use Classes?
Classes help with:
- Code reusability
- Better organization
- Encapsulation (data + methods together)
- Real-world modeling

Interview line: “Classes make code modular, reusable, and closer to real-world entities.”

## Basic Syntax
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)
```

## __init__ Method (Constructor)
- Runs automatically when an object is created
- Used to initialize object data

Interview line: “__init__ is a constructor that initializes the object’s state.”

## What is `self`?
- `self` refers to the current object
- Used to access instance variables and methods

Important interview point: “`self` is passed automatically, but we must declare it explicitly.”

## Creating an Object
```python
p1 = Person("Alex", 25)
p1.greet()
```
- `p1` is an object (instance)  
- `Person()` creates the object  
- Methods are called using dot (`.`) notation

## Instance Variables vs Class Variables
```python
class Student:
    college = "ABC College"   # class variable

    def __init__(self, name):
        self.name = name      # instance variable
```
- Instance variable → unique for each object  
- Class variable → shared by all objects

Interview line: “Instance variables belong to objects, class variables belong to the class.”

## Methods in a Class
Types of methods:
- Instance methods → use `self`
- Class methods → use `cls` (use `@classmethod`)
- Static methods → no `self` or `cls` (use `@staticmethod`)

(Usually interviewers expect at least an explanation of instance methods.)

## Object-Oriented Principles (Brief)
Classes support OOP concepts like:
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

Short line: “Python classes are the foundation of object-oriented programming.”

## One-Line Interview Summary
“A class in Python is a blueprint that defines attributes and methods, enabling object-oriented programming through reusable and well-structured code.”
