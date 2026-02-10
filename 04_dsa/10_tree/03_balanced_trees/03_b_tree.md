# 🌳 B-Tree

A **B-Tree** is a **self-balancing search tree** designed to store **large amounts of data efficiently**, especially on **disk** (databases & file systems).

---

## 💡 Big Idea

Instead of **1 key per node** (like BST), a **B-Tree node stores MANY keys and MANY children**.

---

## 🧠 Why B-Tree Exists (Intuition)

- AVL / Red-Black Trees are great **in memory** 🧠  
- Disk access is **slow** 💽  

👉 **B-Tree:**
- Keeps the tree **short & wide**
- Minimizes **disk reads**
- Perfect for **databases**

---

## 📦 Structure of a B-Tree (Order = m)

For a B-Tree of order **m**:

- Each node can have **at most m children**
- Each node can store **at most m − 1 keys**
- Each node (except root) has **at least ⌈m/2⌉ children**
- Keys inside a node are **sorted**
- **All leaves are at the same level** ✅

---

## 🧩 Example (Order = 4)

- Max children = `4`
- Max keys = `3`

A node might look like:

```
| 10 | 20 | 30 |
 /     |     \
C1    C2     C3
```

👉 Each key range decides which **child path** to follow.

---

## 🔁 Insertion (High Level)

1️⃣ Insert the key into the **correct leaf**  
2️⃣ If the node **overflows** (too many keys):
- Split the node
- Move the **middle key up**
3️⃣ Repeat upward if needed  

✨ The tree stays **balanced automatically**.

---

## ⏱️ Time Complexity

| Operation | Time |
|---------|------|
| Search | O(log n) |
| Insert | O(log n) |
| Delete | O(log n) |

📉 Height stays **very small** due to wide nodes.

---

## 🌲 B-Tree vs Binary Trees

| Feature | AVL / Red-Black Tree | B-Tree |
|------|---------------------|--------|
| Keys per node | 1 | Many |
| Children | 2 | Many |
| Height | Taller | Very short |
| Disk access | ❌ Poor | ✅ Excellent |
| Use case | Memory | Databases |

---

## 🧠 Where B-Trees Are Used

- Database indexes (MySQL, PostgreSQL)
- File systems (NTFS, ext4)
- Large storage systems

👉 You probably used it **today without knowing** 😄

---

## 🧠 One-Line Summary

```
B-Tree = Wide, shallow, disk-optimized search tree
```