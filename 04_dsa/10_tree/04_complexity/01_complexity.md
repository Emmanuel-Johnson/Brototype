# 🌳 Binary Search Tree (BST) -- Time & Space Complexity

Let `n` be the number of nodes.

------------------------------------------------------------------------

## 1️⃣ Search

### 🔎 Steps:

-   Compare value with root
-   Go left or right
-   Repeat until found / null

### ⏱ Time Complexity

  Case         Time
  ------------ ----------
  ✅ Best      O(1)
  📈 Average   O(log n)
  🔥 Worst     O(n)

### 💡 Why?

-   In a **balanced BST** → height = `log n`
-   In a **skewed BST** (like sorted insertion) → height = `n`

Worst case looks like this:

    1
     \
      2
       \
        3
         \
          4

That's basically a linked list 😭 → **O(n)**

------------------------------------------------------------------------

## 2️⃣ Insert

Same logic as search (we first search for the correct position).

  Case         Time
  ------------ ----------
  ✅ Best      O(1)
  📈 Average   O(log n)
  🔥 Worst     O(n)

------------------------------------------------------------------------

## 3️⃣ Delete

Delete has 3 cases:

1.  Leaf node
2.  One child
3.  Two children (find inorder successor)

  Case         Time
  ------------ ----------
  ✅ Best      O(1)
  📈 Average   O(log n)
  🔥 Worst     O(n)

Because we still traverse the height of the tree.

------------------------------------------------------------------------

## 4️⃣ Traversals (Inorder, Preorder, Postorder)

We visit every node once.

  Metric     Complexity
  ---------- ----------------------
  ⏱ Time     O(n)
  📦 Space   O(h) recursion stack

Where: - `h = height` - Balanced → `O(log n)` - Worst → `O(n)`

------------------------------------------------------------------------

# 📦 Space Complexity

  Operation                  Space
  -------------------------- -------
  Search / Insert / Delete   O(h)
  Traversal                  O(h)
  Total Tree Storage         O(n)

------------------------------------------------------------------------

# 🔥 Final Summary (Interview Gold)

## ✅ Balanced BST:

    Search  → O(log n)
    Insert  → O(log n)
    Delete  → O(log n)

## 🔥 Skewed BST:

    Search  → O(n)
    Insert  → O(n)
    Delete  → O(n)

------------------------------------------------------------------------

# ⚡ Interview Tip

If interviewer asks:

> "How do you avoid O(n) worst case?"

Answer: 👉 Use **Self-balancing BST** like: - AVL Tree
- Red-Black Tree

Those guarantee **O(log n)** always.