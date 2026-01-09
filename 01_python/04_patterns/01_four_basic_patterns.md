Below is a Python script that prints four basic star patterns using nested loops.

```python
for i in range(1, 6):
    for j in range(1, 6):
        if j <= i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

print()

for i in range(1, 6):
    for j in range(1, 6):
        if j >= 6 - i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
    
print()

for i in range(1, 6):
    for j in range(1, 6):
        if j <= 6 - i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
    
print()
    
for i in range(1, 6):
    for j in range(1, 6):
        if j >= i:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
```