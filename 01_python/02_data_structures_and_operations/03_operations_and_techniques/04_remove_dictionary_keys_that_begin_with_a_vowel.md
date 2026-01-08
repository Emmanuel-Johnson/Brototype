You cannot safely modify a dictionary while iterating over it. Two safe options:

- Collect keys to remove, then delete them.
- Or create a new dictionary (one-liner).

## Example — collect keys then delete

```python
data = {
    "apple": 10,
    "banana": 20,
    "orange": 30,
    "grape": 40,
    "umbrella": 50
}

vowels = {'a', 'e', 'i', 'o', 'u'}

# Step 1: find keys to remove
keys_to_remove = [k for k in data if k[0].lower() in vowels]

# Step 2: remove them
for k in keys_to_remove:
    del data[k]

print(data)
```

Output:
```
{'banana': 20, 'grape': 40}
```

## One-liner (dictionary comprehension)

If creating a new dictionary is acceptable:

```python
data = {
    "apple": 10,
    "banana": 20,
    "orange": 30,
    "grape": 40,
    "umbrella": 50
}

data = {k: v for k, v in data.items() if k[0].lower() not in 'aeiou'}
```

Notes:
- Deleting while iterating raises a runtime error; collecting keys avoids that.
- Dictionary comprehension is clean and interview-friendly but creates a new dict.
- Both approaches are O(n) time and O(n) extra space if you account for the keys list or new dict.