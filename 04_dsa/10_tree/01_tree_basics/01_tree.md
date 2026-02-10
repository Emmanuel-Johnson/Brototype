# 🌳 Tree Data Structure

A **Tree** is a **non-linear data structure** that represents data in a **hierarchical** way.

### Think of:
- Folder structure in your computer  
- Organization chart  
- Family tree  

---

## 🔑 Basic Terminology

- **Root** → Top node (starting point)
- **Parent** → Node that has children
- **Child** → Node derived from a parent
- **Leaf** → Node with no children
- **Edge** → Connection between nodes
- **Subtree** → Tree inside a tree
- **Height** → Longest path from root to leaf
- **Depth** → Distance from root to a node

---

## 🧠 Key Properties

- One root
- Each node has **one parent** (except root)
- No cycles
- Connected structure

---

## 🌲 Types of Trees (Important!)

### 1️⃣ General Tree
- Any number of children  
- **Example:** File system

### 2️⃣ Binary Tree
- Maximum **2 children** (left & right)

### 3️⃣ Binary Search Tree (BST)
- `Left < Root < Right`
- Fast searching

### 4️⃣ Full Binary Tree
- Each node has **0 or 2 children**

### 5️⃣ Complete Binary Tree
- Filled **level by level (left to right)**

### 6️⃣ Balanced Tree
- Height is minimized  
- **Examples:** AVL Tree, Red-Black Tree

### 7️⃣ Heap
- Min-Heap / Max-Heap  
- Used in **Priority Queues**

---

## 🔄 Tree Traversals

Ways to visit nodes:

### DFS (Depth First Search)
- **Inorder** → Left, Root, Right
- **Preorder** → Root, Left, Right
- **Postorder** → Left, Right, Root

### BFS (Breadth First Search)
- **Level Order Traversal**

---

## ⏱️ Time Complexity (BST – Average Case)

- **Search:** `O(log n)`
- **Insert:** `O(log n)`
- **Delete:** `O(log n)`

⚠️ **Worst case (skewed tree):** `O(n)`

---

## 🧪 Simple Binary Tree Node (Python)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

## 📌 Where Trees Are Used

- Databases (Indexes)
- File systems
- Compilers (Syntax Trees)
- Searching & sorting
- AI Decision Trees