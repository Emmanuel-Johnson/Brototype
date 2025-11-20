### 1. OOP – Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into classes and objects, allowing us to structure programs like real-world entities. Instead of writing large procedural code, OOP lets us group related data (attributes) and behavior (methods) inside objects, which improves modularity, reusability, maintainability, and readability. OOP is built on four main principles — Encapsulation, Inheritance, Polymorphism, and Abstraction, which together help create scalable and flexible applications. Python is fully object-oriented, meaning almost everything — numbers, functions, modules — is treated as an object.

### 2. Class

A class is a blueprint or template for creating objects. It defines what data an object will store (attributes) and what operations it can perform (methods). You can think of a class as a design plan — it doesn’t occupy memory until an object is created from it. Classes support access modifiers, constructors (__init__), and different types of methods such as instance, class, and static methods, making them core building blocks of OOP.

### 3. Object

An object is an instance of a class, meaning it is a concrete entity created using the class blueprint. Each object gets its own copy of instance variables but shares class variables defined at the class level. Objects can call methods defined in the class and represent real-world entities like a Car, Employee, or Account. When an object is created, Python automatically calls the __init__ method to initialize its attributes.

### 4. Encapsulation

Encapsulation is the process of bundling data and methods into a single unit (a class) and restricting direct access to internal details to protect the integrity of data. Python supports three access levels: public (default), protected (single underscore _), and private (double underscore __). Public members are accessible everywhere, protected members are meant for the class and its subclasses, and private members are only accessible inside the class. Encapsulation ensures data security, prevents misuse, and makes code easier to maintain.

### 5. Inheritance (All Types)

Inheritance allows a class (child) to reuse and extend the properties and methods of another class (parent), promoting code reusability and reducing duplication. Single inheritance involves one parent and one child class. Multiple inheritance allows a class to inherit from more than one parent class. Multilevel inheritance forms a hierarchy where a child becomes the parent of another child. Hierarchical inheritance means one parent has multiple child classes. Hybrid inheritance is a combination of multiple forms of inheritance. Python resolves conflicts (like the diamond problem) using Method Resolution Order (MRO) via the C3 linearization algorithm.

### 6. Polymorphism (All Types)

Polymorphism means one interface, many forms, allowing the same method or operator to behave differently depending on the object. Python supports two types: Compile-time polymorphism (implemented through method overloading using default arguments or *args, since Python doesn’t support true overloading), and Runtime polymorphism, which is achieved through method overriding — where a subclass provides its own version of a parent method. Python also supports operator overloading using magic methods like __add__, __len__, and __eq__, enabling custom behaviors for built-in operators. Polymorphism increases flexibility and makes functions work with multiple object types.

### 7. Abstraction

Abstraction focuses on showing only essential features while hiding complex internal details. It simplifies user interaction by exposing only necessary methods. In Python, abstraction is implemented using Abstract Base Classes (ABC) and the @abstractmethod decorator from the abc module. When you define an abstract method, all subclasses must implement it, ensuring consistency. Abstraction helps reduce complexity, provides clear interfaces, and allows developers to modify internal implementation without affecting external code.
