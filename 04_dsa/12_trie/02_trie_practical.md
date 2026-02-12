# 🌳 Trie Implementation in Python

## 📌 TrieNode Class

``` python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

------------------------------------------------------------------------

## 📌 Trie Class

``` python
class Trie:
    def __init__(self):
        self.root = TrieNode()

    # ===============================
    # 🔹 Insert Word
    # ===============================
    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            
            node = node.children[ch]
        
        node.is_end = True

    # ===============================
    # 🔹 Search Full Word
    # ===============================
    def search(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return node.is_end

    # ===============================
    # 🔹 Search Prefix
    # ===============================
    def starts_with(self, prefix):
        node = self.root
        
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        
        return True
```