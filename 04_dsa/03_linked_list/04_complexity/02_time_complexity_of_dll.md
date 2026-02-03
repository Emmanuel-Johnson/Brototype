# Doubly Linked List – Time Complexity

| Operation                 | Time Complexity | Explanation                                      |
|---------------------------|-----------------|--------------------------------------------------|
| Access (by index)         | O(n)            | No direct indexing; traversal required           |
| Search                    | O(n)            | Can traverse from head or tail                   |
| Insertion at beginning    | O(1)            | Update head and previous pointers                |
| Insertion at end          | O(1)*           | Direct insertion if tail pointer exists          |
| Insertion at middle       | O(n)            | Traversal needed to reach the position           |
| Deletion at beginning     | O(1)            | Update head and previous pointer                 |
| Deletion at end           | O(1)*           | Direct deletion if tail pointer exists           |
| Deletion at middle        | O(n)            | Traversal required to reach the target node      |

\* **O(1)** assumes a tail pointer is maintained.

## Key Interview Line

A doubly linked list allows **O(1)** insertion and deletion at **both ends**, but **access and search still take O(n)**.
