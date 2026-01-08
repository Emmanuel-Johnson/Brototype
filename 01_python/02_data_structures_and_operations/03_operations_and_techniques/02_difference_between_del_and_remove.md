# Difference between `del` and `remove()` in Python

In Python, `del` and `remove()` both delete things, but they differ in what they delete and how they operate.

## `del` — deletes by reference or index
- `del` is a statement, not a function.
- It removes a variable, an item at a specific index, a slice, or a dictionary key.

Example with a list:
```python
nums = [10, 20, 30, 40]
del nums[1]
print(nums)  # [10, 30, 40]
```

You can also delete a variable:
```python
x = 100
del x
# using x now raises NameError
```

> ⚠️ After `del x`, using `x` will raise `NameError`.

## `remove()` — deletes by value
- `remove()` is a list method.
- It removes the first occurrence of a given value from a list.

Example:
```python
nums = [10, 20, 30, 20]
nums.remove(20)
print(nums)  # [10, 30, 20]
```

> ⚠️ If the value is not present, `remove()` raises `ValueError`.

## Key differences (interview gold ⭐)

| Feature             | `del`                      | `remove()`           |
|---------------------|----------------------------|----------------------|
| Type                | Statement                  | Method               |
| Deletes by          | Index / reference          | Value                |
| Works on            | Variables, lists, dicts, slices | Lists only      |
| Removes first match | ❌                         | ✅                   |
| Error if not found  | `IndexError` / `NameError` | `ValueError`         |

## When to use
- Use `del` when:
    - You know the index
    - You want to delete a variable, slice, or dict key
    - You want faster deletion by position

- Use `remove()` when:
    - You know the value
    - You don’t know the index
    - You want to remove the first occurrence

## One-line summary
`del` deletes by position or reference (and works beyond lists), while `remove()` deletes by value and works only on lists.
