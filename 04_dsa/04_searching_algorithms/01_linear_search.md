```python
arr = [1, 2, 3, 2, 1, 8, 9, 1, 7]

def linear_search(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            return i
    return -1

print(linear_search(arr, 8))
```