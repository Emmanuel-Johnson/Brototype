# Insertion Sort

Insertion sort builds a sorted array one element at a time by taking the next element and inserting it into its correct position in the already-sorted part.

> **Think of arranging playing cards in your hand.**

---

## How It Works (Intuition)

1. Assume the first element is already sorted.
2. Pick the next element (key).
3. Shift larger elements one step right.
4. Insert the key at the correct position.

---

## Step-by-Step Example

**Array:**  
`[8, 3, 5, 2]`

- **Pass 1**  
    Sorted: `[8]`  
    Insert 3 → `[3, 8, 5, 2]`

- **Pass 2**  
    Sorted: `[3, 8]`  
    Insert 5 → `[3, 5, 8, 2]`

- **Pass 3**  
    Sorted: `[3, 5, 8]`  
    Insert 2 → `[2, 3, 5, 8]` ✅

---

## Python Implementation

```python
def insertion_sort(arr):
        n = len(arr)
        for i in range(1, n):
                key = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > key:
                        arr[j + 1] = arr[j]
                        j -= 1
                arr[j + 1] = key

arr = [8, 3, 5, 2]
insertion_sort(arr)
print(arr)
```

---

## Time & Space Complexity

| Case                  | Time   |
|-----------------------|--------|
| Best (already sorted) | O(n)   |
| Average               | O(n²)  |
| Worst (reverse)       | O(n²)  |

- **Space Complexity:** O(1) (in-place)
- **Stable:** ✅ Yes
- **Adaptive:** ✅ Yes (faster for nearly sorted arrays)

---

## Comparison with Bubble & Selection Sort

| Feature   | Bubble | Selection | Insertion |
|-----------|:------:|:---------:|:---------:|
| Stable    |   ✅   |     ❌    |    ✅     |
| Adaptive  |   ✅   |     ❌    |    ✅     |
| Swaps     |  Many  |    Few    |  Shifts   |
| Best Case |  O(n)  |   O(n²)   |   O(n)    |

> Insertion sort is usually the best among the three for small or nearly sorted data.

---

## When to Use Insertion Sort?

**✅ Best for:**
- Nearly sorted arrays
- Small datasets
- Online sorting (data coming one by one)

**❌ Not good for:**
- Very large datasets

---

## Interview Gold Line ✨

> “Insertion sort is efficient for small or nearly sorted datasets because it minimizes comparisons and shifts.”