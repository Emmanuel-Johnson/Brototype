# Hash Table Implementation (with Chaining)

## 🔹 Idea

- Use an array of buckets.
- Each bucket stores (key, value) pairs.
- Hash function maps a key → bucket index.

---

## ✅ Code

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def _hash(self, key):
        return hash(key) % self.size

    # Insert / Update
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update
                return

        bucket.append((key, value))  # insert new

    # Get value
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    # Remove key
    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    # Display hash table
    def display(self):
        for i, bucket in enumerate(self.table):
            print(i, ":", bucket)
```

---

## 🧪 Example Usage

```python
ht = HashTable()

ht.put("name", "Emmanuel")
ht.put("age", 22)
ht.put("role", "Developer")

print(ht.get("name"))   # Emmanuel
ht.remove("age")

ht.display()
```

---

## ⏱ Time Complexity

- **Insert:** O(1) average, O(n) worst
- **Search:** O(1) average, O(n) worst
- **Delete:** O(1) average, O(n) worst

---

## 🧠 Interview Tip

> **Q:** How are collisions handled?  
> **A:** Using separate chaining (linked list / dynamic array per bucket).

<br>
<br>

# Hash Table Implementation (with Open Addressing / Linear Probing)

```python
class HashTable:
    DELETED = object()   # unique marker

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)

        while self.table[index] not in (None, self.DELETED):
            k, _ = self.table[index]
            if k == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size

        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        start = index

        while self.table[index] is not None:
            if self.table[index] is not self.DELETED:
                k, v = self.table[index]
                if k == key:
                    return v

            index = (index + 1) % self.size
            if index == start:
                break

        return None

    def remove(self, key):
        index = self._hash(key)
        start = index

        while self.table[index] is not None:
            if self.table[index] is not self.DELETED:
                k, _ = self.table[index]
                if k == key:
                    self.table[index] = self.DELETED
                    return True

            index = (index + 1) % self.size
            if index == start:
                break

        return False
```

---

### How it works

- Uses open addressing with linear probing for collision resolution.
- Deleted slots are marked with a unique `DELETED` object.
- Insert, search, and delete operations probe sequentially for the correct slot.

---

### Time Complexity

- **Insert/Search/Delete:** O(1) average, O(n) worst (when many collisions)

---

### Interview Tip

> **Q:** How are collisions handled?  
> **A:** By linear probing (sequentially searching for the next available slot).
