# Static Array vs Dynamic Array

## 1️⃣ Static Array

### Meaning

A **static array** has a fixed size decided **before the program runs**. Once created, its size cannot be changed.

### Example

```c
int arr[5];   // size is fixed = 5
```

### Key Points

* Size is fixed
* Memory allocated once
* Cannot grow or shrink
* Faster (no resizing overhead)

### Pros ✅

* Simple
* Fast access
* Less memory overhead

### Cons ❌

* Wastes memory if size is larger than needed
* Cannot add more elements after full

---

## 2️⃣ Dynamic Array

### Meaning

A **dynamic array** can change its size **during runtime**.

### Example

```python
arr = []
arr.append(10)
arr.append(20)
```

**Examples:** Python list, Java `ArrayList`, C++ `vector`

### Key Points

* Size is flexible
* Memory allocated and reallocated
* Can grow and shrink
* Slightly slower due to resizing

### Pros ✅

* Flexible size
* Efficient memory usage
* Easy to add/remove elements

### Cons ❌

* Extra memory used during resizing
* Slight overhead compared to static arrays

---

## 3️⃣ Side-by-Side Comparison

| Feature           | Static Array | Dynamic Array   |
| ----------------- | ------------ | --------------- |
| Size              | Fixed        | Changeable      |
| When size decided | Compile time | Runtime         |
| Memory            | Continuous   | Continuous      |
| Resize            | ❌ No         | ✅ Yes           |
| Speed             | Faster       | Slightly slower |
| Example           | `int arr[5]` | Python list     |

---

## 4️⃣ Time Complexity (Important ⭐)

| Operation       | Static Array   | Dynamic Array |
| --------------- | -------------- | ------------- |
| Access          | O(1)           | O(1)          |
| Insert (end)    | ❌ Not possible | O(1)*         |
| Insert (middle) | O(n)           | O(n)          |

* *Amortized O(1)*

---

## 5️⃣ One-Line Difference (Interview Ready 🎯)

> **Static array has fixed size, dynamic array can change size at runtime.**
