# React.memo vs useMemo

`React.memo` and `useMemo` are both used for **performance
optimization**, but they work at **different levels** in React.

------------------------------------------------------------------------

# 1️⃣ React.memo

👉 Used to **memoize a component**.

It prevents a component from **re-rendering if its props haven't
changed**.

### Example

``` jsx
import { memo } from "react";

const Child = memo(function Child({ name }) {
  console.log("Child rendered");
  return <h1>{name}</h1>;
});

export default Child;
```

### What happens

If the parent re-renders but the `name` prop stays the same:

👉 **Child will NOT re-render.**

So:

    React.memo → memoize component

------------------------------------------------------------------------

# 2️⃣ useMemo

👉 Used to **memoize a value** (result of a calculation) **inside a
component**.

### Example

``` jsx
import { useMemo } from "react";

function App({ num }) {

  const squared = useMemo(() => {
    console.log("calculating...");
    return num * num;
  }, [num]);

  return <h1>{squared}</h1>;
}
```

### What happens

If `num` doesn't change:

👉 React **reuses the stored value**.

So:

    useMemo → memoize value

------------------------------------------------------------------------

# 3️⃣ Main Difference

  Feature            React.memo                    useMemo
  ------------------ ----------------------------- -----------------------
  What it memoizes   Component                     Value
  Used for           Prevent component re-render   Prevent recalculation
  Where used         Outside component             Inside component

------------------------------------------------------------------------

# 4️⃣ Real Example Together

``` jsx
import { useState, useMemo } from "react";
import { memo } from "react";

const Child = memo(({ value }) => {
  console.log("Child rendered");
  return <h1>{value}</h1>;
});

export default function App() {
  const [count, setCount] = useState(0);

  const squared = useMemo(() => count * count, [count]);

  return (
    <div>
      <Child value={squared} />
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </div>
  );
}
```

### What happens here

-   `useMemo` → prevents recalculating `count * count`
-   `React.memo` → prevents **Child re-render if prop doesn't change**

------------------------------------------------------------------------

# 5️⃣ Easy Way to Remember

    React.memo  → memoize component
    useMemo     → memoize value
    useCallback → memoize function

------------------------------------------------------------------------

# ⚡ Real Performance Combo

A very common optimization pattern:

    React.memo + useCallback

This prevents **child re-renders when passing functions as props**.

------------------------------------------------------------------------

Since you're digging deeper into **React optimization for your Brototype
projects**, understanding how these three work together is very
important:

-   `React.memo`
-   `useMemo`
-   `useCallback`