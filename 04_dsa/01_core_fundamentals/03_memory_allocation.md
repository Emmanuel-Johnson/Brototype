# Memory Allocation

## 1. WHAT

Memory allocation is the process of assigning memory space to a program or data, used to store variables and data structures during execution.

## 2. WHY

It solves the problem of managing limited memory efficiently. Without proper allocation, programs can waste memory, crash, or overwrite important data.

## 3. WHERE

Memory allocation happens at runtime inside the system memory, mainly in stack and heap areas, while the application processes requests and executes logic.

## 4. HOW

* First, the program requests memory for required data.
* Then, the system allocates memory from stack or heap.
* Finally, the memory is used and later released or reused.

## 5. WHEN

* It should be used whenever data needs memory during program execution.
* It should not be misused by allocating memory repeatedly without freeing it.

## 6. EXAMPLE

Creating dynamic arrays or objects in a program where the data size is known only at runtime, such as loading user data from a database.

## 7. PROS & CONS

**Pros:** Allows flexible memory usage, supports dynamic data sizes, and improves performance.

**Cons:** Poor memory management can cause memory leaks and increase overhead.

## 8. COMMON MISTAKES

* Forgetting to free allocated memory in manual memory management languages.
* Allocating more memory than required.
