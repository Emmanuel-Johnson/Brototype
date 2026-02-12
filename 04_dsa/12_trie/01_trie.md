# 🌳 Trie (Prefix Tree)

A **Trie** is a tree data structure used to store strings efficiently.

It's mainly used for:

-   🔎 Fast prefix search
-   📚 Dictionary words
-   🔤 Autocomplete
-   🧠 Spell check

------------------------------------------------------------------------

## 🧩 How It Works

Each node represents:

-   One character
-   Links to next characters
-   A flag to mark end of a word

### Example Words

    cat  
    car  
    dog

### Structure

            (root)
            /    \
           c      d
           |      |
           a      o
          / \      \
         t   r      g

### Notice

-   "cat" and "car" share prefix "ca"
-   That's why Trie is powerful --- **prefix sharing**

------------------------------------------------------------------------

# 🧠 Core Operations

## 1️⃣ Insert Word

**Steps:**

-   Start at root
-   For each character:
    -   If not present → create node
    -   Move to next node
-   Mark last node as end of word

⏱ **Time Complexity:** `O(L)`
`L = length of word`

------------------------------------------------------------------------

## 2️⃣ Search Word

**Steps:**

-   Traverse character by character
-   If character missing → return `False`
-   If end reached and marked → return `True`

⏱ **Time Complexity:** `O(L)`

------------------------------------------------------------------------

## 3️⃣ Starts With (Prefix Check)

**Steps:**

-   Same as search
-   Do NOT check end-of-word flag

⏱ **Time Complexity:** `O(L)`

------------------------------------------------------------------------

# ⏳ Time & Space Complexity

## Time

-   Insert → `O(L)`
-   Search → `O(L)`
-   Prefix → `O(L)`

## Space

Worst case: `O(N × L)`
`N = number of words`

Because each character becomes a node.

------------------------------------------------------------------------

# 🔥 Why Trie Over HashSet?

  Feature         HashSet   Trie
  --------------- --------- ---------
  Search word     O(1)      O(L)
  Prefix search   ❌        O(L) ✅
  Memory usage    Less      More

If prefix search is needed → **Trie wins**.

------------------------------------------------------------------------

# 💡 Interview Tip

If you see problems related to:

-   Autocomplete
-   Dictionary problems
-   Word search
-   Replace words
-   Prefix matching

👉 **Think Trie immediately**