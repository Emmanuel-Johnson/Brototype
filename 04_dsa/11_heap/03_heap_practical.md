# MinHeap Implementation in Python

## Overview

This is a **Min Heap** implementation with:

-   Build Heap → `O(n)`
-   Insert → `O(log n)`
-   Remove (Extract Min) → `O(log n)`
-   Peek → `O(1)`
-   Heap Sort → `O(n log n)`

------------------------------------------------------------------------

## Full Implementation

``` python
class MinHeap:
    def __init__(self):
        self.heap = []

    # ===============================
    # 🔨 BUILD HEAP (O(n))
    # ===============================
    def build_heap(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        
        for i in range(n//2 - 1, -1, -1):
            self._heapify_down(i)

    # ===============================
    # 🔼 INSERT (O(log n))
    # ===============================
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            
            if self.heap[index] >= self.heap[parent]:
                break
            
            self.heap[index], self.heap[parent] = (
                self.heap[parent],
                self.heap[index],
            )
            index = parent

    # ===============================
    # 🔽 REMOVE / EXTRACT MIN (O(log n))
    # ===============================
    def remove(self):
        if not self.heap:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        size = len(self.heap)
        
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
                
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            if smallest == index:
                break
            
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            index = smallest

    # ===============================
    # 👀 PEEK (O(1))
    # ===============================
    def peek(self):
        return self.heap[0] if self.heap else None

    # ===============================
    # 🔄 HEAP SORT (O(n log n))
    # ===============================
    def heap_sort(self):
        copied = self.heap[:]
        result = []
        
        while self.heap:
            result.append(self.remove())
        
        self.heap = copied  # restore
        return result

    # ===============================
    # 🖨 DISPLAY
    # ===============================
    def display(self):
        print(self.heap)
```