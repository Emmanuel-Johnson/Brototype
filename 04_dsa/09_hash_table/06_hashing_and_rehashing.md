## Hashing

Hashing is a technique that converts a key into an index using a hash function, enabling fast storage and retrieval in a hash table. It allows average-time O(1) operations for insert, search, and delete.

---

## Rehashing

Rehashing involves resizing the hash table and recomputing hash values when the load factor exceeds a threshold. All elements are reinserted into the new, larger table using the updated table size.

---

### Why Rehashing Is Needed

As more elements are added, collisions increase and performance drops. Rehashing reduces collisions and restores near constant-time performance.

---

### Simple Flow

1. Insert elements using hashing.
2. Load factor exceeds threshold.
3. Create a bigger table (usually 2× size).
4. Recompute hash for all keys.
5. Insert them into the new table.

---

### Cost

- Rehashing is expensive (O(n)), but occurs infrequently.
- Average performance remains O(1).

---

### Interview One-Liner 🎯

> Hashing maps keys to indexes for fast access, and rehashing resizes the table when it becomes too full to maintain performance.