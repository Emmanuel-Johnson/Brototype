# Flatten any depth

Recursively flatten a nested list of arbitrary depth.

```python
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

nested = [1, [2, [3, 4], 5], 6]
print(flatten(nested))
```

✅ Output:

```
[1, 2, 3, 4, 5, 6]
```

Notes:
- ✔ Handles deeply nested lists
- ✔ Useful for interview questions and quick scripts