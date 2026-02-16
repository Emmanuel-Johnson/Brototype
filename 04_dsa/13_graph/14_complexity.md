# Graph Complexity Notes

When someone says **"complexity of graph"**, they usually mean:

-   Time complexity of graph operations
-   Time complexity of graph traversals (BFS / DFS)
-   Space complexity of graph representation

------------------------------------------------------------------------

# 1️⃣ Graph Representation Complexity

## 🟢 Adjacency List

Example:

``` python
{
  A: [B, C],
  B: [A, D],
  C: [A],
  D: [B]
}
```

### Space Complexity:

O(V + E)

Where: - V = number of vertices
- E = number of edges

Why? - We store V keys - Total neighbors stored = E (or 2E in undirected
graph)

------------------------------------------------------------------------

## 🔵 Adjacency Matrix

Matrix of size V × V

### Space Complexity:

O(V²)

Even if there are few edges, we still allocate full matrix.

------------------------------------------------------------------------

# 2️⃣ BFS & DFS --- Complexity Comparison

## Using Adjacency List

| Algorithm | Time Complexity | Space Complexity |
|-----------|------------------|------------------|
| BFS       | O(V + E)        | O(V)             |
| DFS       | O(V + E)        | O(V)             |

Why? - Visit each vertex once → O(V) - Explore each edge once → O(E) -
Extra space (visited + queue/stack) → O(V)

------------------------------------------------------------------------

## Using Adjacency Matrix

| Algorithm | Time Complexity | Space Complexity |
|-----------|------------------|------------------|
| BFS       | O(V²)           | O(V²)            |
| DFS       | O(V²)           | O(V²)            |

Why? - For each vertex, scan entire row → O(V) - For V vertices →
O(V²) - Matrix storage itself → O(V²)

------------------------------------------------------------------------

# 3️⃣ Basic Graph Operations

## Adjacency List

| Operation     | Time Complexity        |
|--------------|------------------------|
| Add Vertex   | O(1)                   |
| Add Edge     | O(1)                   |
| Remove Edge  | O(E) (worst case)      |
| Remove Vertex| O(V + E)               |

------------------------------------------------------------------------

## Adjacency Matrix

| Operation      | Time Complexity |
|---------------|-----------------|
| Add Vertex    | O(V²)           |
| Add Edge      | O(1)            |
| Remove Edge   | O(1)            |
| Remove Vertex | O(V²)           |

------------------------------------------------------------------------

# Important Insight

-   Sparse graph (E ≈ V) → behaves like O(V)
-   Dense graph (E ≈ V²) → behaves like O(V²)

------------------------------------------------------------------------

# Interview Quick Answer

Time complexity of BFS/DFS:

O(V + E)

Because we visit each vertex once and each edge once.