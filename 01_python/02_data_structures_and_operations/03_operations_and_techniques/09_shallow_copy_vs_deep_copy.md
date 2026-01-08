In Python, copying objects is important when working with mutable types (lists, dicts, sets). There are two main approaches:

## Shallow copy

A shallow copy creates a new outer object but reuses references to nested objects.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 100
print(original)  # [[100, 2], [3, 4]]

shallow.append([5, 6])
print(original)  # [[100, 2], [3, 4]]  # outer append does not affect original
```

Key idea: the top-level container is copied; nested objects are shared.

## Deep copy

A deep copy duplicates the outer object and all nested objects recursively, so nothing is shared.

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 100
print(original)  # [[1, 2], [3, 4]]
```

Key idea: deep copy produces a fully independent copy of the entire object graph.

## How to create copies in Python

Method | Type
--- | ---
`list.copy()` | Shallow
`dict.copy()` | Shallow
`copy.copy(obj)` | Shallow
`copy.deepcopy(obj)` | Deep

## When to use which

Use shallow copy when:
- Data is flat (no nested mutable objects)
- Performance and memory matter

Use deep copy when:
- You have nested mutable structures
- You need complete isolation between objects

> Shallow copy duplicates the container but shares inner objects; deep copy duplicates everything recursively, ensuring full independence.
