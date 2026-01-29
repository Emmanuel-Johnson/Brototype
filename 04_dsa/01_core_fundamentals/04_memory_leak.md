# Memory Leak

## 1. WHAT

Memory leak is a situation where a program allocates memory but fails to release it, causing unused memory to remain occupied during execution.

## 2. WHY

It highlights the problem of wasted memory and reduced system performance. Without detecting or preventing memory leaks, applications can slow down, crash, or run out of memory over time.

## 3. WHERE

Memory leaks occur at runtime in the heap memory while the application handles requests, processes data, or keeps objects alive longer than needed.

## 4. HOW

* First, memory is allocated for objects or data.
* Then, references to that memory are unintentionally retained.
* As a result, the memory cannot be freed or reused by the system.

## 5. WHEN

* Memory leaks typically occur in long-running applications like servers or background services.
* They should never be allowed in short-lived or performance-critical programs.

## 6. EXAMPLE

In a web application, storing user session objects in memory but never clearing them after logout can slowly exhaust available memory.

## 7. PROS & CONS

**Pros:** None. Memory leaks are always undesirable.

**Cons:** Reduce performance, increase memory usage, and can eventually cause application failure.

## 8. COMMON MISTAKES

* Not removing unused object references or event listeners.
* Forgetting to close resources like files, database connections, or streams.
