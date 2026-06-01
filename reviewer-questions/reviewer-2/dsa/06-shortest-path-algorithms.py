from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}
        

    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []
        else:
            print("Vertex is already present in the graph!")
            

    def add_edge(self, v1, v2):
        if v1 not in self.adj or v2 not in self.adj:
            print("Both vertexes must be present!")
            return
        
        if v2 not in self.adj[v1]:
            self.adj[v1].append(v2)
        if v1 not in self.adj[v2]:
            self.adj[v2].append(v1)
            

    def remove_vertex(self, vertex):
        if vertex not in self.adj:
            print("Vertex not present in the graph!")
            return
        
        for neighbor in self.adj[vertex]:
            self.adj[neighbor].remove(vertex)
        del self.adj[vertex]
        

    def remove_edge(self, v1, v2):
        if v1 not in self.adj or v2 not in self.adj:
            print("Both vertexes must be present!")
            return
        
        if v2 in self.adj[v1]:
            self.adj[v1].remove(v2)
        if v1 in self.adj[v2]:
            self.adj[v2].remove(v1)
            

    def bfs(self, start):
        queue = deque([start])
        seen = {start}
        
        while queue:
            v = queue.popleft()
            print(v)
            for neighbor in self.adj[v]:
                if neighbor not in seen:
                    queue.append(neighbor)
                    seen.add(neighbor)
                    

    def shortest_path(self, start, end):
        queue = deque([start])
        visited = {start}
        parent = {start : None}
        
        while queue:
            v = queue.popleft()
            if v == end:
                path = []
                while v is not None:
                    path.append(v)
                    v = parent[v]
                return path[::-1]
            
            for neighbor in self.adj[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    parent[neighbor] = v
                    visited.add(neighbor)
        return "Not Found!"
        
                    
    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)
        
    def _dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex)
        for neighbor in self.adj[vertex]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)
                
                
    def has_cycle(self):
        visited = set()
        for vertex in self.adj:
            if vertex not in visited:
                if self._has_cycle(vertex, visited, None):
                    return True
        return False
        
    def _has_cycle(self, current, visited, parent):
        visited.add(current)
        for neighbor in self.adj[current]:
            if neighbor not in visited:
                if self._has_cycle(neighbor, visited, current):
                    return True
            elif neighbor != parent:
                return True
        return False
        

    def display(self):
        for vertex, neighbor in self.adj.items():
            print(f"{vertex} --> {neighbor}")
            
g = Graph()

g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")
g.add_vertex("F")

g.add_edge("A", "B")
g.add_edge("A", "D")
g.add_edge("B", "C")
g.add_edge("D", "C")
g.add_edge("E", "D")
g.add_edge("E", "F")

g.display()

print()

print(g.shortest_path("A", "F"))
print(g.has_cycle())
