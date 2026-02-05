# Merge Sort

Merge Sort is a classic **divide-and-conquer** sorting algorithm.

Instead of sorting directly, it:

1. **Divides** the array into halves  
2. **Sorts** each half recursively  
3. **Merges** the sorted halves back together  

---

## Big Idea (Intuition)

> “If I can sort small pieces easily, I can merge them to get a sorted big piece.”

This fits perfectly with recursion thinking (which you’ve been practicing 👀).

---

## How It Works (High Level)

Given the array:

```
[38, 27, 43, 3, 9, 82, 10]
```

**Divide:**

```
[38, 27, 43, 3]   [9, 82, 10]
```

**Divide again:**

```
[38, 27] [43, 3]   [9] [82, 10]
```

**Divide until single elements:**

```
[38] [27] [43] [3] [9] [82] [10]
```

**Merge back (sorted):**

```
[27, 38] [3, 43] [9] [10, 82]
→ [3, 27, 38, 43] [9, 10, 82]
→ [3, 9, 10, 27, 38, 43, 82]
```

✅ **Fully sorted!**

---

## Python Implementation

```python
def merge_sort(arr):
    if len(arr) <= 1:   # base case
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(arr))
```

---

## Why Recursion Feels Natural Here

- **Base case:** array of size 0 or 1 is already sorted  
- **Recursive case:** sort left half + sort right half  
- **Merge step:** combine results  

This is a perfect example of a “problem naturally recursive” 👍

---

## Time & Space Complexity

| Case     | Time      |
|----------|-----------|
| Best     | O(n log n)|
| Average  | O(n log n)|
| Worst    | O(n log n)|

- **Space Complexity:** O(n) ❗ (extra array)
- **Stable:** ✅ Yes
- **In-place:** ❌ No (standard version)

---

## Comparison with Earlier Sorts

| Algorithm  | Time      | Space | Stable |
|------------|-----------|-------|--------|
| Bubble     | O(n²)     | O(1)  | ✅     |
| Selection  | O(n²)     | O(1)  | ❌     |
| Insertion  | O(n²)     | O(1)  | ✅     |
| Merge      | O(n log n)| O(n)  | ✅     |

👉 This is where sorting becomes serious.

---

## When to Use Merge Sort?

**✅ Best for:**
- Large datasets
- Linked lists
- When guaranteed performance matters

**❌ Not ideal when:**
- Memory is very limited
- In-place sorting is required

---

## Interview Killer Line 💣

> “Merge sort guarantees O(n log n) time in all cases because it divides the array evenly and merges in linear time.”