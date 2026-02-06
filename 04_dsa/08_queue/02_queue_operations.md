# Queue Using Class

## Queue Using Array (Python)

```python
class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if self.isFull():
            print("Queue Overflow")
            return

        if self.isEmpty():
            self.front = 0

        self.rear += 1
        self.queue[self.rear] = value
        print(value, "enqueued")

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None

        removed = self.queue[self.front]

        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1

        print(removed, "dequeued")
        return removed

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.queue[self.rear]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return self.rear == self.size - 1

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Queue elements:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()
```

---

## Queue Using Linked List

### Node Definition

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Queue Implementation

```python
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue (Insert at rear)
    def enqueue(self, value):
        new_node = Node(value)

        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(value, "enqueued")

    # Dequeue (Remove from front)
    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return None

        removed = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        print(removed, "dequeued")
        return removed

    # Front / Peek
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.front.data

    # Rear
    def getRear(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        return self.rear.data

    # isEmpty
    def isEmpty(self):
        return self.front is None

    # Display
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return

        temp = self.front
        print("Queue elements:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
```

### Example Usage

```python
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Front:", q.peek())
print("Rear:", q.getRear())

q.dequeue()
q.display()

print("isEmpty:", q.isEmpty())
```

#### Output (Expected)

```
10 enqueued
20 enqueued
30 enqueued
Queue elements: 10 20 30
Front: 10
Rear: 30
10 dequeued
Queue elements: 20 30
isEmpty: False
```

---

## Important Interview Points

- **Enqueue:** O(1) (insert at rear)
- **Dequeue:** O(1) (remove from front)
- No `isFull()` (dynamic memory)
- Underflow possible, overflow not required
- Uses two pointers: `front` and `rear`

**Interview Question:**  
**Q:** Why is linked list queue better than array queue?  
**A:** It avoids overflow, doesn’t waste space, and supports dynamic size.