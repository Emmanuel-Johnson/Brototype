```python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binary_search(arr, value):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
    return -1

print(binary_search(arr, 8))
```