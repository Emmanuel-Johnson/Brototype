# Doubly Linked List

## 1. WHAT
Doubly Linked List is a linear data structure used to store elements as nodes, where each node points to both the next and previous nodes. It is used to allow two-way traversal of data.

## 2. WHY
It solves the limitation of one-direction traversal in singly linked lists. Without it, moving backward or deleting a node without tracking the previous node becomes difficult and repetitive.

## 3. WHERE
It fits in the data structure layer of a system where ordered data needs forward and backward navigation. It is commonly used in system components like memory managers and navigation logic.

## 4. HOW
Each node stores data, a next pointer, and a previous pointer. Operations update both pointers during insertion or deletion. Traversal can move in either direction starting from any node.

## 5. WHEN
Use it when frequent insertions, deletions, and bidirectional traversal are required. Do not use it when memory is constrained or backward traversal is unnecessary.

## 6. EXAMPLE
In a browser history feature, pages are stored in a doubly linked list to allow moving back and forward efficiently.

## 7. PROS & CONS
It supports easy two-way traversal and faster deletions compared to singly linked lists. However, it uses extra memory for pointers and has more complex pointer management.

## 8. COMMON MISTAKES
Forgetting to update both next and previous pointers can break the list. Using it where a singly linked list is sufficient leads to unnecessary memory usage.
