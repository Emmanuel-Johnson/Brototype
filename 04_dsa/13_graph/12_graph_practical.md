# Graph Implementation in Python

## Overview

This implementation includes:

-   Add Vertex
-   Add Edge (Undirected)
-   Remove Edge
-   Remove Vertex
-   Display Graph
-   BFS (Breadth First Search)
-   DFS (Depth First Search)
-   Cycle Detection (Undirected Graph)

------------------------------------------------------------------------

## Code

``` python
from collections import deque

class Graph:
    def __init__(self):
        # adjacency list: { vertex: [neighbors] }
        self.adj = {}

    # -------------------------
    # Add Vertex
    # -------------------------
    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []
        else:
            print("Vertex already exists")

    # -------------------------
    # Add Edge (Undirected)
    # -------------------------
    def add_edge(self, v1, v2):
        if v1 not in self.adj:
            self.add_vertex(v1)
        if v2 not in self.adj:
            self.add_vertex(v2)

        # Undirected → add both sides
        if v2 not in self.adj[v1]:
            self.adj[v1].append(v2)
        if v1 not in self.adj[v2]:
            self.adj[v2].append(v1)

    # -------------------------
    # Remove Edge
    # -------------------------
    def remove_edge(self, v1, v2):
        if v1 in self.adj and v2 in self.adj[v1]:
            self.adj[v1].remove(v2)

        if v2 in self.adj and v1 in self.adj[v2]:
            self.adj[v2].remove(v1)

    # -------------------------
    # Remove Vertex
    # -------------------------
    def remove_vertex(self, vertex):
        if vertex in self.adj:
            # remove edges connected to this vertex
            for neighbor in self.adj[vertex]:
                self.adj[neighbor].remove(vertex)

            del self.adj[vertex]
        else:
            print("Vertex not found")

    # -------------------------
    # Display Graph
    # -------------------------
    def display(self):
        for vertex in self.adj:
            print(f"{vertex} -> {self.adj[vertex]}")

    # -------------------------
    # BFS (Breadth First Search)
    # -------------------------
    def bfs(self, start):
        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # -------------------------
    # DFS (Depth First Search)
    # -------------------------
    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
    
    # -------------------------
    # Cycle Detection
    # -------------------------
    def has_cycle(self):
        visited = set()

        for vertex in self.adj:
            if vertex not in visited:
                if self._dfs_cycle(vertex, visited, parent=None):
                    return True
        return False

    def _dfs_cycle(self, current, visited, parent):
        visited.add(current)

        for neighbor in self.adj[current]:
            if neighbor not in visited:
                if self._dfs_cycle(neighbor, visited, current):
                    return True
            elif neighbor != parent:
                return True

        return False
```