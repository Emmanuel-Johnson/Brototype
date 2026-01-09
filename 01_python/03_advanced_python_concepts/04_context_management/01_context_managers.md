A context manager is an object that manages resources for you (for example: files, database connections, network sockets, locks). The pattern is: set something up → use it → clean it up automatically, even if an error occurs.

## Why do we need context managers?

Without a context manager you might write:

```python
file = open("data.txt", "r")
data = file.read()
file.close()
```

Problem: if an exception occurs before `file.close()`, the file remains open, which can cause resource leaks. Context managers give a safer pattern.

## The `with` statement

The `with` statement is used to work with context managers:

```python
with open("data.txt", "r") as file:
    data = file.read()
```

What happens:
- The file is opened when entering the block.
- The file is automatically closed when exiting the block, even if an exception occurs.
- Result: cleaner, safer, more readable code.

## How `with` works internally

A context manager implements two special methods: `__enter__()` and `__exit__()`.

Execution flow:

1. `resource = manager.__enter__()`
2. try:
       # use resource
   finally:
       `manager.__exit__()`

`__enter__()` runs when entering the `with` block. `__exit__()` runs when leaving the block (including on errors).

## Simple custom context manager (class-based)

```python
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

with MyContext():
    print("Inside block")
```

Output:
```
Entering context
Inside block
Exiting context
```

`__exit__` runs no matter what — even if an exception occurs.

## Context manager using `contextlib`

For simple setup/cleanup logic, `contextlib` provides a decorator-based approach:

```python
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Enter")
    try:
        yield
    finally:
        print("Exit")

with my_context():
    print("Inside")
```

This pattern is often preferred for concise context managers.

## Real-world uses

Common use cases:
- File handling (`open`)
- Database connections and transactions
- Thread locks (`with lock:`)
- Network sockets
- Measuring execution time / profiling

## Key interview summary (one-liner)

“A context manager in Python is an object that manages resources using `__enter__` and `__exit__`, and the `with` statement ensures automatic setup and cleanup, making code safer and cleaner.”
