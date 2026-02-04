# Linear Search

**Idea:** Check elements one by one from start to end.

### ⏱ Time Complexity

- **Best case:** O(1) — element found at the first position
- **Average case:** O(n)
- **Worst case:** O(n) — element at last position or not present

### 💾 Space Complexity

- O(1) (no extra space)

### ✅ Notes

- Works on sorted or unsorted arrays
- Simple, but slow for large data

---

# Binary Search

**Idea:** Repeatedly divide the array into halves.

### ⏱ Time Complexity

- **Best case:** O(1) — element is at the middle
- **Average case:** O(log n)
- **Worst case:** O(log n)

### 💾 Space Complexity

- **Iterative:** O(1)
- **Recursive:** O(log n) (call stack)

### ⚠️ Notes

- Array must be sorted
- Much faster for large datasets

---

# Quick Comparison

| Feature      | Linear Search | Binary Search      |
|--------------|--------------|-------------------|
| Data order   | Any          | Must be sorted    |
| Time (worst) | O(n)         | O(log n)          |
| Space        | O(1)         | O(1) / O(log n)   |
| Speed        | Slower       | Faster            |

---

**Rule of thumb:**

- Small or unsorted data → **Linear Search**
- Large, sorted data → **Binary Search**