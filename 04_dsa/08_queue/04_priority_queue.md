# Priority Queue

A **Priority Queue** is a data structure where each element has a priority, and elements are removed based on their priority rather than the order they were added. This is useful when certain tasks must be processed before others.

In a **normal queue**, elements follow the First-In-First-Out (FIFO) principle. In a **priority queue**, the element with the highest (or lowest) priority is served first, regardless of when it was added.

## Types of Priority Queues

- **Max Priority Queue**: The element with the highest priority is removed first.
- **Min Priority Queue**: The element with the lowest priority is removed first.

## Implementation Methods

- **Heap (most common)**: Efficient and fast.
- **Array or Linked List**: Simpler but less efficient.

## Core Operations

- **Insert**: Add an element with a given priority.
- **Delete / Extract**: Remove the element with the highest (or lowest) priority.
- **Peek**: View the element with the highest priority without removing it.

## Time Complexity (Heap-based)

- **Insert**: O(log n)
- **Delete**: O(log n)
- **Peek**: O(1)

## Real-life Examples

- CPU scheduling (process with the highest priority runs first)
- Dijkstra’s algorithm (shortest path)
- Emergency room systems (patients with the most critical needs are treated first)
