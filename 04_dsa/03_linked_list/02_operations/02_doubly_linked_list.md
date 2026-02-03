class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_begin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            
    def insert_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
            
    def convert_arr_to_dll(self, arr):
        if not arr:
            return
        
        newnode = Node(arr[0])
        self.head = newnode
        self.tail = newnode
        
        for i in arr[1 : ]:
            newnode = Node(i)
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
            
    def delete(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        
        current = self.head.next
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.prev
                    current.prev.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
            
    def insert_node_before(self, value, data):
        if self.head is None:
            return
        if self.head.data == value:
            self.insert_at_begin(data)
            return
        current = self.head
        while current.next:
            if current.next.data == value:
                newnode = Node(data)
                newnode.next = current.next
                current.next.prev = newnode
                newnode.prev = current
                current.next = newnode
                break
            current = current.next
            
    def insert_node_after(self, value, data):
        if self.head is None:
            return
        current = self.head
        while current:
            if current.data == value:
                if current == self.tail:
                    self.insert_at_end(data)
                    return
                else:
                    newnode = Node(data)
                    newnode.next = current.next
                    current.next.prev = newnode
                    newnode.prev = current
                    current.next = newnode
                    return
            current = current.next
            
    def reverse(self):
        if self.head is None:
            return
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head
        
    def insert_node_at_index(self, index, data):
        if index < 0:
            return
        if index == 0:
            self.insert_at_begin(data)
            return
        current = self.head
        i = 0
        while current:
            if i == index - 1:
                if current == self.tail:
                    self.insert_at_end(data)
                else:
                    newnode = Node(data)
                    newnode.next = current.next
                    current.next.prev = newnode
                    newnode.prev = current
                    current.next = newnode
                    return
            current = current.next
            i += 1
        print("Index out of range!")
        
    def remove_duplicates(self):
        if self.head is None:
            return
        current = self.head
        seen = {self.head.data}
        while current.next:
            if current.next.data in seen:
                if current.next == self.tail:
                    self.tail = current
                    current.next = None
                else:
                    current.next = current.next.next
                    current.next.prev = current
            else:
                seen.add(current.next.data)
                current = current.next
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " --> ")
            current = current.next
        print("None")
        
    def display_reverse(self):
        current = self.tail
        while current:
            print(current.data, end = " --> ")
            current = current.prev
        print("None")
        
                
dll = DoublyLinkedList()

# dll.insert_at_begin(10)
# dll.insert_at_begin(20)
# dll.insert_at_begin(30)
# dll.insert_at_begin(40)
# dll.insert_at_begin(50)

# dll.insert_at_end(10)
# dll.insert_at_end(20)
# dll.insert_at_end(30)
# dll.insert_at_end(40)
# dll.insert_at_end(50)

dll.convert_arr_to_dll([1, 1, 2, 3, 1, 2, 3])

# dll.delete(4)

# dll.insert_node_before(2, 100)

# dll.insert_node_after(1, 100)

# dll.reverse()

# dll.insert_node_at_index(6, 100)

dll.remove_duplicates()

dll.display()

# dll.display_reverse()
