# How Time Complexity is Calculated

**Time complexity** describes how the running time of an algorithm grows as the input size (`N`) increases.

## Steps to Calculate Time Complexity

1. **Decide what N is:**  
    (e.g., array length, number of elements, etc.)

2. **Find the main operation:**  
    (e.g., comparison, loop step, calculation)

3. **Count how many times that operation runs as N grows.**

4. **Express the result using Big-O notation.**

### Example

```python
for i in range(n):
     print(i)
```

- The loop runs `n` times.
- Time grows directly with `n`.  
  👉 **Time complexity = O(N)**

If there are two nested loops:

```python
for i in range(n):
     for j in range(n):
          print(i, j)
```

- Runs `n × n` times.  
  👉 **Time complexity = O(N²)**

---

# How Space Complexity is Calculated

**Space complexity** measures how much extra memory an algorithm uses as `N` grows.

- Only count extra memory (not the input itself).

## Steps to Calculate Space Complexity

1. **Look for extra variables, arrays, objects, recursion stack.**
2. **See how that memory grows with input size.**
3. **Express it in Big-O notation.**

### Example 1: Constant Space

```python
sum = 0
for i in range(n):
     sum += i
```

- Only one variable used.
- Memory does **not** grow with `n`.  
  👉 **Space complexity = O(1)**

### Example 2: Linear Space

```python
arr = []
for i in range(n):
     arr.append(i)
```

- Array size grows with `n`.  
  👉 **Space complexity = O(N)**

---

## One-line Difference (Easy to Remember)

- **Time complexity:** How long the code takes.
- **Space complexity:** How much extra memory it needs.

> Loops affect time, data structures affect space.