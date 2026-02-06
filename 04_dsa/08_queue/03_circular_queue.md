# Circular Queue

A **Circular Queue** is a queue where the last position connects back to the first, forming a circle. This structure allows reuse of empty spaces created after deletions, unlike a normal linear queue.

In a linear queue, once the `rear` reaches the end, you can’t insert new elements even if there’s space at the front. A circular queue solves this by wrapping `rear` back to the start using modulo arithmetic.

## How It Works (Array-Based)

- **front**: Points to the first element.
- **rear**: Points to the last element.
- **Next position**:  
    `(index + 1) % size`

## Core Operations

- **Enqueue**: Insert at `rear`, then update  
    `rear = (rear + 1) % size`
- **Dequeue**: Remove from `front`, then update  
    `front = (front + 1) % size`
- **isFull**:  
    `(rear + 1) % size == front`
- **isEmpty**:  
    `front == -1`

## Why Use a Circular Queue?

- Avoids memory wastage
- Improves space utilization
- Used in CPU scheduling, buffering, and streaming data

## Time Complexity

- **Enqueue**: O(1)
- **Dequeue**: O(1)