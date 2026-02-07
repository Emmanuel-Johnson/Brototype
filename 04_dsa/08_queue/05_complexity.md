# Queue Complexity

Queues (FIFO) are optimized for constant-time operations, making them ideal for scheduling, buffering, and real-time systems.

## Time Complexity

- **Enqueue (insert):** `O(1)`  
    Adds an element at the rear in constant time.

- **Dequeue (delete):** `O(1)`  
    Removes an element from the front in constant time.

- **Front / Peek:** `O(1)`  
    Accesses the front element.

- **Rear:** `O(1)`  
    Accesses the last element.

- **isEmpty / isFull:** `O(1)`

> **Note:**  
> - Linked list queues and circular array queues maintain these complexities.  
> - ⚠️ Simple array queues (non-circular) may have `O(n)` enqueue due to element shifting.

## Space Complexity

- **O(n):**  
    Space required to store `n` elements.

## Interview One-Liner

Queue operations like enqueue and dequeue run in `O(1)` time, making queues efficient for FIFO-based processing.