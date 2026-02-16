# 🟢 Adjacency List

An **Adjacency List** represents a graph by storing:

👉 For each vertex → a list of its neighbors.

Instead of an `n × n` matrix,
we store only existing edges.

------------------------------------------------------------------------

## 📌 Example Graph

Vertices: A, B, C, D

Edges: - A --- B
- A --- C
- B --- D

------------------------------------------------------------------------

## 📋 Adjacency List Representation

A → B, C
B → A, D
C → A
D → B

We only store actual connections, not empty spaces like a matrix.

------------------------------------------------------------------------

## 🧠 Python Representation

``` python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

Clean and efficient.

------------------------------------------------------------------------

## ⚡ Space & Time Complexity

Let:

-   V = number of vertices
-   E = number of edges

Then:

-   **Space** → O(V + E)
-   **Edge check** → O(degree of vertex)

Adjacency List is best for **sparse graphs**.

------------------------------------------------------------------------

## 🆚 Matrix vs List

  Feature              Adjacency Matrix   Adjacency List
  -------------------- ------------------ ----------------
  Space                O(n²)              O(V + E)
  Best For             Dense Graph        Sparse Graph
  Used in Real Apps?   Rare               Very Common

------------------------------------------------------------------------

## 🧠 Directed Graph Version

For directed graph:

If:

A → B

Representation:

A → B
B → (nothing)

We only store **outgoing edges**.