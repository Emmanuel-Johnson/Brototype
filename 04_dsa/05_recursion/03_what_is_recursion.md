# What is Recursion?

Recursion is a programming technique where a function calls itself to solve a problem by breaking it into smaller subproblems of the same type.

> **Think:** “Solve a big problem by solving smaller versions of it.”

## Example (Concept)

To find factorial of 5:

```
5! = 5 × 4!
4! = 4 × 3!
...
until 1!
```

---

## Recursive Function Structure

### 1️⃣ Base Case
- The stopping condition
- Prevents infinite recursion
- Returns a direct result

```python
if condition:
    return value
```

### 2️⃣ Recursive Case
- The function calls itself
- Moves the problem closer to the base case

```python
return function(smaller_input)
```

### 3️⃣ Progress Toward Base Case
- Each call must reduce the problem size
- Otherwise → infinite recursion ❌

**Generic Template:**
```python
def recursive_function(input):
    # 1. Base case
    if base_condition:
        return base_value

    # 2. Recursive case
    return recursive_function(smaller_input)
```

---

## Base Case in Recursion

The base case is the condition where the function stops calling itself.

**Why is it important?**
- Prevents infinite recursion
- Defines the simplest possible problem
- Acts like the “exit door” 🚪

**Example:**
```python
def factorial(n):
    if n == 1:      # base case
        return 1
    return n * factorial(n - 1)
```

> If you forget the base case → ❌ stack overflow error.

---

## Recursive vs Iterative Approach

### 🔁 Recursive Approach
- Uses function calls
- Elegant & closer to mathematical logic
- Uses more memory (call stack)
- Slower due to function overhead

**Examples:** factorial, tree traversal, DFS

### 🔄 Iterative Approach
- Uses loops (`for`, `while`)
- Faster
- Memory efficient
- Code may be longer or less intuitive

**Examples:** linear search, array traversal

---

## 📊 Quick Comparison Table

| Aspect      | Recursion         | Iteration         |
|-------------|-------------------|-------------------|
| Uses        | Function calls    | Loops             |
| Memory      | More (stack)      | Less              |
| Speed       | Slower            | Faster            |
| Readability | High (some cases) | Medium            |
| Risk        | Stack overflow    | Infinite loop     |

---

## 🧠 Interview Tip (IMPORTANT)

If asked “Which is better?”, say:

> **Recursion is better when the problem is naturally recursive (trees, graphs).  
> Iteration is preferred when performance and memory are critical.**