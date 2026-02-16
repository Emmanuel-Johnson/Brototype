# 🟢 Basic Graph Terminology

---

## 1️⃣ Vertex (Node)

A **vertex** is a point in a graph.

👉 Represents a person, city, computer, etc.

📌 Example:  
In a friend network, each person is a vertex.

---

## 2️⃣ Edge

An **edge** connects two vertices.

👉 Represents a relationship or connection.

- In **undirected graph** → connection both ways  
- In **directed graph** → one-way connection  

---

## 3️⃣ Degree (Undirected Graph)

**Degree of a vertex** =  
👉 Number of edges connected to it.

If a node connects to 3 nodes → Degree = 3

---

## 4️⃣ In-degree & Out-degree (Directed Graph)

In directed graphs:

- **In-degree** → Number of incoming edges  
- **Out-degree** → Number of outgoing edges  

### Example:

A → B → C

For vertex **B**:

- In-degree = 1  
- Out-degree = 1  

---

## 5️⃣ Path

A **path** is a sequence of vertices connected by edges.

Example:

A → B → C → D  

That is a **path of length 3**.

---

## 6️⃣ Cycle

A **cycle** is a path that:

👉 Starts and ends at the same vertex.

Example:

A → B → C → A  

That’s a cycle.

---

## 7️⃣ Connected Graph

A graph is **connected** if:

👉 You can reach every vertex from any other vertex.

If some nodes are isolated → it is a **disconnected graph**.

---

## 8️⃣ Connected Components

In a disconnected graph:

Each separate group is called a **connected component**.

Think of:
Separate islands 🌴

---

## 9️⃣ Weighted vs Unweighted Graph

- **Weighted graph** → Edges have cost (distance, time, money)
- **Unweighted graph** → No cost

Used in **shortest path problems**.

---

## 🔟 Complete Graph

Every vertex connects to every other vertex.

Super dense graph.

---

## 1️⃣1️⃣ Bipartite Graph

- Vertices can be divided into two sets  
- Edges only between sets  
- No odd cycles allowed  

---

## 1️⃣2️⃣ Tree

A **tree** is:

👉 Connected  
👉 Acyclic  
👉 Undirected  

Number of edges = n − 1

---

# 🎯 Core Idea to Remember

Graph =  
**Vertices + Edges + Relationship**

Everything else is just variations of this.
