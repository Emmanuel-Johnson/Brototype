# Time Complexity

## 1. WHAT
Time complexity is a way to measure how an algorithm’s execution time grows with input size. It is used to estimate performance without running the code.

## 2. WHY
It helps choose faster algorithms and avoid slow code at scale. Without it, performance issues appear late and debugging becomes repetitive and costly.

## 3. WHERE
It fits during algorithm design and code review stages. In a request–response system, it impacts how quickly the backend handles increasing user requests.

## 4. HOW
First, identify the input size and core operations. Then count how often those operations run as input grows. Finally, express the growth using Big-O notation.

## 5. WHEN
It should be used when building scalable features or handling large data. It should not be overfocused for very small inputs or one-time scripts.

## 6. EXAMPLE
In an LMS project, using binary search `O(log n)` to find a student record is faster than linear search `O(n)` as users increase.

## 7. PROS & CONS
It enables objective performance comparison and better scalability decisions. However, it ignores constant factors and hardware-level optimizations.

## 8. COMMON MISTAKES
Confusing time complexity with actual execution time. Another mistake is ignoring worst-case complexity during interviews or system design.

<br>
<br>
<br>

# Space Complexity

## 1. WHAT
Space complexity is a measure of how much extra memory an algorithm uses as input size grows. It is used to evaluate memory efficiency independent of execution time.

## 2. WHY
It helps prevent memory overuse and crashes in large systems. Without it, programs may work for small data but fail or slow down when data scales.

## 3. WHERE
It fits during algorithm design and system optimization phases. In a request–response flow, it affects how much memory each request consumes on the server.

## 4. HOW
First, identify all extra memory used by the algorithm. Then relate that memory usage to input size. Finally, express the growth using Big-O notation.

## 5. WHEN
It should be used when working with large data, limited RAM, or concurrent users. It should not be over-prioritized when memory is abundant and speed is the main goal.

## 6. EXAMPLE
In an LMS project, storing all student records in memory uses `O(n)` space, while processing records one by one uses `O(1)` extra space.

## 7. PROS & CONS
It helps build memory-efficient and stable applications and supports better scalability decisions. However, optimizing for space can increase code complexity or execution time.

## 8. COMMON MISTAKES
Ignoring recursion stack space in analysis. Another mistake is confusing input storage with extra auxiliary space.
