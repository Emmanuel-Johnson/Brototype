# Heap

## ✅ Definition (1 line)

A heap is a complete binary tree that satisfies the heap property (in a
max-heap, parent ≥ children; in a min-heap, parent ≤ children).

------------------------------------------------------------------------

## 🚀 3--5 Applications of Heap

-   Priority Queue implementation
-   Heap Sort algorithm
-   Finding kth largest/smallest element
-   Dijkstra's shortest path algorithm
-   Task scheduling systems

------------------------------------------------------------------------

## 🔎 Brief Explanation (1--2 Applications)

### 🏆 Priority Queue

Heaps are mainly used to implement priority queues.

Instead of removing the first inserted element, we remove the highest
(or lowest) priority element.

Example:

-   Emergency room patients (critical cases first)
-   CPU process scheduling

### 🛣 Dijkstra's Algorithm

Heaps are used to efficiently pick the minimum distance node in shortest
path problems.

Using a heap makes the time complexity O((V + E) log V) instead of
slower approaches.