In Python, dictionaries store data as key–value pairs. Removing keys is common; choose the method that matches your safety and intent requirements.

## 1. del — direct and strict
Use `del` to remove a key in-place.

```python
data = {"a": 1, "b": 2, "c": 3}
del data["b"]
```

Raises `KeyError` if the key doesn't exist. Best when you are sure the key is present.

> Interview tip: `del` is fast and direct, but unsafe if the key may be missing.

## 2. pop() — safe and returns the value
`pop()` removes a key and returns its value.

```python
data = {"a": 1, "b": 2}
value = data.pop("b")  # value == 2
```

Provide a default to avoid exceptions:

```python
data.pop("x", None)
```

No exception is raised when a default is provided.

> Interview tip: Use `pop()` when you want both removal and the value.

## 3. popitem() — removes the last inserted key
`popitem()` removes and returns the last inserted key–value pair (dicts are ordered since Python 3.7).

```python
data = {"a": 1, "b": 2}
data.popitem()  # removes ("b", 2)
```

Useful for stack-like (LIFO) behavior; not for removing a specific key.

## 4. Dictionary comprehension — non-mutating approach
Create a new dictionary without the undesired key:

```python
data = {"a": 1, "b": 2, "c": 3}
new_data = {k: v for k, v in data.items() if k != "b"}
```

Original `data` remains unchanged.

> Interview tip: Useful in functional or immutable-style programming.

## 5. Clearing all keys
Remove all keys while keeping the dictionary object:

```python
data.clear()
```

The dictionary becomes empty.

## Quick comparison

| Method           | Raises Error?        | Returns Value? | Use Case                         |
|------------------|----------------------|----------------|----------------------------------|
| `del`            | Yes (if missing)     | No             | Key definitely exists            |
| `pop()`          | No (with default)    | Yes            | Safe removal + get the value     |
| `popitem()`      | Yes (if empty)       | Yes            | Remove last item (LIFO)          |
| Comprehension    | No                   | New dict       | Keep original unchanged          |
| `clear()`        | No                   | No             | Remove everything                |
