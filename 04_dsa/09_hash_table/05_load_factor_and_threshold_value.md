## Load Factor (α)

The **load factor** measures how full a hash table is. It is defined as:

```
α = (number of elements) / (table size)
```

A higher load factor means more collisions and slower operations.

---

## Threshold Value

The **threshold value** is the maximum load factor allowed before resizing the hash table.  
When the load factor exceeds this value, the table is rehashed into a larger table.

---

## Why They Matter

- If the load factor grows too large, collision handling becomes expensive.
- The threshold ensures hash table operations stay close to **O(1)** time.

---

## Common Values (Interview-Ready)

- **Typical load factor threshold:** `0.7 – 0.75`
- **Python `dict`:** resizes before reaching ~`0.66`
- **Java `HashMap` default:** `0.75`

---

## Simple Example

- **Table size:** `10`
- **Threshold:** `0.7` → **Max elements:** `7`
- **Insert 8th element:** Rehashing triggered

---

## One-Liner for Interview 🎯

> “Load factor shows how full the hash table is, and the threshold decides when resizing happens to control collisions.”