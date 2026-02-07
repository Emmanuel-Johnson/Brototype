### 1️⃣ Division Method

The most common method. The key is divided by the table size, and the remainder is used as the index.

**Example:**  
`h(k) = k % m`  
Simple and fast, but a poor choice of `m` can cause collisions.

---

### 2️⃣ Multiplication Method

The key is multiplied by a constant fraction, and the fractional part is used to compute the index.  
This method distributes keys better than division and is less dependent on table size.

---

### 3️⃣ Mid-Square Method

The key is squared, and the middle digits of the result are taken as the index.  
It reduces the effect of patterns in keys but involves extra computation.

---

### 4️⃣ Folding Method

The key is split into equal parts, and those parts are added together to form the index.  
Useful when keys are very large numbers like phone numbers or account IDs.

---

### 5️⃣ Universal Hashing

A hash function is chosen randomly from a set of functions to reduce collision chances.  
Commonly used in advanced implementations to protect against worst-case inputs.

---

### 6️⃣ Perfect Hashing

Used when the set of keys is fixed and known in advance.  
It guarantees no collisions, but is expensive to construct.

---

> **INTERVIEW TIP 🎯**  
> For most real-world systems, division or multiplication methods are used along with good collision handling.

---

## Division Method (Hashing) — Simple Example

Suppose we have:

- Hash table size (`m`) = 10  
- Key (`k`) = 123

**Formula:**  
`h(k) = k mod m`

**Step 1:** Apply modulo operation  
`123 mod 10 = 3`

✅ **Final Result:**  
The key `123` is stored at index `3` in the hash table.

---

## Multiplication Method (Hashing) — Simple Example

Suppose we have:

- Hash table size (`m`) = 10  
- Key (`k`) = 123  
- Constant fraction (`A`) = 0.618 (a commonly used value)

**Step 1:** Multiply the key by `A`  
`k × A = 123 × 0.618 = 75.914`

**Step 2:** Take only the fractional part  
`fractional part = 0.914`

**Step 3:** Multiply by table size (`m`)  
`0.914 × 10 = 9.14`

**Step 4:** Take the floor value  
`Index = ⌊9.14⌋ = 9`

✅ **Final Result:**  
The key `123` is stored at index `9` in the hash table.
