# 🌲 Trie -- Time & Space Complexity

Let:

-   `n` = number of words
-   `L` = length of word
-   `Σ` = alphabet size (like 26 for lowercase letters)

------------------------------------------------------------------------

## 1️⃣ Insert

### 🔤 Steps:

-   Go character by character
-   Create node if not exists
-   Mark end of word

### ⏱ Time Complexity

  Case        Time
  ----------- ------
  All cases   O(L)

### 💡 Why?

You process each character once.

It does **NOT** depend on total number of words `n`.

------------------------------------------------------------------------

## 2️⃣ Search (Full Word)

  Case        Time
  ----------- ------
  All cases   O(L)

Same logic --- go character by character.

------------------------------------------------------------------------

## 3️⃣ StartsWith (Prefix Search)

  Case        Time
  ----------- ------
  All cases   O(L)

We just stop early without checking end-of-word.

------------------------------------------------------------------------

# 🔥 Important Insight

Unlike BST:

-   BST search → depends on height (`log n` or `n`)
-   Trie search → depends on length of word

That's the magic ✨

------------------------------------------------------------------------

# 📦 Space Complexity

This is where Trie gets expensive 👀

## Worst Case Space

If no prefixes are shared:

Total nodes ≈ `n × L`

**Space = O(n × L)**

------------------------------------------------------------------------

## With Shared Prefixes

Example:

    cat
    car
    cart

They share `ca` → so memory is reused.

So in real-world cases, space is often much less than `n × L`.

------------------------------------------------------------------------

## 🧠 Per Node Space

Each node stores:

-   Up to `Σ` children pointers
-   Boolean flag

If using array of size 26:

Each node → **O(Σ)**

So total space more precisely:

**O(total_characters × Σ)**

------------------------------------------------------------------------

If using hashmap instead of array:

-   More memory efficient
-   Slightly slower than array access

------------------------------------------------------------------------

# 🌟 Final Interview Summary

  Operation    Time
  ------------ ----------
  Insert       O(L)
  Search       O(L)
  StartsWith   O(L)
  Space        O(n × L)

------------------------------------------------------------------------

# 🚀 When is Trie Better Than BST?

Use Trie when:

-   You need prefix search
-   Autocomplete
-   Dictionary lookups
-   Word search problems

BST can't efficiently do prefix matching.