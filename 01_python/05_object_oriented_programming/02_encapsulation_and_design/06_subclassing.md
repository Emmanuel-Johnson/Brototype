> “In Python, subclassing means creating a new class from an existing class.  
> The new class, called a subclass or child class, inherits attributes and methods from the parent or base class.”

## What is subclassing?
Subclassing is the mechanism that enables inheritance.

- Parent class → base functionality  
- Child class → extends or modifies behavior

Example:
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass
```

> Interview line: “Subclassing allows code reuse and extension of existing classes.”

## How subclassing works
```python
dog = Dog()
dog.speak()
```
Output:
```
Animal speaks
```

> Key point: “Even though Dog has no methods, it can use methods from Animal.”

## Overriding methods in a subclass
A subclass can override parent methods:
```python
class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()
```
Output:
```
Bark
```
> Interview gold: “Method overriding allows subclasses to provide their own implementation.”

## Using super() in subclassing
To reuse parent behavior:
```python
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")
```
> Key interview line: “super() calls the parent class method following the method resolution order.”

## Subclass constructor (__init__)
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```
> Important point: “super().__init__() ensures the parent class is properly initialized.”

## Types of inheritance (brief)
Python supports:
- Single inheritance  
- Multiple inheritance  
- Multilevel inheritance  
- Hierarchical inheritance

> Interview-safe line: “Subclassing works across all inheritance types in Python.”

## When should you use subclassing?
Use subclassing when:
- There is an “is-a” relationship  
- You want to extend existing behavior  
- You want polymorphism

Avoid it when:
- Relationship is “has-a” (use composition instead)

> Strong line: “Prefer subclassing only when the relationship is logically valid.”

## Subclassing enables polymorphism
```python
class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]
for a in animals:
    a.speak()
```
> Interview line: “Subclassing enables polymorphism through method overriding.”

## Common interview mistakes
- Forgetting super().__init__()  
- Using inheritance where composition fits better  
- Confusing overriding with overloading

> Correct view: “Subclassing should model real-world hierarchy, not just reuse code.”

## One-line interview summary
> “Subclassing in Python allows a child class to inherit, extend, or override behavior from a parent class, enabling code reuse and polymorphism.”
