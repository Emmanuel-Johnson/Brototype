“Duck typing in Python means that the type of an object is determined by its behavior, not its class.  
If an object behaves like a duck, Python treats it like a duck.”

## What does “duck typing” mean?

> “If it walks like a duck and quacks like a duck, it’s a duck.”

- Focus is on what methods/attributes an object provides, not what class it belongs to.
- Pythonic mindset: behavior over explicit types.

## Simple example
```python
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())
make_sound(Cat())
```
Key point: both objects work because they implement the same method.

## No inheritance required

- Dog and Cat can be unrelated classes with no common base.
- Duck typing works without inheritance.

## Duck typing vs traditional OOP

Traditional (type-based):
```python
if isinstance(obj, Dog):
    obj.speak()
```

Pythonic (duck typing):
```python
obj.speak()
```

Duck typing avoids explicit type checks.

## What happens if the method is missing?
```python
make_sound(10)  # Raises AttributeError
```
Duck typing relies on trusting that the object provides the expected behavior; missing methods are caught at runtime.

## Duck typing and polymorphism

- Duck typing is a form of polymorphism: same interface, different implementations.
- Enables polymorphism without inheritance.

## Duck typing vs abstract base classes

- Duck typing: flexible, informal.
- Abstract base classes: strict, enforced.
- Python supports both approaches.

## Real-world Python examples

- File objects: read(), write()
- Iterables: __iter__()
- Context managers: __enter__(), __exit__()

## When to use duck typing

Use when:
- You want flexibility
- You care about behavior
- You want clean, Pythonic code

Avoid when:
- Strict contracts are required
- APIs must be tightly controlled

## Common interview mistakes

- Confusing duck typing with inheritance
- Assuming compile-time type safety
- Overusing isinstance()

Correct mindset: “Python prefers behavior-based programming.”

## One-line interview summary

“Duck typing in Python means objects are used based on their behavior rather than their explicit type, enabling flexible and polymorphic code.”
