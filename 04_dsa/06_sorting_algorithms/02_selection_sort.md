# Selection Sort

Selection sort is a comparison-based sorting algorithm where we repeatedly select the smallest element from the unsorted part and place it at the correct position.

> **Key idea:** Find minimum → swap → shrink unsorted part

---

## How It Works (Intuition)

Think of arranging cards in your hand:

1. Look at all cards.
2. Pick the smallest.
3. Put it in the first position.
4. Repeat for the remaining cards.

---

## Step-by-Step Example

Given array:

```
[64, 25, 12, 22, 11]
```

**Pass 1:**  
Smallest = 11  
Swap with first element  
→ `[11, 25, 12, 22, 64]`

**Pass 2:**  
Smallest in remaining = 12  
→ `[11, 12, 25, 22, 64]`

**Pass 3:**  
Smallest = 22  
→ `[11, 12, 22, 25, 64]`

**Pass 4:**  
Smallest = 25  
→ `[11, 12, 22, 25, 64]` ✅

---

## Python Implementation

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print(arr)
```

---

## Time & Space Complexity

| Case    | Time   |
|---------|--------|
| Best    | O(n²)  |
| Average | O(n²)  |
| Worst   | O(n²)  |

- **Space Complexity:** O(1) (in-place)
- **Stable:** ❌ No (because of swapping)
- **Swaps:** Minimal (at most n - 1 swaps)

---

## Bubble Sort vs Selection Sort

| Feature      | Bubble Sort | Selection Sort |
|--------------|-------------|---------------|
| Comparisons  | More        | Same          |
| Swaps        | Many        | Very few      |
| Stable       | Yes         | No            |
| Adaptive     | Yes (optimized) | No        |

---

## When to Use Selection Sort?

**✅ Good for:**
- Understanding sorting logic
- When swap cost is high
- Small datasets

**❌ Not good for:**
- Large datasets
- Already sorted data (still O(n²))

---

💡 **Interview tip:**  
If asked “Why selection sort?” →  
*It minimizes the number of swaps, which is useful when swaps are expensive.*