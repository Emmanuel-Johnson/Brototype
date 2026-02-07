## Hash Table Complexity

### Time Complexity

| Operation  | Average Case | Worst Case      |
|------------|--------------|----------------|
| Insertion  | O(1)         | O(n) (collisions) |
| Search     | O(1)         | O(n)           |
| Deletion   | O(1)         | O(n)           |

> **Note:** Average case assumes a good hash function and a low load factor.

---

#### Why Can Worst Case Be O(n)?

When many keys hash to the same index (especially with chaining), the hash table acts like a linked list, making operations linear time.

---

### Effect of Collision Handling

- **Chaining:**  
    - Average: O(1 + α), where α = load factor  
    - Worst: O(n)
- **Open Addressing (Linear/Quadratic Probing):**  
    - Average: O(1)  
    - Performance drops sharply as load factor approaches 1

---

### Space Complexity

- **O(n):** Extra space is needed for the hash table and collision handling structures.

---

### Interview One-Liner 🎯

> “Hash table operations run in O(1) average time, but can degrade to O(n) in the worst case due to collisions.”
