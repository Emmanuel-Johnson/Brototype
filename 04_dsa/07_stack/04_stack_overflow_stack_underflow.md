## Stack Overflow

Stack overflow occurs when you attempt to push an element onto a stack that is already at its maximum capacity.

- Stacks have a fixed size.
- No space left to insert a new element.
- Common in array-based stacks.

**Example:**  
Stack size = 5, already has 5 elements  
`push()` → ❌ *Overflow*

**In recursion:**  
Too many function calls without returning can also cause stack overflow.

---

## Stack Underflow

Stack underflow occurs when you attempt to pop an element from an empty stack.

- Stack has no elements.
- Nothing to remove.

**Example:**  
Stack is empty  
`pop()` → ❌ *Underflow*

---

### 🧠 Memory Trick

- **Overflow:** push when **FULL**
- **Underflow:** pop when **EMPTY**