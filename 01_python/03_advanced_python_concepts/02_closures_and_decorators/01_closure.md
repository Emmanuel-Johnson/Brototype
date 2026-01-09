> “A closure in Python is a function that remembers variables from its enclosing scope, even after that outer function has finished executing.”

## What is a closure?

In Python, functions are first-class objects — meaning they can be returned from other functions, stored in variables, and passed as arguments.

A closure occurs when:
- a nested function is defined inside another function
- the inner function uses variables from the outer function
- the outer function returns the inner function

Even after the outer function finishes, the inner function still remembers those variables.

## Simple example
```python
def outer(msg):
    def inner():
        print(msg)
    return inner

fn = outer("Hello")
fn()   # Output: Hello
```

Here, `outer()` has finished executing but `inner()` still remembers `msg`. That remembered value is stored in the closure.

## Why does this work?

Python stores referenced variables (not copies) in the closure environment, so they are not destroyed when the outer function exits.

You can inspect the closure:
```python
print(fn.__closure__)
```

## Key properties of closures
- Remembers free variables (variables not local to the inner function)  
- Keeps those variables alive in memory  
- Is read-only by default — to modify captured variables, use `nonlocal`

## Modifying closure variables (`nonlocal`)
```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```
Without `nonlocal`, Python treats `count` as a new local variable and raises an error.

## Real-world use cases

1. Data hiding (encapsulation)

```python
def bank_account(balance):
    def withdraw(amount):
        nonlocal balance
        balance -= amount
        return balance
    return withdraw

acct = bank_account(100)
acct(10)  # 90
```
`balance` cannot be accessed directly — only via `withdraw()`.

2. Function factories

```python
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```

3. Decorators (built using closures)

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say():
    print("Hello")

say()
# Output:
# Before
# Hello
# After
```
