# 🌳 Binary Heap -- Full Time & Space Complexity

------------------------------------------------------------------------

## 1️⃣ Insert (uses Heapify Up)

**Steps:** - Add element at end - Bubble up

  Case      Time
  --------- ----------
  Best      O(1)
  Average   O(log n)
  Worst     O(log n)

**Why?**\
Element may travel from leaf → root\
Height of heap = log n

**Space:** O(1)

------------------------------------------------------------------------

## 2️⃣ Remove (Extract Min/Max) (uses Heapify Down)

**Steps:** - Replace root with last element - Bubble down

  Case      Time
  --------- ----------
  Best      O(1)
  Average   O(log n)
  Worst     O(log n)

**Why?**\
Element may travel from root → leaf\
Max distance = height = log n

**Space:** O(1)

------------------------------------------------------------------------

## 3️⃣ Peek

  Case      Time
  --------- ------
  Best      O(1)
  Average   O(1)
  Worst     O(1)

Just return index 0.

**Space:** O(1)

------------------------------------------------------------------------

## 4️⃣ Heapify (Single Call)

### Heapify Up

### Heapify Down

  Case      Time
  --------- ----------
  Best      O(1)
  Average   O(log n)
  Worst     O(log n)

**Space:** - Iterative → O(1)\
- Recursive → O(log n)

------------------------------------------------------------------------

## 5️⃣ Build Heap (Bottom-Up)

``` python
for i in range(n//2 - 1, -1, -1):
    heapify_down(i)
```

  Case      Time
  --------- ------
  Best      O(n)
  Average   O(n)
  Worst     O(n)

**Important:**\
Even though heapify is O(log n),\
Build heap total = **O(n)** (not O(n log n))

**Space:** O(1)

------------------------------------------------------------------------

## 6️⃣ Heap Sort

**Steps:** - Build heap → O(n)\
- Extract n times → n × log n

  Case      Time
  --------- ------------
  Best      O(n log n)
  Average   O(n log n)
  Worst     O(n log n)

Heap sort does not get faster on sorted data.

**Space:** O(1) (in-place)

------------------------------------------------------------------------

# 🧠 Final Interview Table

  Operation    Best         Average      Worst        Space
  ------------ ------------ ------------ ------------ -------
  Insert       O(1)         O(log n)     O(log n)     O(1)
  Remove       O(1)         O(log n)     O(log n)     O(1)
  Peek         O(1)         O(1)         O(1)         O(1)
  Heapify      O(1)         O(log n)     O(log n)     O(1)
  Build Heap   O(n)         O(n)         O(n)         O(1)
  Heap Sort    O(n log n)   O(n log n)   O(n log n)   O(1)

------------------------------------------------------------------------

# 🔥 Key Takeaways

-   Height of heap = log n\
-   Heapify = O(log n)\
-   Insert = O(log n)\
-   Remove = O(log n)\
-   Build heap = O(n)\
-   Heap sort = O(n log n)