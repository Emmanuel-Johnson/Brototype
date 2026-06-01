- @staticmethod is a method inside a class that does not use self or cls.
- It works like a normal function but is grouped inside the class for better organization.
- It can be called using the class name without creating an object.


```python
class Math:
    
    @staticmethod
    def add(a, b):
        return a + b

# Calling staticmethod using class name
result = Math.add(10, 5)

print(result)
```

Output:

```python
15
```