"Object-Oriented Programming in Python is based on four main design principles: Encapsulation, Inheritance, Polymorphism, and Abstraction. These principles help us write reusable, maintainable, and scalable code."

---

## 1. Encapsulation
What it is:
- Bundling data and methods, controlling access to internal state.

Python example:
```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # protected by convention

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
```

Why it matters:
- Protects invariants, prevents accidental misuse, improves maintainability.

Web dev uses:
- Model attribute access control (ORMs), hiding DB internals behind getters/setters.
- Encapsulating session/state logic inside a service class.
- Hiding sensitive config or tokens in a secrets manager class.

Interview line:
- "Encapsulation hides internal details and exposes only what is necessary."

---

## 2. Inheritance
What it is:
- A class can reuse and extend behavior of another class.

Types of inheritance (with short Python examples):

- Single inheritance (one parent):
```python
class View:
    def get(self, request): ...

class HomeView(View):
    def get(self, request): ...
```

- Multiple inheritance (multiple parents, common in mixins):
```python
class AuthMixin:
    def authenticate(self, req): ...

class LoggingMixin:
    def log(self, msg): ...

class MyView(AuthMixin, LoggingMixin):
    pass
```

- Multilevel inheritance (A → B → C):
```python
class BaseModel: ...
class User(BaseModel): ...
class Admin(User): ...
```

- Hierarchical inheritance (one parent, many children):
```python
class Serializer: ...
class UserSerializer(Serializer): ...
class ProductSerializer(Serializer): ...
```

- Hybrid inheritance (combination of above):
- Common in complex frameworks when mixing base classes and mixins.

Why it matters:
- Promotes code reuse, centralizes logic, supports specialization.

Web dev uses:
- Class-based views (Django/Flask extensions) built from base view + mixins.
- Reusable mixins (authentication, pagination, logging).
- Base service/repository classes extended for domain-specific behavior.
- Model inheritance for shared fields and behavior across DB models.

Interview line:
- "Inheritance represents an 'is-a' relationship when used appropriately."

---

## 3. Polymorphism
What it is:
- "Same interface, different implementations." Objects can be used interchangeably if they support expected behavior.

Common types of polymorphism (with Python-relevant notes and examples):

1. Subtype (inclusion) polymorphism
- Via inheritance and duck typing: use base type or interface.
```python
class Shape:
    def area(self): raise NotImplementedError

class Circle(Shape):
    def area(self): ...

def total_area(shapes: list[Shape]):
    return sum(s.area() for s in shapes)
```

2. Duck typing (runtime polymorphism)
- No inheritance required; just implement the expected methods.
```python
class Dog:
    def speak(self): print("Bark")

class RobotDog:
    def speak(self): print("Beep bark")

for obj in [Dog(), RobotDog()]:
    obj.speak()  # both work
```

3. Ad-hoc polymorphism (overloading)
- Python lacks compile-time overloading, but supports:
  - Operator overloading via special methods:
```python
class Query:
    def __init__(self, expr): ...
    def __and__(self, other): return Query(f"({self.expr} AND {other.expr})")
```
  - Function dispatch via functools.singledispatch:
```python
from functools import singledispatch

@singledispatch
def process(x): ...
@process.register
def _(x: int): ...
```

4. Parametric polymorphism (generics)
- Using typing generics to write reusable code across types:
```python
from typing import Generic, TypeVar, List

T = TypeVar("T")
class Repository(Generic[T]):
    def save(self, obj: T): ...
```

5. Coercion polymorphism (implicit conversion)
- Less common in Python, but present via __int__/__float__ and duck-conversion patterns.

Why it matters:
- Enables flexible APIs, decouples code, simplifies testing and extension.

Web dev uses:
- Polymorphic serializers (DRF) that handle multiple model types.
- Request handlers that accept objects implementing required methods (middleware).
- Query builders using operator overloading to chain filters.
- Generic repository/service classes parameterized with model types.
- Versioned APIs serving different payload shapes via polymorphic views/serializers.

Interview gold:
- "Polymorphism allows objects of different classes to be treated uniformly."

---

## 4. Abstraction
What it is:
- Hiding implementation details and exposing only essential operations.

Python example using ABC:
```python
from abc import ABC, abstractmethod

class CacheBackend(ABC):
    @abstractmethod
    def get(self, key): ...
    @abstractmethod
    def set(self, key, value): ...
```

Why it matters:
- Enforces contracts, decouples high-level logic from concrete implementations.

Web dev uses:
- Abstract base classes for storage/cache backends (Redis, in-memory).
- Service interfaces for payment gateways; concrete classes implement details.
- Abstract repository or adapter patterns to isolate DB logic.

Interview line:
- "Abstraction focuses on what an object does, not how it does it."

---

## How These Principles Work Together
- Encapsulation → protects data and internal invariants.
- Inheritance → reuses and specializes behavior.
- Polymorphism → allows interchangeable implementations.
- Abstraction → defines contracts and hides implementation.

Together they form the foundation of clean object-oriented design.

---

## Real-World Web Development Use Cases (concise)
- Authentication & Authorization
  - Encapsulate token handling in AuthService.
  - Mixin-based permissions using multiple inheritance.
  - Polymorphic handlers for different credential types (JWT, OAuth).

- Class-Based Views
  - Base view class (abstraction), mixins for logging/auth (multiple inheritance), different view implementations (polymorphism).

- Serializers & Deserialization
  - Polymorphic serializers for different payload shapes.
  - Abstract serializer interface with concrete model serializers.

- ORMs & Models
  - Encapsulation of field validation; properties for computed fields.
  - Model inheritance for shared fields (BaseTimestampModel → User/Product).
  - Query DSL built with operator overloading for expressive filters.

- Services & Repositories
  - Abstract repository interfaces, concrete SQL/NoSQL implementations.
  - Generic repositories (parametric polymorphism) usable across models.
  - Swap implementations in tests using polymorphism/mocks.

- Middleware & Plugins
  - Middleware base classes (abstraction) and pluggable implementations.
  - Mixins for cross-cutting concerns (rate limiting, metrics).

---

## Common Interview Mistakes
- Mixing up abstraction vs encapsulation.
- Saying Python enforces private access (it uses conventions).
- Ignoring real examples / applying inheritance where composition is better.

Correct mindset:
- "Python encourages OOP through conventions, protocols, and powerful runtime features — design deliberately."

One-line summary:
- "OOP in Python uses encapsulation for safety, inheritance for reuse, polymorphism for flexibility, and abstraction for clean contracts — applied via mixins, ABCs, duck typing, and generics in web development."