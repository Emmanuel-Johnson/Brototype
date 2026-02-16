# Trie

## ✅ Definition (1 line)

A trie (prefix tree) is a tree-based data structure used to store
strings where each node represents a character of a word.

------------------------------------------------------------------------

## 🚀 3--5 Applications of Trie

-   Autocomplete systems
-   Spell checking
-   Dictionary word storage
-   Prefix searching
-   IP routing (Longest Prefix Matching)

------------------------------------------------------------------------

## 🔎 Brief Explanation (1--2 Applications)

### 🔍 Autocomplete Systems

Tries are perfect for autocomplete.

If we store words like:

-   cat
-   car
-   cap

They share the prefix "ca", so they share the same branch in the trie.

Typing "ca" quickly gives all possible matches --- very efficient.

Time complexity for search → O(L)
(where L = length of the word, not number of words)

### 🌐 IP Routing

Routers use tries to match the longest prefix of an IP address to decide
where to forward data packets.

This makes networking super efficient.