# Common Time Complexities (in Plain Words)

## O(1) — Constant Time

- **Time does NOT change with input size.**
- No matter if N = 10 or N = 1,000,000 → same time.

**Example:**
```python
x = arr[0]
```
- 👉 Always 1 step  
- 👉 O(1)

> 🧠 *Best possible complexity*

---

## O(log N) — Logarithmic Time

- **Time increases very slowly as N increases.**
- Happens when input size is cut in half each step.

**Example:**  
*Binary Search*

Array size:  
16 → 8 → 4 → 2 → 1

- 👉 O(log N)

> 🧠 *Big data, small time*

---

## O(N) — Linear Time

- **Time grows directly with input size.**
- If input doubles, time doubles.

**Example:**
```python
for i in range(n):
    print(i)
```
- 👉 Runs N times  
- 👉 O(N)

> 🧠 *One loop*

---

## O(N log N) — Linearithmic Time

- **A loop (N) with a log operation inside.**
- Common in efficient sorting algorithms.

**Example:**  
*Merge Sort*  
*Quick Sort (average case)*

- 👉 O(N log N)

> 🧠 *Fast sorting complexity*

---

## O(N²) — Quadratic Time

- **Time grows very fast.**
- Usually caused by nested loops.

**Example:**
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
- 👉 N × N operations  
- 👉 O(N²)

> 🧠 *Slow for large data*

---

## Easiest Way to Remember 🔥

| Complexity   | Think of         |
|--------------|------------------|
| O(1)         | Direct access    |
| O(log N)     | Divide by 2      |
| O(N)         | Single loop      |
| O(N log N)   | Efficient sorting|
| O(N²)        | Nested loops     |

---

## Interview Ranking (Best → Worst)

**O(1) → O(log N) → O(N) → O(N log N) → O(N²)**

> Loops decide time complexity. Nested loops make it worse.