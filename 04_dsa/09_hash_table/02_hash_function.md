## What is a Hash Function?

A **hash function** takes a key and converts it into a fixed-size number (an index) used to store or find data in a hash table.

---

## Why Use a Hash Function?

A hash function determines where to store data in a hash table. Without it, we wouldn’t know which index a key belongs to, making fast access impossible.

---

## How Does a Hash Function Work?

A hash function applies a mathematical formula to the key and produces an index within the table size.

**Example:**
```python
index = key % table_size
```

---

## Characteristics of a Good Hash Function

A good hash function should:

- Be fast to compute
- Distribute keys uniformly
- Minimize collisions
- Always give the same output for the same key

---

## Bad Hash Functions

A bad hash function causes many keys to map to the same index, leading to too many collisions and slow performance.

---

## Example

If `table_size = 10`:

- Key = 25 → `25 % 10 = 5`
- Key = 35 → `35 % 10 = 5` _(collision)_

---

## Role in Hash Table

The efficiency of a hash table depends heavily on the hash function. Even a good collision-handling method cannot compensate for a poor hash function.