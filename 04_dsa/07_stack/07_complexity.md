## ⏱ Time Complexity

| Operation         | Complexity |
|-------------------|------------|
| Push              | O(1)       |
| Pop               | O(1)       |
| Peek / Top        | O(1)       |
| IsEmpty           | O(1)       |
| IsFull (array stack) | O(1)    |

> **All core stack operations are constant time.**

---

## 💾 Space Complexity

- **Array-based stack:** `O(n)`
- **Linked-list stack:** `O(n)`

Where `n` = number of elements in the stack.

---

## ⚠️ Special Case: Dynamic Array Stack

- If stack is implemented using a dynamic array:
    - Push is **O(1) amortized**
    - Worst case **O(n)** when resizing happens (array doubles)
- In interviews → still considered **O(1)**.

---

## 🧠 One-line Interview Answer

> “Stack operations like push, pop, and peek take O(1) time, and the space complexity is O(n).”