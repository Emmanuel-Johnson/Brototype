# Stack Using Class

```python
class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1
        
    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow!")
            return
        self.stack.append(data)
        self.top += 1
        
    def pop(self):
        if self.top == -1:
            print("Stack Underflow!")
            return None
        self.top -= 1
        return self.stack.pop()
        
    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]
        
    def display(self):
        if self.top == -1:
            print("Stack is Empty!")
            return
        print("Stack (Top to Bottom) :- ")
        for i in range(self.top, -1, -1):
            print(self.stack[i])

    def is_empty(self):
        return self.top == -1
        
    def is_full(self):
        return self.top == self.size - 1
        
s = Stack(5)

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()
```

<br>
<br>
<br>

# Stack Using Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        newnode = Node(data)
        newnode.next = self.top
        self.top = newnode
    
    def pop(self):
        if self.top is None:
            print("Stack is Underflow!")
            return None
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data
        
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
        
    def display(self):
        if self.top is None:
            print("Stack is empty!")
            return
        
        current = self.top
        print("Stack (Top to Bottom) :- ", end = " ")
        while current:
            print(f"{current.data}", end = "  ")
            current = current.next
        print()
    
    def is_empty(self):
        return self.top is None
        
s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.display()

print(s.peek())
```
