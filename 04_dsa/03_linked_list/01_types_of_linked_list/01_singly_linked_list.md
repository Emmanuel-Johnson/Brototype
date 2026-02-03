# Singly Linked List

## 1. WHAT
Singly Linked List is a linear data structure used to store elements as nodes, where each node points to the next node in sequence. It is used to manage dynamic collections of data without fixed size.

## 2. WHY
It solves the problem of fixed-size arrays and costly shifting during insertions or deletions. Without it, frequent insert/delete operations become repetitive and inefficient due to data movement.

## 3. WHERE
It fits in the data handling layer of a system, especially in memory-level data management. It is commonly used inside system utilities, data processing pipelines, and backend logic.

## 4. HOW
Each node stores data and a reference to the next node. Operations start from the head node and move forward one node at a time. Insertion or deletion adjusts pointers instead of shifting data.

## 5. WHEN
Use it when frequent insertions and deletions are needed and random access is not required. Do not use it when fast index-based access is critical, like in array-heavy algorithms.

## 6. EXAMPLE
In a task management app, tasks can be stored as a singly linked list where new tasks are added or removed dynamically without reallocating memory.

## 7. PROS & CONS
It allows dynamic size and efficient insertions/deletions with low memory overhead. However, it has slower access time and no backward traversal support.

## 8. COMMON MISTAKES
Forgetting to update pointers during deletion can cause memory leaks. Using it where frequent random access is required leads to poor performance.
