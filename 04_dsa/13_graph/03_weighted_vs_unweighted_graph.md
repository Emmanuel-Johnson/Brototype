# ⚖️ Weighted vs Unweighted Graph

------------------------------------------------------------------------

# 🎯 1️⃣ Unweighted Graph

## ✅ Definition

Edges have no cost/value.

If:

    A — B

It just means connection exists.
Nothing more.

------------------------------------------------------------------------

## 🧠 What does this imply?

Every edge is treated as having equal cost (usually 1).

So:

**Shortest path = Minimum number of edges**

------------------------------------------------------------------------

## 💻 Example (Adjacency List)

``` python
graph = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["A"]
}
```

------------------------------------------------------------------------

## 🔥 Used In

-   Social networks
-   Number of islands
-   Connected components
-   BFS shortest path (very common interview question)

------------------------------------------------------------------------

## 🚀 Algorithm Used

👉 **BFS finds shortest path**
Time Complexity: **O(V + E)**

------------------------------------------------------------------------

# 💰 2️⃣ Weighted Graph

## ✅ Definition

Edges have weight (cost, distance, time, etc.)

Example:

    A —5— B

That `5` might mean:

-   Distance (5 km)
-   Time (5 minutes)
-   Cost ($5)

------------------------------------------------------------------------

## 🧠 What changes here?

Now:

**Shortest path ≠ Minimum edges**
**Shortest path = Minimum total weight**

Big difference.

------------------------------------------------------------------------

## 💻 Example (Adjacency List)

``` python
graph = {
    "A": [("B", 5), ("C", 2)],
    "B": [("A", 5)],
    "C": [("A", 2)]
}
```

------------------------------------------------------------------------

## 🔥 Used In

-   Google Maps
-   Flight ticket pricing
-   Network routing
-   Delivery optimization

------------------------------------------------------------------------

## 🚀 Algorithms Used

  Case                       Algorithm
  -------------------------- ----------------
  No negative weights        Dijkstra
  Negative weights allowed   Bellman-Ford
  All pairs shortest path    Floyd-Warshall

------------------------------------------------------------------------

# ⚡ Core Difference (Interview Gold)

| Feature               | Unweighted        | Weighted               |
|-----------------------|-------------------|------------------------|
| Edge has cost?        | ❌ No              | ✅ Yes                 |
| All edges equal?      | ✅ Yes             | ❌ No                  |
| Shortest path means   | Fewest edges      | Minimum total weight   |
| Main algorithm        | BFS               | Dijkstra               |

------------------------------------------------------------------------

# 🧠 Interview Trap

If interviewer says:

> "Find shortest path"

You MUST ask:
👉 **Is the graph weighted or unweighted?**

Because:

-   Unweighted → **BFS**
-   Weighted → **Dijkstra**

That's a maturity signal in interviews 💯