“In Python, a destructor is a special method named `__del__`. It is called when an object is about to be destroyed, and it is mainly used for cleanup operations.”

## What is `__del__`?
- `__del__` stands for "delete".
- Called when an object’s reference count becomes zero (or when GC collects it).
- Used to release external resources.

Example:
```python
class FileHandler:
    def __del__(self):
        print("Object is being destroyed")
```

> Interview line: “`__del__` is invoked when Python garbage-collects an object.”

## When is `__del__` called?
```python
obj = FileHandler()
del obj
```
- `del` removes a reference, not the object itself.
- The object is destroyed only if no references remain.

> Key interview point: “`del` deletes a reference, not the object itself.”

## Why use destructors?
Used mainly for cleanup of non-memory resources:
- Closing files
- Releasing database connections
- Freeing network or system resources

Example:
```python
class Database:
    def __del__(self):
        self.connection.close()
```

> Interview line: “Destructors are used for cleanup of non-memory resources.”

## Destructor vs Garbage Collection
- Python uses automatic garbage collection.
- Destructor execution time is not guaranteed.
- Depends on reference counting and the garbage collector.

> Warning: “`__del__` should not be relied on for critical cleanup.”

## Constructor vs Destructor

| Constructor (`__init__`) | Destructor (`__del__`) |
|---|---|
| Initializes object | Cleans up object |
| Called on creation | Called on deletion |
| Predictable | Non-deterministic |

## Common interview pitfalls
❌ Assuming `__del__` runs immediately  
❌ Using it for critical logic  
❌ Depending on it for closing important resources

Correct approach: Use context managers (`with`) instead of destructors for reliable cleanup.

## Advanced point — Reference cycles
- Objects in circular references may delay or skip `__del__`.
- The garbage collector may not call destructors predictably for cycles.

> “Reference cycles can prevent predictable destructor execution.”

## Should we use `__del__` in real projects?
Short answer: Rarely. Prefer context managers and explicit cleanup.

> One-line interview summary:  
> “The `__del__` method is a destructor in Python that is called during garbage collection to clean up resources, but its execution timing is not guaranteed.”
