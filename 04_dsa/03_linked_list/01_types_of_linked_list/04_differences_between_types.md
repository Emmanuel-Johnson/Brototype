# Linked List Types

## Singly Linked List
A singly linked list is a linear data structure where each node stores data and a reference to the next node. Traversal is possible only in one direction (forward), and it uses less memory because it stores only one link per node.

## Doubly Linked List
A doubly linked list is a linear data structure where each node stores data, a previous pointer, and a next pointer. It allows traversal in both forward and backward directions but requires extra memory for the additional pointer.

## Circular Linked List
A circular linked list is a linked list where the last node points back to the first node instead of `null`. This creates a loop, making traversal continuous, which is useful in applications like round-robin scheduling.

---

## Differences Between Linked List Types

| Feature                | Singly Linked List | Doubly Linked List | Circular Linked List |
|------------------------|-------------------|--------------------|----------------------|
| Pointers per node      | 1 (next)          | 2 (prev, next)     | 1 or 2               |
| Traversal              | One direction     | Both directions    | Continuous loop      |
| Memory usage           | Lowest            | Highest            | Medium               |
| Last node points to    | null              | null               | Head node            |
| Implementation         | Simple            | Complex            | Moderate             |
