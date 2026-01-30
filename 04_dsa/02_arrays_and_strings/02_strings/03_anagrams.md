# Anagrams

## What is an Anagram?

Two strings are **anagrams** if:

* They contain the **same characters**
* With the **same frequency**
* The **order does not matter**

---

## Examples

### ✅ Anagrams

* `"listen"` ↔ `"silent"`
* `"evil"` ↔ `"vile"`
* `"race"` ↔ `"care"`

### ❌ Not Anagrams

* `"hello"` ↔ `"world"` (different letters)
* `"aab"` ↔ `"abb"` (different frequency)

---

## How to Check Anagrams (Main Idea)

---

### Method 1️⃣: Sorting (Easy to Understand)

#### Steps

1. Convert both strings to arrays
2. Sort them
3. Compare the results

```python
s1 = "listen"
s2 = "silent"

sorted(s1) == sorted(s2)   # True
```

#### Time Complexity

* Sorting → `O(n log n)`

---

### Method 2️⃣: Frequency Count (Best Method ⭐)

#### Steps

1. Count characters in both strings
2. Compare the counts

```python
from collections import Counter

Counter("listen") == Counter("silent")
```

#### Time Complexity

* Counting → `O(n)`
* Comparison → `O(1)` (fixed alphabet)

✅ More efficient than sorting

---

### Method 3️⃣: Using Array (Interview-Style)

For lowercase English letters only:

```python
def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    count = [0] * 26

    for i in range(len(s1)):
        count[ord(s1[i]) - ord('a')] += 1
        count[ord(s2[i]) - ord('a')] -= 1

    return all(c == 0 for c in count)
```

#### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

---

## Important Points ⚠️

* Length of both strings must be the same
* Case sensitivity matters (`"Listen" ≠ "silent"`)
* Spaces and symbols should be handled if present

---

## One-Line Definition (Exam Ready 🎯)

> **Two strings are anagrams if they contain the same characters with the same frequency but in a different order.**
