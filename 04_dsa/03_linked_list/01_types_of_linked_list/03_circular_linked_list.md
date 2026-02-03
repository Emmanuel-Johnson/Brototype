# Circular Linked List

## 1. WHAT
Circular Linked List is a linear data structure used to store nodes where the last node points back to the first node. It is used to form a continuous loop of data.

## 2. WHY
It solves the problem of restarting traversal without resetting to the head. Without it, repeated cycling through data requires extra checks and manual pointer resets.

## 3. WHERE
It fits in the data management layer where resources or tasks are reused cyclically. It is commonly used in schedulers, buffers, and rotation-based system components.

## 4. HOW
Nodes are linked sequentially like a normal linked list. The last node’s next pointer is set to the head node. Traversal continues until a full cycle is detected.

## 5. WHEN
Use it when data needs to be processed repeatedly in a loop. Do not use it when a clear start and end of data is required.

## 6. EXAMPLE
In a round-robin CPU scheduler, processes are stored in a circular linked list so each process gets CPU time in turn.

## 7. PROS & CONS
It allows efficient cyclic traversal and eliminates the need for null checks at the end. However, traversal termination is tricky and debugging becomes harder.

## 8. COMMON MISTAKES
Forgetting the stopping condition can cause infinite loops. Incorrectly updating the last node pointer can break the circular structure.
