# 🌳 Tree vs 🌲 Trie (Prefix Tree)

---

## 🔍 Feature Comparison

| Feature | Tree | Trie |
|------|------|------|
| **Meaning** | General hierarchical structure | Specialized tree for strings |
| **Data Stored** | Any data (int, object, etc.) | Characters |
| **Node Represents** | A value | A prefix |
| **Root** | Any value | Usually empty node |
| **Children** | Any meaning | Characters (a–z) |
| **Searching** | Depends on type (BST, etc.) | Prefix-based |
| **Time Complexity** | `O(log n)` (BST avg) | `O(m)` (word length) |
| **Space Usage** | Efficient | Higher (many nodes) |

---

## 🌳 What is a Tree?

A **Tree** is a general **hierarchical data structure**.

### Used for:
- File systems  
- Databases  
- Expression trees  
- BST, AVL Tree, Heap  

### Example:
```
        10
       /  \
      5    20
```

📌 Search performance depends on the structure  
(BST, balanced or skewed).

---

## 🌲 What is a Trie?

Also called a **Prefix Tree**.

- Optimized for **strings**
- Each level represents **one character**
- Paths form complete words

### Example (words: cat, car):
```
        (root)
          |
          c
          |
          a
         / \
        t   r
```

---

## 🔍 Searching Difference (IMPORTANT)

### Tree (BST)
- Search depends on height
- Worst case: `O(n)`

### Trie
- Search depends on word length
- Always: `O(m)` where `m = length of word`

👉 That’s why **Tries are used in autocomplete**.

---

## 💾 Space Difference

- **Tree** → Stores values only  
- **Trie** → Stores characters + pointers  

⚠️ Trie uses **more memory**, but gives **faster string search**.

---

## 🧠 When to Use What?

### ✅ Use Tree when:
- Hierarchical data
- Numeric comparisons
- Sorting / searching
- Balanced performance needed

### ✅ Use Trie when:
- Words / strings
- Prefix search
- Autocomplete
- Spell checker
- Dictionary lookup

---

## 📌 Real-World Examples

- **Tree** → File system, DOM, database indexes  
- **Trie** → Google search suggestions, phone contacts, IDE autocomplete  

---

## 🔥 Interview One-Liner

**Tree** organizes data hierarchically;  
**Trie** organizes strings character by character.