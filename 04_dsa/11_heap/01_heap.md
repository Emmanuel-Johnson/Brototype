# 🌳 What is a Heap?

A **Heap** is a special type of **Binary Tree** that follows specific
rules.

It's mainly used to: - Implement **Priority Queues** - Quickly get the
**min or max element** - Solve problems like **Top K elements, Dijkstra,
etc.**

------------------------------------------------------------------------

# 🧠 Two Types of Heaps

## 1️⃣ Min Heap

**Rule:**\
👉 Parent node is smaller than its children.

### Example:

            5
          /   \
         10    15
        /  \
       20  30

Here: - 5 \< 10 and 15\
- 10 \< 20 and 30

✅ So this is a **Min Heap**.

📌 Smallest element is always at the root.

------------------------------------------------------------------------

## 2️⃣ Max Heap

**Rule:**\
👉 Parent node is greater than its children.

### Example:

            50
          /    \
         30     40
        /  \
       10   20

Here: - 50 \> 30 and 40
- 30 \> 10 and 20

✅ So this is a **Max Heap**.

📌 Largest element is always at the root.

------------------------------------------------------------------------

# 🧱 Important Heap Properties

## 1️⃣ Complete Binary Tree

Heap must be a **complete binary tree**: - Filled from left to right
- No gaps

## 2️⃣ Heap Order Property

-   **Min Heap** → Parent is smaller
-   **Max Heap** → Parent is larger

------------------------------------------------------------------------

# ⚡ Time Complexity

  Operation        Time
  ---------------- ----------
  Insert           O(log n)
  Delete (root)    O(log n)
  Peek (min/max)   O(1)

💡 Why O(log n)?\
Because heap height = **log n**.

------------------------------------------------------------------------

# 💡 How Heap is Stored

Heaps are usually stored in an **array**, not like a linked tree.

If index = `i`:

-   Left child = `2*i + 1`
-   Right child = `2*i + 2`
-   Parent = `(i - 1) // 2`

This makes it very efficient 🚀

------------------------------------------------------------------------

# 🧑‍💻 Python Example (Min Heap)

``` python
import heapq

heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)

print(heap)               # [5, 10, 20]
print(heapq.heappop(heap))  # 5
```

📌 Python default heap = **Min Heap**.

------------------------------------------------------------------------

# 🔥 When Should You Use Heap?

-   Finding **k largest/smallest**
-   **Priority Queue** problems
-   **Scheduling**
-   **Dijkstra's algorithm**
-   **Median in data stream**