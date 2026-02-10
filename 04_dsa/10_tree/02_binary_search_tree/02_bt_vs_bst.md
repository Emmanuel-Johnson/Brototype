# 🌳 Binary Tree (BT) vs 🌲 Binary Search Tree (BST)

Let’s keep this **simple, exam‑friendly, and crystal clear** 👇

---

## 🔹 Binary Tree (BT)

A **Binary Tree** is just a tree where:

- Each node has **at most 2 children** (left & right)

👉 That’s it. **No ordering rule.**

---

## 🔹 Binary Search Tree (BST)

A **Binary Search Tree (BST)** is a **special type of Binary Tree** with an order:

- Left subtree → values **less than** node  
- Right subtree → values **greater than** node  

---

## 🔍 Key Differences (Side‑by‑Side)

| Feature | Binary Tree (BT) | Binary Search Tree (BST) |
|------|------------------|--------------------------|
| Structure | Max 2 children | Max 2 children |
| Ordering rule | ❌ No order | ✅ Left < Root < Right |
| Search speed | ❌ Slow | ✅ Fast |
| Inorder traversal | ❌ Not sorted | ✅ Sorted order |
| Use case | Hierarchy, expression trees | Fast search, sorted data |
| Example | Heap, Expression Tree | AVL Tree, Red‑Black Tree |

---

## 🧠 Example to Feel the Difference

### Binary Tree (Valid BT ❌ Not BST)

```
      10
     /  \
   50    5
```

- Valid **Binary Tree** ✅  
- Not a **BST** ❌  
  - 50 > 10 on left  
  - 5 < 10 on right  

---

### Binary Search Tree (BST)

```
      10
     /  \
    5   50
```

- Valid **Binary Tree** ✅  
- Valid **BST** ✅  

---

## 🔥 Important Relationship (Remember This!)

```
Every BST is a Binary Tree
❌ Not every Binary Tree is a BST
```

👉 This line alone can **save marks in exams** 😄

---

## 🧩 When to Use What?

### Use **Binary Tree** when:
- Structure matters more than order
- Expression trees
- Heaps
- Syntax trees

### Use **BST** when:
- You need **fast search**
- You want **sorted data**
- Implementing maps, sets, databases

---

## 🧠 One‑Line Summary

```
BT  = structure only
BST = structure + ordering
```