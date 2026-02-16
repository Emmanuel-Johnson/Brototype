# 🟢 Adjacency Matrix

An **Adjacency Matrix** is a way to represent a graph using a **2D array
(matrix)**.

If a graph has `n` vertices,
👉 we create an `n × n` matrix.

------------------------------------------------------------------------

## 📌 Basic Idea

If there is an edge between vertex `i` and vertex `j`:

-   Put `1` → if edge exists
-   Put `0` → if no edge

------------------------------------------------------------------------

## 🧠 Example Graph

Vertices: A, B, C, D

Edges: - A --- B
- A --- C
- B --- D

------------------------------------------------------------------------

## 📊 Adjacency Matrix Representation

        A  B  C  D
    A   0  1  1  0
    B   1  0  0  1
    C   1  0  0  0
    D   0  1  0  0

------------------------------------------------------------------------

## 🔎 Important Observations

### 1️⃣ Undirected Graph

Matrix is **symmetric**.

If A--B exists:

    matrix[A][B] = matrix[B][A]

------------------------------------------------------------------------

### 2️⃣ Directed Graph

Matrix is **not symmetric**.

If:

A → B

    matrix[A][B] = 1
    matrix[B][A] = 0

------------------------------------------------------------------------

### 3️⃣ Weighted Graph

Instead of `1`, store the **weight**.

Example:

If edge A → B has weight 5:

    matrix[A][B] = 5

If no edge exists, sometimes store: - `0` - or `∞` (for shortest path
problems)

------------------------------------------------------------------------

## ⚡ Time & Space Complexity

If graph has `n` vertices:

-   **Space** → O(n²)
-   **Edge check** → O(1)

Edge check is fast because we directly access:

    matrix[i][j]

------------------------------------------------------------------------

## ❗ Drawback

If graph is **sparse** (few edges),

Adjacency Matrix wastes space
because we still allocate `n²` cells.

------------------------------------------------------------------------

## 🆚 Matrix vs List

  Feature      Adjacency Matrix   Adjacency List
  ------------ ------------------ ----------------
  Space        O(n²)              O(V + E)
  Edge Check   O(1)               O(degree)
  Best For     Dense Graph        Sparse Graph

------------------------------------------------------------------------

## 🎯 When to Use

Use Adjacency Matrix when:

-   Graph is dense
-   Fast edge lookup is required
-   Number of vertices is small
-   Using algorithms like Floyd--Warshall

------------------------------------------------------------------------

## 🧠 Interview One-Liner

Adjacency Matrix is best for dense graphs when O(1) edge lookup is
required, but it costs O(n²) space.