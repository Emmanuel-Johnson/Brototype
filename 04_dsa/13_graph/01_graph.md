# 🌐 Graph Data Structure

## 📌 What is a Graph?

A **Graph** is a data structure used to represent relationships between
objects.

It consists of:

-   **Vertices (Nodes)** → Data points
-   **Edges** → Connections between nodes

### 👉 Think of:

-   Cities connected by roads
-   People connected by friendships
-   Web pages connected by links

All of these are **graphs**.

------------------------------------------------------------------------

## 🧠 Basic Structure

        A —— B
        |     |
        C —— D

Here:

-   `A, B, C, D` → **Vertices**
-   Lines → **Edges**

------------------------------------------------------------------------

# 📚 Types of Graphs

## 1️⃣ Directed Graph (Digraph)

Edges have direction.

Example:

    A → B  
    B → C

You can only travel in the arrow direction.

### ✅ Used in:

-   Twitter follow system
-   Course prerequisites
-   Task scheduling

------------------------------------------------------------------------

## 2️⃣ Undirected Graph

Edges have no direction.

    A — B

Means: - A can go to B
- B can go to A

### ✅ Used in:

-   Facebook friendships
-   Road maps

------------------------------------------------------------------------

## 3️⃣ Weighted Graph

Edges have cost/weight.

    A —5— B

The `5` might mean: - Distance
- Time
- Cost

### ✅ Used in:

-   Google Maps shortest path
-   Network routing

------------------------------------------------------------------------

# 🏗 Graph Representation in Code

There are **2 main ways** to represent a graph:

------------------------------------------------------------------------

## 1️⃣ Adjacency Matrix

        A B C
    A [ 0 1 1 ]
    B [ 1 0 0 ]
    C [ 1 0 0 ]

### ✔ Advantages

-   Easy to check connection

### ❌ Disadvantages

-   Wastes space if graph is sparse

**Space Complexity → O(V²)**

------------------------------------------------------------------------

## 2️⃣ Adjacency List (Most Used)

``` python
graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"]
}
```

### ✔ Advantages

-   Saves space
-   Used in interviews
-   Used in real systems

**Space Complexity → O(V + E)**

💡 In real-world systems and coding interviews → **Adjacency List is
standard**

------------------------------------------------------------------------

# 🔁 Important Graph Traversals

## 1️⃣ BFS (Breadth First Search)

-   Uses **Queue**
-   Level order traversal
-   Finds shortest path in unweighted graph

**Time Complexity → O(V + E)**

------------------------------------------------------------------------

## 2️⃣ DFS (Depth First Search)

-   Uses **Recursion / Stack**
-   Goes deep first

**Time Complexity → O(V + E)**

------------------------------------------------------------------------

# 🧮 Important Graph Problems for Interviews

You WILL see these:

-   BFS / DFS traversal
-   Detect cycle (directed & undirected)
-   Topological sort
-   Shortest path
-   Number of islands
-   Connected components
-   Bipartite graph

------------------------------------------------------------------------

# 🌍 Real World Usage

Graphs are everywhere:

-   Social networks
-   GPS navigation
-   Internet routing
-   Dependency resolution (npm, pip)
-   Recommendation systems

------------------------------------------------------------------------

# 🎯 Interview Reality Check

For most coding interviews, you must know:

-   Graph representation
-   BFS
-   DFS
-   Cycle detection
-   Topological sort

If you master these → Graph becomes easy territory 💪