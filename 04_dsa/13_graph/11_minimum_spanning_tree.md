# 🌳 Minimum Spanning Tree (MST)

## 📌 What is a Spanning Tree?

If you have a **connected, undirected graph**, a spanning tree:

-   👉 Connects all vertices
-   👉 Uses no cycles
-   👉 Uses exactly **V − 1 edges** (where V = number of vertices)

So it's basically the minimum edges needed to connect everything.

------------------------------------------------------------------------

## 📌 What is a Minimum Spanning Tree?

A **Minimum Spanning Tree (MST)** is:

-   👉 A spanning tree
-   👉 With the **minimum possible total edge weight**

So:

-   No cycles ❌
-   All nodes connected ✅
-   Total weight is as small as possible ✅

------------------------------------------------------------------------

## 📊 Example

### Weighted Graph

Vertices: **A, B, C, D**

Edges with weights:

-   A --- B (4)
-   A --- C (3)
-   B --- C (2)
-   B --- D (5)
-   C --- D (7)

### Step 1: Choose smallest edges first

Sorted edges:

1.  B --- C (2)
2.  A --- C (3)
3.  A --- B (4)
4.  B --- D (5)
5.  C --- D (7)

We pick carefully (no cycles allowed):

-   ✅ B --- C (2)
-   ✅ A --- C (3)
-   ❌ A --- B (4) → would create cycle
-   ✅ B --- D (5)

Now all 4 vertices are connected.

### ✅ Total weight = 2 + 3 + 5 = 10

That is the **MST**.

------------------------------------------------------------------------

## 🧠 Important Properties

For a graph with **V vertices**:

-   MST has **V − 1 edges**
-   No cycles
-   Always exists if graph is connected
-   Can have multiple MSTs if weights are equal

------------------------------------------------------------------------

## 🛠 Algorithms to Find MST

### 1️⃣ Kruskal's Algorithm

-   Sort all edges by weight
-   Pick smallest edge
-   Add it if it doesn't form a cycle
-   Repeat

Uses **Union-Find (Disjoint Set)**.

Best when graph has **more edges**.

------------------------------------------------------------------------

### 2️⃣ Prim's Algorithm

-   Start from any node
-   Keep adding smallest edge connecting new vertex
-   Use a **priority queue**

Best when graph is **dense**.

------------------------------------------------------------------------

## 💡 Real-Life Use

-   🛣 Road network design
-   🌐 Internet cable layout
-   ⚡ Electrical wiring
-   🏙 Connecting cities with minimum cost

Basically:
**Connect everything with minimum money.**

------------------------------------------------------------------------

## ⚡ Quick Interview Summary

A **Minimum Spanning Tree** is:

> A subset of edges in a connected, weighted, undirected graph that
> connects all vertices without cycles and with minimum total weight.