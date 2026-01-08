## 1) Example range
```python
evens = [i for i in range(-20, 0) if i % 2 == 0]
print(evens)
```

Output:
```text
[-20, -18, -16, -14, -12, -10, -8, -6, -4, -2]
```

## 2) General form (easy to explain in interviews)
```python
even_negatives = [x for x in numbers if x < 0 and x % 2 == 0]
```

## 3) One-liner with step (most efficient)
```python
evens = list(range(-2, -21, -2))
```
