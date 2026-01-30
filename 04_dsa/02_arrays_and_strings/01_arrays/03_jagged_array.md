# Jagged Array

## What is a Jagged Array?

A **jagged array** is an array of arrays where **each row can have a different size**.

👉 Unlike a normal 2D array, rows are **not equal in length**.

---

## Visual Example

```
Row 0 → [1, 2, 3]
Row 1 → [4, 5]
Row 2 → [6, 7, 8, 9]
```

Here:

* Row 0 has **3** elements
* Row 1 has **2** elements
* Row 2 has **4** elements

👉 This structure is a **jagged array**

---

## Example in Code

### Python

```python
jagged = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
]
```

### Java

```java
int[][] jagged = new int[3][];
jagged[0] = new int[]{1, 2, 3};
jagged[1] = new int[]{4, 5};
jagged[2] = new int[]{6, 7, 8, 9};
```

---

## Jagged Array vs 2D Array

| Feature     | 2D Array          | Jagged Array           |
| ----------- | ----------------- | ---------------------- |
| Row size    | Same for all rows | Different for each row |
| Structure   | Rectangle         | Irregular              |
| Memory      | Can waste space   | More memory-efficient  |
| Flexibility | Less              | More                   |

---

## Why Use Jagged Array?

* When data rows are **not equal in size**
* To **save memory**
* Useful for real-world data such as:

  * Students with different subject counts
  * Graph adjacency lists
  * Monthly sales (different number of days)

---

## Time Complexity

* **Access element:** `O(1)` → `jagged[row][col]`
* **Traversal:** `O(total elements)`

---

## One-Line Definition (Exam Ready 🎯)

> **A jagged array is an array of arrays where each inner array can have a different length.**
