# 🔴⚫ Red-Black Tree

A **Red-Black Tree** is a **self-balancing Binary Search Tree (BST)** that stays *approximately balanced* using **node colors** and a few strict rules.

Think of it as:

> **“Less strict than AVL, but faster to update.”**

---

## 🎨 Coloring Rules (The Heart ❤️)

1️⃣ Every node is either **Red** or **Black**  
2️⃣ The **root is always Black**  
3️⃣ **Red nodes cannot have Red children** (no double red ❌)  
4️⃣ Every path from a node to its **NULL leaves** has the same number of **Black nodes**  
5️⃣ All **NULL (NIL) leaves** are **Black**  

👉 These rules keep the tree balanced enough.

---

## ⚖️ How Balancing Works

Instead of aggressively rotating like AVL trees, Red-Black Trees use:

- **Recoloring** 🎨  
- **Fewer rotations** 🔁  

**Result 👉** Faster **insert** and **delete** operations compared to AVL trees.

---

## ⏱️ Time Complexity

| Operation | Time |
|---------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

📏 Height is guaranteed to be:

```
≤ 2 × log₂(n)
```

---

## 🔴⚫ Red-Black Tree vs AVL Tree

| Feature | AVL Tree | Red-Black Tree |
|------|---------|---------------|
| Balance | Very strict | Less strict |
| Height | Smaller | Slightly taller |
| Search | Faster | Slightly slower |
| Insert/Delete | Slower | Faster |
| Rotations | More | Fewer |

👉 **AVL** → Read-heavy systems  
👉 **Red-Black** → Write-heavy systems  

---

## 🧠 Where Red-Black Trees Are Used

- C++ `map` / `set`  
- Java `TreeMap` / `TreeSet`  
- Linux kernel schedulers  
- Database indexing (internal structures)  

✨ You use them **without even realizing it** 😄

---

## 🧠 One-Line Summary

```
Red-Black Tree = BST + colors + relaxed balancing
```