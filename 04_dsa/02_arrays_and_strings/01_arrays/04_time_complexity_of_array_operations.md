# Time Complexity of Array Operations

*Assume array size = **N***

---

## 1️⃣ Access (Read / Write)

```text
arr[i]
```

**⏱ Time Complexity:** `O(1)`

**Why?**
Arrays store elements in continuous memory, so index access is direct.

---

## 2️⃣ Traversal

```python
for i in arr:
    print(i)
```

**⏱ Time Complexity:** `O(N)`

**Why?**
Every element is visited once.

---

## 3️⃣ Insertion

### a) At the End

```text
arr[N] = x
```

**⏱ Time Complexity:** `O(1)`
⚠️ Only true **if space is available**

---

### b) At the Beginning

Insert at index `0`

**⏱ Time Complexity:** `O(N)`

**Why?**
All elements must shift one position to the right.

---

### c) At a Middle Position

Insert at index `k`

**⏱ Time Complexity:** `O(N)`

**Why?**
Elements after index `k` must shift.

---

## 4️⃣ Deletion

### a) From the End

**⏱ Time Complexity:** `O(1)`

---

### b) From the Beginning

**⏱ Time Complexity:** `O(N)`

**Why?**
All elements must shift left.

---

### c) From the Middle

**⏱ Time Complexity:** `O(N)`

---

## 5️⃣ Searching

### a) Linear Search (Unsorted Array)

**⏱ Time Complexity:** `O(N)`

**Worst case:** element is last or not present.

---

### b) Binary Search (Sorted Array)

**⏱ Time Complexity:** `O(log N)`

👉 Requires array to be **sorted**

---

## 6️⃣ Summary Table ⭐

| Operation             | Time Complexity |
| --------------------- | --------------- |
| Access                | O(1)            |
| Traversal             | O(N)            |
| Insert at end         | O(1)            |
| Insert at beginning   | O(N)            |
| Insert at middle      | O(N)            |
| Delete from end       | O(1)            |
| Delete from beginning | O(N)            |
| Delete from middle    | O(N)            |
| Linear search         | O(N)            |
| Binary search         | O(log N)        |

---

## 7️⃣ One-Line Rule to Remember 🎯

> **Shifting elements = O(N)**
> **Direct index access = O(1)**
