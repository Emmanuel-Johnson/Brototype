# 🔁 Cyclic Graph vs Acyclic Graph

------------------------------------------------------------------------

# 🔄 1️⃣ Cyclic Graph

## ✅ Definition

A graph is **cyclic** if there exists a path that starts and ends at the
same node.

Example:

    A → B → C → A

You can start at A and come back to A again.
That's a cycle.

------------------------------------------------------------------------

## 🧠 In Simple Words

If you can walk and eventually return to where you started → **cycle
exists**.

------------------------------------------------------------------------

## 🔥 Where Cycles Appear?

-   Social networks
-   Road networks
-   Mutual dependencies
-   Undirected graphs commonly contain cycles

------------------------------------------------------------------------

## ⚠️ Why Cycles Matter?

-   In **task scheduling**, cycles are bad
-   In **dependency graphs**, cycle = impossible execution
-   In **DFS**, cycles can cause infinite recursion if no `visited` set

------------------------------------------------------------------------

# 🚫 2️⃣ Acyclic Graph

## ✅ Definition

A graph with **no cycles**.

You can never return to the starting node.

------------------------------------------------------------------------

## 🧠 Special Case

If a directed graph has no cycle →
it is called a:

👉 **Directed Acyclic Graph (DAG)**

Very important term for interviews.

------------------------------------------------------------------------

## 🔥 Real-Life Uses of DAG

-   Course prerequisites
-   Build systems (npm, pip dependencies)
-   Task scheduling
-   Topological sort

------------------------------------------------------------------------

# ⚡ Directed vs Undirected Cycles (Important Difference)

## 🔹 In Undirected Graph

Cycle exists if:

-   You reach a visited node
-   AND it's not your parent

(Interview classic logic)

------------------------------------------------------------------------

## 🔹 In Directed Graph

Cycle exists if:

-   During DFS, you revisit a node in the recursion stack

This is more tricky.

------------------------------------------------------------------------

# 📊 Quick Comparison

| Feature                  | Cyclic Graph | Acyclic Graph |
|--------------------------|--------------|---------------|
| Cycle present?           | ✅ Yes       | ❌ No         |
| Can return to start?     | Yes          | No            |
| Used in scheduling?      | ❌ No        | ✅ Yes        |
| Special name (directed)  | ---          | DAG           |

------------------------------------------------------------------------

# 🧠 Interview Reality

Most common graph interview problem types:

-   Detect cycle in undirected graph
-   Detect cycle in directed graph
-   Check if graph is DAG
-   Topological sort (works only if DAG)

If graph has a cycle →
❌ **Topological sort is impossible.**