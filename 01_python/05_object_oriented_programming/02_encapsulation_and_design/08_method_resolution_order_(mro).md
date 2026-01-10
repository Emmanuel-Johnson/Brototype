“In Python, Method Resolution Order (MRO) defines the order in which Python looks for methods and attributes in a class hierarchy. It is especially important in multiple inheritance.”

## What is MRO?
MRO is the sequence of classes Python follows to resolve method calls.

- Determines which method is called
- Applies to methods and attributes
- Used internally by `super()`

> Interview line: “MRO decides the order in which classes are searched for a method.”

## Why do we need MRO?
Multiple inheritance can create ambiguity when the same method name exists in multiple parent classes. Python resolves this using the C3 linearization algorithm.

> Interview-safe line: “Python uses C3 linearization to compute MRO.”

## Simple inheritance example
```python
class A:
    def show(self):
        print("A")

class B(A):
    pass

print(B.mro())
```

Output:
```
[B, A, object]
```

> Key point: “Python checks the child first, then the parent, then object.”

## Multiple inheritance example
```python
class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

C().show()
print(C.mro())
```

Output:
```
A
[C, A, B, object]
```

> Why? “Python follows the order of inheritance defined in the class.”

## Diamond problem (classic interview case)
```python
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

print(D.mro())
```

MRO of D:
```
[D, B, C, A, object]
```

> Interview gold: “Python resolves the diamond problem using C3 linearization.” 🏆

## How `super()` uses MRO
`super()` does not mean “call parent directly”; it means “call the next class in the MRO.”

> Important: “super() follows MRO, not the immediate parent.”

## How to check MRO
Two ways:
- `ClassName.mro()`
- `ClassName.__mro__`

> Interview line: “MRO can be inspected programmatically.”

## Rules of MRO (high-level)
- Child classes come before parents  
- Order is preserved as written in the class definition  
- No class appears twice

> Safe interview phrasing: “MRO maintains consistency and avoids ambiguity.”

## Common interview mistakes
- ❌ Thinking `super()` calls only the parent  
- ❌ Ignoring inheritance order  
- ❌ Not understanding diamond inheritance

Correct understanding:
- ✅ “MRO provides a predictable method lookup order.”

## When is MRO important?
- Multiple inheritance  
- Cooperative inheritance  
- Frameworks and mixins  
- Complex class hierarchies

> One-line interview summary: “Method Resolution Order defines the sequence Python follows to resolve methods in inheritance hierarchies, ensuring consistent behavior even with multiple inheritance.”
