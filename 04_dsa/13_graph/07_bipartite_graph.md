# 🟢 Bipartite Graph

A **Bipartite Graph** is a graph where:

👉 The vertices can be divided into **two separate sets**  
👉 Edges connect **only between the two sets**  
👉 No edges exist inside the same set  

Think of it like:  
Two teams. Connections only happen **across teams**, never within the same team.

---

## 📌 Visual Understanding

Let:

- Left side = **Set U**
- Right side = **Set V**

Edges go only:

U → V ✅

Not allowed:

U → U ❌  
V → V ❌  

That’s the rule.

---

## 🧠 Important Property (Interview Favorite)

A graph is **bipartite if and only if**:

👉 It has **NO odd-length cycle**

### Why?

If there is an **odd cycle** (like 3 nodes forming a triangle ❌)
→ It is **NOT bipartite**

Even-length cycles? ✅ Allowed

---

## 📚 Real-Life Examples

- Students ↔ Courses  
- Drivers ↔ Riders (like Uber matching)  
- Jobs ↔ Applicants  
- Buyers ↔ Products  

Basically:  
Two different categories interacting.

---

# ⚡ Special Case: Complete Bipartite Graph

When:

👉 Every node in Set A connects to every node in Set B

It is written as:

K(m, n)

Where:
- m = number of vertices in Set A
- n = number of vertices in Set B

### Example:

K(2,3)

- 2 nodes on left
- 3 nodes on right
- All possible cross connections exist

---

# 🎯 Quick Comparison

| Feature                | Complete Graph | Bipartite Graph        |
|------------------------|---------------|------------------------|
| All nodes connected?   | ✅ Yes         | ❌ Only across sets     |
| Two separate groups?   | ❌ No          | ✅ Yes                  |
| Odd cycle allowed?     | ❌ Yes (exists) | ❌ Not allowed          |

---
