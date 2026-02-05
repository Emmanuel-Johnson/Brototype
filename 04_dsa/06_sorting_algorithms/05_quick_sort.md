# Quick Sort

Quick Sort is a divide-and-conquer sorting algorithm. Unlike merge sort, it doesn’t require extra arrays. It works by choosing a **pivot** and rearranging elements so that:

- Elements smaller than the pivot go to the left
- Elements greater than the pivot go to the right

Then, it recursively sorts the left and right parts.

---

## Intuition

> Put one element in its correct position, then sort the rest.

Once the pivot is placed correctly, it never moves again.

---

## Step-by-Step Example

**Given array:**  
`[10, 7, 8, 9, 1, 5]`

1. **Choose pivot:** last element → `5`
2. **Partition:**  
    `[1] 5 [10, 7, 8, 9]`
3. **After partition:**  
    `[1, 5, 10, 7, 8, 9]`
4. **Recursively sort:**  
    - Left: `[1]`  
    - Right: `[10, 7, 8, 9]`
5. **Final sorted array:**  
    `[1, 5, 7, 8, 9, 10]`

---

## Python Implementation (Lomuto Partition)

```python
def quick_sort(arr, low, high):
     if low < high:
          pivot_index = partition(arr, low, high)
          quick_sort(arr, low, pivot_index - 1)
          quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
     pivot = arr[high]
     i = low - 1
     for j in range(low, high):
          if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
     arr[i + 1], arr[high] = arr[high], arr[i + 1]
     return i + 1

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
```

---

## Why Quick Sort is Fast in Practice

- No extra memory like merge sort
- Good cache performance
- Fewer comparisons on average

That’s why real-world libraries love it.

---

## Time & Space Complexity

| Case    | Time        |
|---------|-------------|
| Best    | O(n log n)  |
| Average | O(n log n)  |
| Worst   | O(n²) ❗     |

- **Space Complexity:** O(log n) (recursion stack)
- **Stable:** No
- **In-place:** Yes

---

### ⚠️ Worst Case

Occurs when:
- Pivot is always smallest or largest
- Array is already sorted (with bad pivot choice)

---

### How to Avoid Worst Case (Interview Tip)

- Use a random pivot
- Median-of-three pivot
- Hybrid: Quick Sort + fallback to Heap/Merge

> **Note:** Python’s `sorted()` uses Timsort, not quick sort.

---

## Quick Sort vs Merge Sort

| Feature      | Quick Sort   | Merge Sort   |
|--------------|-------------|-------------|
| Avg Time     | O(n log n)  | O(n log n)  |
| Worst Time   | O(n²)       | O(n log n)  |
| Space        | O(log n)    | O(n)        |
| Stable       | ❌           | ✅           |
| In-place     | ✅           | ❌           |

---

> **Interview killer line:**  
> “Quick sort is preferred in practice because of its in-place nature and cache efficiency, even though merge sort has better worst-case guarantees.”