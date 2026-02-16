# 🔗 Connected Graph vs Disconnected Graph

------------------------------------------------------------------------

# 🟢 1️⃣ Connected Graph

## ✅ Definition

A graph is **connected** if:

👉 You can reach every vertex from any other vertex.

In simple words:
There's a path between every pair of nodes.

------------------------------------------------------------------------

## 🧠 Example

If you start BFS or DFS from any node,
you will visit all nodes.

That means → **Graph is connected.**

------------------------------------------------------------------------

## 🔥 Real-Life Example

-   A fully connected friend network
-   A road system where every city is reachable

------------------------------------------------------------------------

## 💡 Important (Undirected Graph)

In an **undirected graph**:

If it has **1 connected component**,
it is called a **connected graph**.

------------------------------------------------------------------------

# 🔴 2️⃣ Disconnected Graph

## ✅ Definition

A graph is **disconnected** if:

👉 At least one vertex cannot be reached from another vertex.

In simple words:
Graph is broken into separate groups.

------------------------------------------------------------------------

## 🧠 Example

If you run BFS from node A
and some nodes are never visited →
Graph is **disconnected**.

------------------------------------------------------------------------

## 🔥 These separate parts are called:

👉 **Connected Components**

Each isolated group = 1 component.

------------------------------------------------------------------------

# 🧠 Directed Graph Version (Important!)

For **directed graphs**, connectivity is more complex.

There are two types:

## 1️⃣ Strongly Connected Graph

Every node can reach every other node (following direction).

## 2️⃣ Weakly Connected Graph

If you ignore directions, it becomes connected.

------------------------------------------------------------------------

# ⚡ Quick Comparison

| Feature                       | Connected | Disconnected |
|--------------------------------|-----------|--------------|
| All nodes reachable?           | ✅ Yes    | ❌ No        |
| BFS from one node visits all?  | Yes       | No           |
| Components count               | 1         | > 1          |
