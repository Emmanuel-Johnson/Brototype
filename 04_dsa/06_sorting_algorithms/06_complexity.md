Time & Space Complexity

## 🫧 Bubble Sort

| Case                         | Time   |
|------------------------------|--------|
| Best (already sorted, optimized) | O(n)   |
| Average                      | O(n²)  |
| Worst                        | O(n²)  |

- **Space:** O(1) (in-place)
- **Stable:** ✅
- **Adaptive:** ✅ (with swapped flag)

---

## 🔍 Selection Sort

| Case    | Time   |
|---------|--------|
| Best    | O(n²)  |
| Average | O(n²)  |
| Worst   | O(n²)  |

- **Space:** O(1) (in-place)
- **Stable:** ❌
- **Adaptive:** ❌

> Time is always n² because it always scans the remaining array.

---

## ✋ Insertion Sort

| Case                | Time   |
|---------------------|--------|
| Best (already sorted) | O(n)   |
| Average             | O(n²)  |
| Worst (reverse sorted) | O(n²)  |

- **Space:** O(1) (in-place)
- **Stable:** ✅
- **Adaptive:** ✅

---

## ⚔️ Merge Sort

| Case    | Time        |
|---------|-------------|
| Best    | O(n log n)  |
| Average | O(n log n)  |
| Worst   | O(n log n)  |

- **Space:** O(n) ❗ (extra arrays)
- **Stable:** ✅
- **Adaptive:** ❌

> Always divides evenly → guaranteed performance.

---

## ⚡ Quick Sort

| Case    | Time        |
|---------|-------------|
| Best    | O(n log n)  |
| Average | O(n log n)  |
| Worst   | O(n²) ❗     |

- **Space:** O(log n) (recursion stack)
- **Stable:** ❌
- **Adaptive:** ❌

> ⚠️ Worst case when pivot is always smallest/largest.

---

## 🧠 One-Glance Comparison Table (Interview Gold)

| Algorithm  | Best        | Avg         | Worst      | Space    |
|------------|-------------|-------------|------------|----------|
| Bubble     | O(n)        | O(n²)       | O(n²)      | O(1)     |
| Selection  | O(n²)       | O(n²)       | O(n²)      | O(1)     |
| Insertion  | O(n)        | O(n²)       | O(n²)      | O(1)     |
| Merge      | O(n log n)  | O(n log n)  | O(n log n) | O(n)     |
| Quick      | O(n log n)  | O(n log n)  | O(n²)      | O(log n) |

---

## 🎯 How to answer in interviews (short & sharp)

- **Small / nearly sorted data?** → Insertion Sort
- **Guaranteed performance needed?** → Merge Sort
- **Fast in practice, in-place?** → Quick Sort
- **Learning basics?** → Bubble / Selection

<br>
<br>
<br>

## 🧩 Sorting Algorithms: Properties Table (Stable · In-Place · Adaptive)

| Algorithm      | Stable | In-Place | Adaptive |
|----------------|--------|----------|----------|
| Bubble Sort    | ✅ Yes | ✅ Yes   | ✅ Yes*  |
| Selection Sort | ❌ No  | ✅ Yes   | ❌ No    |
| Insertion Sort | ✅ Yes | ✅ Yes   | ✅ Yes   |
| Merge Sort     | ✅ Yes | ❌ No    | ❌ No    |
| Quick Sort     | ❌ No  | ✅ Yes** | ❌ No    |

---

## 🔍 Tiny Interview Notes (Very Important)

**Stable**  
👉 Maintains relative order of equal elements  
Example: (5a, 5b) stays (5a, 5b)

**In-Place**  
👉 Uses constant extra space (ignoring recursion stack)

**Adaptive**  
👉 Runs faster when input is already / nearly sorted

---

## ⚠️ Footnotes (Interview Traps)

- **Bubble Sort adaptive?**  
    ✅ Only with swapped flag optimization

- **Quick Sort in-place?**  
    ✅ Yes, but uses O(log n) recursion stack  
    (Still considered in-place in interviews)

- **Merge Sort in-place?**  
    ❌ No — needs extra arrays → O(n) space

---

## 🎯 One-Line Interview Answer

“Insertion and Bubble are stable, in-place, and adaptive;  
Selection is in-place but neither stable nor adaptive;  
Merge is stable but not in-place;  
Quick is in-place but not stable or adaptive.”