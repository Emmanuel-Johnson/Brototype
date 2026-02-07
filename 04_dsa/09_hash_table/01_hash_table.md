# Hash Table

## What is a Hash Table?

A **Hash Table** is a data structure that stores and retrieves data as key–value pairs. It uses a hash function to convert a key into an index, allowing efficient access to values.

## Why Use a Hash Table?

Hash tables solve the problem of slow searching in arrays or lists. Without hashing, searching can take linear time (`O(n)`), but hash tables provide fast access (`O(1)` on average), even with large datasets.

## How Does a Hash Table Work?

- A **hash function** converts a key into an index.
- The value is stored at that index in an array-like structure (the table).
- To retrieve a value, the same hash function is used to find the correct index quickly.

## Handling Collisions

A **collision** occurs when two keys produce the same index. Common solutions include:
- **Chaining:** Store multiple values in a list at one index.
- **Open Addressing:** Find another empty slot in the table.

## Time Complexity

- **Insert:** O(1) average
- **Search:** O(1) average
- **Delete:** O(1) average
- **Worst case (many collisions):** O(n)

## Real-Life Uses

Hash tables are widely used in:
- Databases
- Caches
- Password storage
- Symbol tables in compilers
- Python dictionaries / Java `HashMap`