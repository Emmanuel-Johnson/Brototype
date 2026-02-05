## Sort a Stack Using a Temporary Stack

The following Python function sorts a stack (represented as a list) using an additional temporary stack:

```python
def sort_stack(stack):
    temp_stack = []
    while stack:
        current = stack.pop()
        
        while temp_stack and temp_stack[-1] > current:
            stack.append(temp_stack.pop())
            
        temp_stack.append(current)
    
    return temp_stack

print(sort_stack([3, 1, 4, 2]))
```

**Output:**
```
[1, 2, 3, 4]
```