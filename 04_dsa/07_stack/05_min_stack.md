# 📦 Min Stack

A **Min Stack** is a special stack that supports retrieving the minimum element in **O(1)** time, along with normal stack operations.

---

## ✅ Operations (All O(1))

- `push(x)`
- `pop()`
- `top()`
- `getMin()` → returns the minimum element currently in the stack

---

## 🧠 Core Idea (Most Common Approach)

Use **two stacks**:

- `mainStack` → stores all values
- `minStack` → stores the minimums so far

**Rules:**

- **When pushing:**
    - Push to `mainStack`
    - Push to `minStack` only if it’s empty or `x <= currentMin`
- **When popping:**
    - Pop from `mainStack`
    - If popped value == `minStack.top()`, also pop `minStack`

---

## 🧪 Example Walkthrough

Push sequence: `5, 3, 7, 3`

| Operation | mainStack   | minStack  |
|-----------|-------------|-----------|
| push 5    | 5           | 5         |
| push 3    | 5, 3        | 5, 3      |
| push 7    | 5, 3, 7     | 5, 3      |
| push 3    | 5, 3, 7, 3  | 5, 3, 3   |

- `getMin()` → **3**

---

## 🧩 Python Implementation

```python
class MinStack:
        def __init__(self):
                self.stack = []
                self.min_stack = []

        def push(self, x):
                self.stack.append(x)
                if not self.min_stack or x <= self.min_stack[-1]:
                        self.min_stack.append(x)

        def pop(self):
                if self.stack:
                        if self.stack[-1] == self.min_stack[-1]:
                                self.min_stack.pop()
                        self.stack.pop()

        def top(self):
                return self.stack[-1] if self.stack else None

        def getMin(self):
                return self.min_stack[-1] if self.min_stack else None
```

---

## ⚠️ Common Interview Traps

- ❌ Using `min()` → O(n) (wrong)
- ❌ Forgetting to handle duplicate minimums
- ❌ Not syncing `minStack` during pop

---

## 🧠 One-line Memory Hook

> **Min Stack = Normal Stack + History of Minimums**