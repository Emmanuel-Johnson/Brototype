# 🧠 useMemo in React

`useMemo` is used to memoize (cache) a calculated value so React doesn't
recompute it on every render.

Think of it like:

> "Hey React, this calculation is expensive.
> Only redo it if these specific values change."

---

## 🔥 Why Do We Need It?

By default, React re-runs everything inside your component on every
render.

Even this:

```js
const expensiveValue = heavyCalculation(data);
```

It runs again every render --- even if `data` didn't change.

That can slow your app.

---

## 🧩 Syntax

```js
const memoizedValue = useMemo(() => {
  return someCalculation;
}, [dependencies]);
```

- First argument → function that returns value
- Second argument → dependency array
- It recalculates only when dependencies change

---

## 💡 Simple Example

```js
import { useState, useMemo } from "react";

function App() {
  const [count, setCount] = useState(0);
  const [number, setNumber] = useState(1000000);

  const expensiveCalculation = useMemo(() => {
    console.log("Calculating...");
    return number * 2;
  }, [number]);

  return (
    <div>
      <h2>{count}</h2>
      <button onClick={() => setCount(count + 1)}>Increase Count</button>

      <p>{expensiveCalculation}</p>
    </div>
  );
}
```

👉 Now when you increase `count`,
it will **NOT** re-run the expensive calculation.

It only runs when `number` changes.

---

## 🚫 When NOT to Use useMemo

Very important.

Don't use it for simple calculations like:

```js
const fullName = useMemo(() => firstName + lastName, [firstName, lastName]);
```

That's unnecessary --- the calculation is cheap.

---

## ✅ useMemo is Useful For:

- Heavy loops
- Filtering large lists
- Sorting big arrays
- Complex computations
- Preventing unnecessary object recreation

---

## 🛒 Real Example (E-commerce Filtering)

```js
const filteredProducts = useMemo(() => {
  return products.filter((product) =>
    product.name.toLowerCase().includes(searchTerm.toLowerCase()),
  );
}, [products, searchTerm]);
```

Now filtering only runs when:

- `products` change
- `searchTerm` changes

Not when some unrelated state updates.

That's huge for performance when the product list is large.

---

## ⚠️ Common Beginner Mistake

Using `useMemo` everywhere thinking:

> "More useMemo = faster app"

Nope ❌

`useMemo` itself has overhead.

Use it only when:

- There is a real performance problem
- Or there is expensive recalculation

---

## 🧠 Difference: useMemo vs useCallback

Quick preview:

- `useMemo` → memoizes **value**
- `useCallback` → memoizes **function**

---

## 🎯 Practical Rule

If your component feels slow →
Profile it → Then add `useMemo`.

Not before.
