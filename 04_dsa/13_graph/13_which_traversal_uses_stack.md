# Graph Traversal: DFS vs BFS

👉 **DFS (Depth First Search)** uses a **Stack**
👉 **BFS (Breadth First Search)** uses a **Queue**

------------------------------------------------------------------------

## 🔹 DFS → Stack

DFS goes deep first --- like:

> "Let me finish this entire path before checking others."

That behavior naturally fits a **Stack**
**LIFO -- Last In First Out**

There are two ways DFS uses a stack:

### 1️⃣ Explicit Stack (Iterative DFS)

You manually use a stack data structure.

``` python
stack = [start]

while stack:
    node = stack.pop()   # LIFO
```

`.pop()` removes from the end → **Stack behavior**

------------------------------------------------------------------------

### 2️⃣ Implicit Stack (Recursive DFS)

The **call stack** handles it automatically.

``` python
def dfs(node):
    for neighbor in graph[node]:
        dfs(neighbor)
```

Here, recursion uses the system stack internally.

------------------------------------------------------------------------

## 🔹 BFS → Queue

BFS explores level by level:

> "Let me visit all neighbors first, then go deeper."

That fits a **Queue**
**FIFO -- First In First Out**

``` python
from collections import deque

queue = deque([start])

while queue:
    node = queue.popleft()   # FIFO
```

`.popleft()` → **Queue behavior**

------------------------------------------------------------------------

## 🧠 Easy Memory Trick

-   **DFS → Deep → Stack**
-   **BFS → Breadth → Queue**