# Complexity Analysis

## 1. WHAT
Complexity analysis is the method used to measure how an algorithm’s time and memory usage grow as input size increases. It is used to compare algorithms independent of hardware or programming language.

## 2. WHY
It helps predict performance before running code. Without it, choosing efficient solutions becomes trial-and-error, and scaling issues appear only after the system slows down.

## 3. WHERE
It fits at the algorithm design stage, before coding or optimization. In a request–response system, it guides how fast core logic executes under high load.

## 4. HOW
First, identify the input size and key operations. Then count how often those operations run as input grows. Finally, express the growth using Big-O notation.

## 5. WHEN
It should be used while selecting algorithms for large or scalable systems. It should not be overemphasized for very small inputs where readability matters more than performance.

## 6. EXAMPLE
While building a search feature, choosing binary search with `O(log n)` instead of linear search with `O(n)` improves response time as data grows.

## 7. PROS & CONS
It helps compare algorithms objectively and improves scalability decisions. However, it ignores constants and may not reflect real-world performance exactly.

## 8. COMMON MISTAKES
Ignoring worst-case complexity and focusing only on the average case. Another mistake is assuming a lower Big-O always means faster execution in practice.
