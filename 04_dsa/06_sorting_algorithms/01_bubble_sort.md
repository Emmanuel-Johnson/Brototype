# Bubble Sort

Bubble sort is a simple comparison-based sorting algorithm. It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they’re in the wrong order. Big elements “bubble up” to the end — that’s where the name comes from.

## How It Works (Intuition)

Think of numbers as bubbles in water:

- Heavier (larger) bubbles go upwards (towards the end of the array)
- Each pass pushes one largest element to its correct position

## Step-by-Step Example

**Array:**  
`[5, 3, 8, 4]`

**Pass 1**
- Compare 5 & 3 → swap → `[3, 5, 8, 4]`
- Compare 5 & 8 → no swap
- Compare 8 & 4 → swap → `[3, 5, 4, 8]`  
    ➡️ Largest element 8 is now fixed at the end

**Pass 2**
- Compare 3 & 5 → no swap
- Compare 5 & 4 → swap → `[3, 4, 5, 8]`

**Pass 3**
- No swaps → array is sorted ✅

## Python Implementation

```python
def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
                for j in range(0, n - i - 1):
                        if arr[j] > arr[j + 1]:
                                arr[j], arr[j + 1] = arr[j + 1], arr

arr = [5, 3, 8, 4]
bubble_sort(arr)
print(arr)
```

## Optimized Version (Important for Interviews 👀)

Stop early if no swaps happen in a pass.

```python
def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
                swapped = False
                for j in range(0, n - i - 1):
                        if arr[j] > arr[j + 1]:
                                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                                swapped = True
                if not swapped:
                        break
```

## Time & Space Complexity

| Case                  | Time   |
|-----------------------|--------|
| Best (already sorted) | O(n)   |
| Average               | O(n²)  |
| Worst                 | O(n²)  |

- **Space Complexity:** O(1) (in-place)
- **Stable:** ✅ Yes

## When to Use Bubble Sort?

**✅ Good for:**
- Learning sorting basics
- Very small datasets
- Interview explanation clarity

**❌ Not good for:**
- Large datasets
- Performance-critical systems
