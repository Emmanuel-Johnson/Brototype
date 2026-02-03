```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
        
    def convert_array_to_sll(self, arr):
        if not arr:
            return
        self.head = Node(arr[0])
        current = self.head
        for i in arr[1 : ]:
            current.next = Node(i)
            current = current.next
            
    def insert_node_before_value(self, value, data):
        newnode = Node(data)
        if self.head is None:
            return
        
        if self.head.data == value:
            newnode.next = self.head
            self.head = newnode
            return
        
        current = self.head
        while current.next:
            if current.next.data == value:
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
            
    def insert_node_after_value(self, value, data):
        newnode = Node(data)
        if self.head is None:
            return
        current = self.head
        while current:
            if current.data == value:
                newnode.next = current.next
                current.next = newnode
                return
            current = current.next
            
    def insert_node_at_index(self, index, data):
        newnode = Node(data)
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            return
        current = self.head
        i = 0
        while current:
            if i + 1 == index:
                newnode.next = current.next
                current.next = newnode
                return
            i += 1
            current = current.next
        print("Index out of range!")
        
    def delete(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def display_reversed_recursive(self):
        def _print_reverse(node):
            if node is None:
                return
            _print_reverse(node.next)
            print(node.data)
        _print_reverse(self.head)
        
    def display_reversed_iterative(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop())
            
    def remove_duplicates(self):
        if self.head is None:
            return
        current = self.head
        seen = {current.data}
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next
    
    def reverse_sll(self):
        if self.head is None:
            return
        current = self.head
        prev = None
        while current.next:
            move = current.next
            current.next = prev
            prev = current
            current = move
        current.next = prev
        self.head = current

sll = SinglyLinkedList()

# sll.insert_at_begin(10)
# sll.insert_at_begin(15)
# sll.insert_at_begin(20)

sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_end(30)
sll.insert_at_end(40)
sll.insert_at_end(50)

# sll.convert_array_to_sll([1, 2, 3, 4, 5])

# sll.insert_node_before_value(20, 200)

# sll.insert_node_after_value(20, 500)

# sll.insert_node_at_index(2, 500)

# sll.insert_node_at_index(4, 1000)

# sll.delete(1)

# sll.display_reversed_recursive()

# sll.display_reversed_iterative()

# sll.remove_duplicates()

# sll.reverse_sll()

sll.display()
```
