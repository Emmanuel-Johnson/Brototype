# 🔀 Directed vs Undirected Graph

------------------------------------------------------------------------

# ➡️ Directed Graph (Digraph)

## ✅ Definition

Edges have direction.

If there is an edge:

    A → B

It means:

-   You can go from A to B
-   You CANNOT automatically go from B to A
-   Direction matters

------------------------------------------------------------------------

## 🧠 Real-Life Examples

-   **Instagram follow**
    If A follows B → doesn't mean B follows A

-   **Course prerequisites**
    Data Structures → Algorithms
    (You can't reverse it)

-   **Task scheduling**
    One task must finish before another

------------------------------------------------------------------------

## 💻 Representation (Adjacency List)

``` python
graph = {
    "A": ["B"],   # A points to B
    "B": [],
}
```

Here, **B does NOT point back to A.**

------------------------------------------------------------------------

## 🔍 Important Properties

-   **In-degree** → Number of incoming edges
-   **Out-degree** → Number of outgoing edges

### Commonly Used In:

-   Topological Sort
-   Dependency graphs
-   DAG problems

------------------------------------------------------------------------

# ↔️ Undirected Graph

## ✅ Definition

Edges have no direction.

If:

    A — B

It means:

-   A can go to B
-   B can go to A
-   Connection is mutual

------------------------------------------------------------------------

## 🧠 Real-Life Examples

-   Facebook friendship
-   Road between two cities
-   Two people connected in network

------------------------------------------------------------------------

## 💻 Representation (Adjacency List)

``` python
graph = {
    "A": ["B"],
    "B": ["A"],
}
```

Notice:
We add both sides manually.

------------------------------------------------------------------------

# ⚡ Quick Comparison

| Feature                   | Directed                      | Undirected        |
|---------------------------|--------------------------------|-------------------|
| Edge Direction            | Yes                            | No                |
| Reverse travel automatic? | ❌ No                          | ✅ Yes            |
| Degree type               | In-degree & Out-degree         | Only Degree       |
| Cycle detection logic     | Different                      | Different         |
| Used for                  | Dependencies                   | Relationships     |

------------------------------------------------------------------------

# 🧠 Interview Trick

Many students forget this:

-   In **undirected graph**, when using BFS/DFS:
    If you don't use `visited`, you'll loop infinitely
    because edges go both ways.

-   In **directed graph**:
    Loops happen only if there's a cycle.

------------------------------------------------------------------------

# 🎯 When To Use What?

## Use Directed Graph when:

-   Order matters
-   Flow matters
-   Dependencies exist

## Use Undirected Graph when:

-   Relationship is mutual
-   Two-way movement exists