# Hash Table

## ✅ Definition (1 line)

A hash table is a data structure that stores key--value pairs and uses a
hash function to compute an index for fast access.

------------------------------------------------------------------------

## 🚀 3--5 Applications of Hash Table

-   Database indexing
-   Caching (e.g., storing recently accessed data)
-   Frequency counting (like counting characters in a string)
-   Implementing dictionaries/maps (Python dict, Java HashMap)
-   Symbol tables in compilers

------------------------------------------------------------------------

## 🔎 Brief Explanation (1--2 Applications)

### 1️⃣ Caching

Hash tables are used to store recently used data for quick retrieval.

Since average lookup time is O(1), it makes applications faster.

### 2️⃣ Frequency Counting

Example: Count how many times each character appears in a string.

We store:

    {
      'a': 3,
      'b': 1,
      'c': 2
    }

This is heavily used in problems like anagrams and duplicates detection.