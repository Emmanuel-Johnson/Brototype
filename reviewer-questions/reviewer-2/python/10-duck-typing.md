- Duck typing means Python checks an object by its behavior, not its type.
- If an object has the required methods or properties, it can be used.
- Example: if it has a run() method, Python treats it like something that can run.


```python
class Car:
    def run(self):
        print("Car is running")

class Dog:
    def run(self):
        print("Dog is running")

def start(obj):
    obj.run()   # Python only checks if run() exists

c = Car()
d = Dog()

start(c)
start(d)
```

Output:

```python
Car is running
Dog is running
```

Here, both Car and Dog work because they both have a run() method. Python cares about the behavior, not the object type.