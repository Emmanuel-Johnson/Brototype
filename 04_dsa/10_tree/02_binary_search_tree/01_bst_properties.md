# 🌳 Binary Search Tree (BST) — Properties

A **Binary Search Tree (BST)** is a special kind of binary tree with **ordering rules** that make searching fast.

---

## ✅ 1. At Most Two Children

Each node has:
- Left child  
- Right child  

👉 No node can have more than **two children**.

---

## ✅ 2. Left Subtree Rule

For any node:

- All values in the **left subtree** are **less than** the node’s value.

**Example:**  
If node = `50`  
Left subtree values can be: `10, 20, 40` (all `< 50`)

---

## ✅ 3. Right Subtree Rule

For any node:

- All values in the **right subtree** are **greater than** the node’s value.

**Example:**  
If node = `50`  
Right subtree values can be: `60, 70, 90` (all `> 50`)

---

## ✅ 4. Recursive Property (Important 🔥)

- The **left subtree** must also be a BST  
- The **right subtree** must also be a BST  

👉 The BST rules apply **at every node**, not just the root.

---

## ✅ 5. No Duplicates (Usually)

Most BST definitions say:
- Duplicate values are **not allowed**

⚠️ Some implementations allow duplicates but always place them **consistently on one side**.

---

## ✅ 6. Inorder Traversal Gives Sorted Order 🔥

If you traverse a BST using **Inorder traversal**:

```
Left → Root → Right
```

You get elements in **ascending sorted order**.

**Example:**
```
Inorder traversal → 10 20 30 40 50 60 70
```

✨ This is a **key advantage** of BST.

---

## ✅ 7. Time Complexity Depends on Height

### Balanced BST
- Search / Insert / Delete → **O(log n)**

### Skewed BST (looks like a linked list 😬)
- Search / Insert / Delete → **O(n)**

👉 That’s why **balanced trees** (AVL Tree, Red-Black Tree) exist.

---

## 🧠 One-Line Summary

**BST = Binary Tree + Ordering Rule**  

```
left < root < right
```