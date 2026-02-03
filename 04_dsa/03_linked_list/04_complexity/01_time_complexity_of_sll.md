# Singly Linked List – Time Complexity

| Operation                 | Time Complexity | Explanation                                      |
|---------------------------|-----------------|--------------------------------------------------|
| Access (by index)         | O(n)            | Must traverse from the head node                 |
| Search                    | O(n)            | Each node is checked one by one                  |
| Insertion at beginning    | O(1)            | Only the head pointer is updated                 |
| Insertion at end          | O(n)            | Traversal required to reach the last node        |
| Insertion at middle       | O(n)            | Need traversal to the required position          |
| Deletion at beginning     | O(1)            | Head is moved to the next node                   |
| Deletion at end           | O(n)            | Traverse to the second-last node                 |
| Deletion at middle        | O(n)            | Traversal needed to reach the target node        |

## Key Interview Line

A singly linked list supports **O(1)** insertion and deletion **only when the position is already known**; otherwise, traversal makes the operation **O(n)**.
