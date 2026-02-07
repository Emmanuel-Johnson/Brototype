## What is a Collision?

A **collision** occurs when two different keys produce the same hash index in a hash table.

---

## Why Do Collisions Happen?

Collisions occur because the number of possible keys exceeds the number of available slots in the hash table. No matter how well-designed the hash function is, multiple keys may map to the same index.

---

## Collision Handling Techniques

### 1. Chaining

- Each table index holds a list (often a linked list) of all elements that hash to that index.
- Simple to implement.
- No overflow issue; performance depends on the length of the lists.

### 2. Open Addressing

When a collision occurs, the algorithm searches for another empty slot in the table.

- **Linear Probing:** Checks subsequent slots one by one. Simple but can cause clustering.
- **Quadratic Probing:** Uses a quadratic formula to determine the next slot, reducing clustering.
- **Double Hashing:** Applies a second hash function to decide the step size, offering the best distribution among probing methods.

---

## Time Complexity

- **Average case (good hash, low load):** `O(1)`
- **Worst case (many collisions):** `O(n)`

---

## Real-World Note

Languages like Python and Java use advanced collision handling to maintain near `O(1)` performance.

---

## Interview One-Liner 💡

> A collision happens when two keys map to the same index; it is handled using chaining or open addressing.

---

### Quick Comparison of Collision Handling Methods

| Method             | Extra Space | Clustering | Implementation |
|--------------------|-------------|------------|----------------|
| Chaining           | Yes         | No         | Easy           |
| Linear Probing     | No          | High       | Very Easy      |
| Quadratic Probing  | No          | Medium     | Moderate       |

---

### Summary of Methods

**Chaining:**  
Each index stores a list of entries. Easy to implement, no overflow, but performance depends on list length.  
- Average: `O(1)`, Worst: `O(n)`

**Linear Probing:**  
Checks next slots sequentially until an empty one is found. Simple and cache-friendly, but causes primary clustering.  
- Average: `O(1)`, Worst: `O(n)`

**Quadratic Probing:**  
Jumps to slots using a quadratic formula, reducing clustering but may not cover all slots.  
- Average: `O(1)`, Worst: `O(n)`
