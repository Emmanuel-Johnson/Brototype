# 🌳 What is Heapify?

**Heapify = Fix the heap property.**

If a tree violates heap rules, heapify rearranges it so it becomes a
valid heap again.

There are two situations:

-   🔼 Heapify Up (after insert)
-   🔽 Heapify Down (after delete or build heap)

------------------------------------------------------------------------

# 🔼 Heapify Up (Bubble Up)

Used when you insert a new element.

### Idea:

1.  Insert at last position\
2.  Compare with parent\
3.  If wrong order → swap\
4.  Continue upward

### Example (Min Heap)

Insert `5` into:

            10
          /    \
         20     30

After inserting at last:

            10
          /    \
         20     30
        /
       5

5 \< 20 ❌\
Swap.

            10
          /    \
         5      30
        /
       20

5 \< 10 ❌\
Swap again.

            5
          /    \
         10     30
        /
       20

Done ✅

That upward fixing = **Heapify Up**

------------------------------------------------------------------------

# 🔽 Heapify Down (Bubble Down)

Used when: - You delete the root\
- During heap construction

### Example (Min Heap)

Delete root from:

            5
          /   \
         10    15
        /  \
       20  30

### Step 1: Replace root with last element (30)

            30
          /    \
         10     15
        /
       20

Now heap property broken ❌

Compare 30 with children (10, 15)\
Smallest child = 10\
Swap.

            10
          /    \
         30     15
        /
       20

Again compare 30 with 20\
Swap.

            10
          /    \
         20     15
        /
       30

Done ✅

That downward fixing = **Heapify Down**

------------------------------------------------------------------------

# 🧠 Why Heapify is O(log n)?

Because:

-   Maximum swaps = height of tree\
-   Height = log n

So it's very efficient.

------------------------------------------------------------------------

# 🧑‍💻 Python Implementation (Min Heapify Down)

``` python
def heapify_down(arr, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_down(arr, n, smallest)
```

------------------------------------------------------------------------

# 🔥 Build Heap Using Heapify

Very important interview concept.

Instead of inserting one by one (O(n log n))\
We build heap in **O(n)** using bottom-up heapify.

``` python
for i in range(n//2 - 1, -1, -1):
    heapify_down(arr, n, i)
```

This is called **Build Heap**.

------------------------------------------------------------------------

# 🧐 Quick Check

If array is:

    [40, 10, 30, 5]

After full heapify (min heap), what will root be?

👉 **Answer: 5**