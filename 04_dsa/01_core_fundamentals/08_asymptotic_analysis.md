# Asymptotic Analysis

Asymptotic analysis describes how an algorithm behaves as the input size (**N**) becomes very large.

> **We don’t care about:**
> - Exact time in seconds
> - Machine speed
> - Small inputs

> **We care only about:**  
> Growth trend

---

## Big-O (O) — Worst Case

**Big-O** describes the maximum time an algorithm can take in the worst situation.

> _Think:_ “What is the slowest this code can ever be?”

**Example:**  
Searching for a number in an unsorted array:

- **Best case:** Number is first
- **Worst case:** Number is last or not present

- Worst case comparisons = **N**
- **Big-O:** `O(N)`

> 📌 Interviewers mostly ask about Big-O.

---

## Big-Ω (Omega) — Best Case

**Big-Ω** describes the minimum time an algorithm can take in the best situation.

> _Think:_ “What is the fastest this code can ever be?”

**Example:**  
Same search:

- If number is found at first position:
    - Comparisons = **1**
    - **Big-Ω:** `Ω(1)`

---

## Big-Θ (Theta) — Average / Tight Bound

**Big-Θ** describes the normal or average performance when best and worst are similar.

> _Think:_ “How does it usually behave?”

**Example:**  
A loop that always runs N times:
```python
for i in range(n):
        print(i)
```
- Best case = **N**
- Worst case = **N**
- **Big-Θ:** `Θ(N)`

---

## Easy Way to Remember 🧠

| Notation | Meaning      | Question it answers           |
|----------|-------------|------------------------------|
| Big-O    | Worst case  | “How bad can it get?”        |
| Big-Ω    | Best case   | “How fast can it be?”        |
| Big-Θ    | Average/exact | “What usually happens?”    |

---

## Interview Shortcut 🚀

If the interviewer doesn’t specify:
> **Always say Big-O first**