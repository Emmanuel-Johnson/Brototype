# Using two pointers 

This keeps the result sorted without re-sorting.

```python
def merge_sorted_lists(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    # add remaining elements
    result.extend(a[i:])
    result.extend(b[j:])

    return result
```

### Example

```python
a = [1, 3, 5, 7]
b = [2, 4, 6]

print(merge_sorted_lists(a, b))
```

### Output

```
[1, 2, 3, 4, 5, 6, 7]
```

### ⏱ Time Complexity

- O(n + m) — optimal  
- No extra sorting