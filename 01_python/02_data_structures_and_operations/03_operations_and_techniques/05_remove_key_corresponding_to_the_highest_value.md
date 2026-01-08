## Practical 1 — Remove one key with highest value (in-place)

```python
my_dict = {"apple": 5, "orange": 6, "banana": 8, "grapes": 10}

max_key = max(my_dict, key=my_dict.get)
my_dict.pop(max_key)

print(my_dict)
```

✅ Output
```py
{'apple': 5, 'orange': 6, 'banana': 8}
```

- Modifies original dictionary  
- Removes only one key

---

## Practical 2 — Remove all keys with highest value (returns new dictionary)

```python
my_dict = {"apple": 5, "orange": 6, "banana": 10, "grapes": 10}

max_value = max(my_dict.values())

result = {k: v for k, v in my_dict.items() if v != max_value}

print(result)
```

✅ Output
```py
{'apple': 5, 'orange': 6}
```

- Keeps original dictionary  
- Removes all max-value keys

---

## Practical 3 — Safe version (handles empty dictionary)

```python
my_dict = {}

if my_dict:
    my_dict.pop(max(my_dict, key=my_dict.get))
```

---

## Interview guidance

- Default answer
```python
my_dict.pop(max(my_dict, key=my_dict.get))
```

- If asked about duplicates
```python
{k: v for k, v in my_dict.items() if v != max(my_dict.values())}
```
