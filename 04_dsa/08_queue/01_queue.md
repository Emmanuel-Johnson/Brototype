## 1. What is a Queue?
A queue is a linear data structure that stores elements in the order they arrive and processes them in the same order, following the FIFO (First In, First Out) principle.

## 2. Why Use a Queue?
Queues solve the problem of fair and ordered processing for multiple tasks or requests. Without queues, managing order manually can become complex and error-prone.

## 3. Where are Queues Used?
Queues are commonly found in request–response systems, scheduling layers, and buffering components. They act as intermediaries between producers (who add data) and consumers (who process data).

## 4. How Does a Queue Work?
Elements are added at the rear (enqueue) and removed from the front (dequeue). The queue maintains order so the earliest inserted element is always processed first.

## 5. When to Use a Queue?
Use a queue when order matters and tasks must be handled sequentially, such as in job scheduling or message handling. Avoid queues when random access or frequent middle-element operations are needed.

## 6. Example
In a web server, incoming client requests are placed in a queue and processed one by one by worker threads, ensuring fairness and stability.

## 7. Pros & Cons
Queues provide predictable ordering and simplify task coordination, improving system fairness. However, they only allow access from the front and rear, and slow processing can cause delays.

## 8. Common Mistakes
Common mistakes include confusing queues with stacks and breaking FIFO order, or not handling overflow/underflow in fixed-size queue implementations.

<br>
<br>
<br>

# Queue (FIFO – First In, First Out)

A **queue** is a linear data structure that works on **FIFO (First In, First Out)**.  
Think of a line at a ticket counter 🎟️ — the first person in line is the first to be served.

---

## 🔹 Core Idea

- **Insert (Enqueue)** → happens at the **rear**
- **Remove (Dequeue)** → happens from the **front**

---

## 🔹 Basic Operations

| Operation        | Meaning                              |
|------------------|--------------------------------------|
| `enqueue(x)`     | Add element `x` to the rear           |
| `dequeue()`      | Remove element from the front         |
| `peek()` / `front()` | View the front element           |
| `isEmpty()`      | Check if the queue is empty           |
| `isFull()`       | Check if the queue is full (array-based) |

---

## 🔹 Types of Queues

- **Simple Queue** – Basic FIFO queue  
- **Circular Queue** – Last position connects to first (saves space)  
- **Priority Queue** – Elements are served based on priority, not arrival time  
- **Deque (Double Ended Queue)** – Insertion and deletion from both ends  

---

## 🔹 Time Complexity

| Operation | Time Complexity |
|----------|-----------------|
| Enqueue  | O(1)            |
| Dequeue  | O(1)            |
| Peek     | O(1)            |

---

## 🔹 Real-Life Use Cases

- CPU scheduling 🖥️  
- Printer job management 🖨️  
- BFS (Breadth-First Search) in graphs 🌐  
- Call center systems ☎️  
