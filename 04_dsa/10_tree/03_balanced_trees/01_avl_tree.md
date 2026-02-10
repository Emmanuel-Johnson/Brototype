# 🌲 AVL Tree

An **AVL Tree** is a **self-balancing Binary Search Tree (BST)**.  
It automatically keeps itself balanced after every **insert** or **delete**, so operations stay fast.

---

## 🔑 Core Idea (One Line)

For every node, the **height difference** between its left and right subtree is **at most 1**.

This height difference is called the **Balance Factor**.

---

## ⚖️ Balance Factor

```
Balance Factor = height(left subtree) − height(right subtree)
```

### Allowed Values

- `-1` ✅  
- `0` ✅  
- `+1` ✅  

If it becomes `-2` or `+2` → tree is **unbalanced** ❌ → must be fixed using **rotations**.

---

## 🔁 Rotations (How AVL Fixes Itself)

There are **4 imbalance cases**:

1️⃣ **LL (Left-Left)** → Right Rotation  
2️⃣ **RR (Right-Right)** → Left Rotation  
3️⃣ **LR (Left-Right)** → Left Rotation + Right Rotation  
4️⃣ **RL (Right-Left)** → Right Rotation + Left Rotation  

👉 You don’t need to memorize code immediately — just understand **why rotations happen**.

---

## ⏱️ Time Complexity

| Operation | Time |
|---------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

**Why?** 👉 Because the tree height is always **minimized**.

---

## 👍 Advantages

- Always balanced  
- Very fast lookups  
- Predictable performance  

---

## 👎 Disadvantages

- Extra work (rotations required)  
- More complex than a normal BST  

---

## 🤔 AVL vs Normal BST

| Feature | BST | AVL |
|------|-----|-----|
| Balanced? | ❌ Maybe | ✅ Always |
| Height | Can be O(n) | O(log n) |
| Speed | Can degrade | Consistent |

---

## 🧠 One-Line Summary

```
AVL Tree = BST + automatic balancing (using rotations)
```