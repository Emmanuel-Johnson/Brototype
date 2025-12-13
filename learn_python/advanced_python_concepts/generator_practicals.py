# ✅ Method 1: Create a generator to count upto n

def my_generator(n):
    while n <= 10:
        yield n
        n += 1

gen = my_generator(1)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



# ✅ Method 2: Create a generator to count upto n

n = 10
gen = (i for i in range(1, n + 1))
for _ in range(n):
    print(next(gen))



# ✅ Generator for infinite Fibonacci series

def fibonaaci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonaaci()

for _ in range(10):
    print(next(gen))
