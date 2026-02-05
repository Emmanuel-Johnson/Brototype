## 1. WHAT
A **stack** is a linear data structure used to store elements in a **Last In, First Out (LIFO)** order.  
It allows insertion and removal of elements only from one end, called the **top**.

---

## 2. WHY
A stack solves problems where the **most recent action must be handled first**.  
Without stacks, managing **nested operations**, **reversals**, or **backtracking** becomes complex and repetitive.

---

## 3. WHERE
Stacks fit inside **core system logic**, such as:
- Function execution (call stack)
- Expression evaluation
- Request handling

They are heavily used in:
- Compilers
- Operating systems
- Runtime memory management

---

## 4. HOW
- Elements are added using the **push** operation onto the top of the stack.
- Elements are removed using the **pop** operation, also from the top.
- Access is restricted so **only the top element is visible** at any time.

---

## 5. WHEN
Use a stack when:
- Order reversal is required
- Undo/redo operations are needed
- Nested processing is involved

❌ Do **not** use a stack when:
- Frequent random access is required
- Searching elements is a priority

---

## 6. EXAMPLE
In a **text editor**, the **undo** feature uses a stack to store previous actions.  
Each new action is **pushed**, and undo **pops** the most recent one.

---

## 7. PROS & CONS

### ✅ Pros
- Simple to implement
- Fast operations (O(1))
- Efficient for managing recent data

### ❌ Cons
- Limited access (top only)
- Can cause **overflow** if size is not managed properly

---

## 8. COMMON MISTAKES
- Accessing elements other than the top (violates stack rules)
- Ignoring **overflow** and **underflow** conditions during implementation

<br>
<br>
<br>

# 📦 Stack Data Structure

A **stack** is a linear data structure that follows **LIFO — Last In, First Out**.  
Think of a stack of plates 🍽️: you add on top, you remove from the top.

---

## 🔑 Core Operations

All operations happen at **one end → TOP**

| Operation        | Meaning                          |
|------------------|----------------------------------|
| `push(x)`        | Insert element at the top        |
| `pop()`          | Remove top element               |
| `peek()` / `top()` | View top element               |
| `isEmpty()`      | Check if stack is empty          |
| `isFull()`       | (Array stack) check overflow     |

---

## ⏱️ Time Complexity

- **Push:** O(1)  
- **Pop:** O(1)  
- **Peek:** O(1)  

✅ Fast because **no shifting** is needed.

---

## 🧠 Where Stacks Are Used

- Function calls & recursion (**call stack**)
- Undo / Redo operations
- Expression evaluation (infix → postfix)
- Backtracking (DFS, maze solving)
- Parenthesis checking `({[]})`

---

## 🧩 Stack Implementation (Python)

```python
stack = []

stack.append(10)   # push
stack.append(20)

print(stack.pop()) # pop → 20
print(stack[-1])   # peek → 10
```

---

## ⚠️ Common Stack Problems (Interview Gold 🥇)

- Valid Parentheses
- Reverse a string
- Next Greater Element
- Stack using array / linked list
- Min Stack (get minimum in O(1))

---

## 💡 One-line Summary

**Stack = LIFO + operations at one end + O(1) efficiency**