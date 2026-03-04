# React `useMemo` vs `useCallback`

`useMemo` and `useCallback` are React hooks used for **optimization
(memoization)**.
They help prevent unnecessary recalculations or recreations during
re-renders.

However, they are used for **different purposes**.

------------------------------------------------------------------------

# 1️⃣ useMemo

👉 Used to **memoize a value** (result of a calculation).

React recalculates the value **only when dependencies change**.

### Example

``` jsx
import { useMemo } from "react";

function App({ num }) {

  const squared = useMemo(() => {
    console.log("Calculating...");
    return num * num;
  }, [num]);

  return <h1>{squared}</h1>;
}
```

### What happens

-   If `num` doesn't change, React **uses the stored value**.
-   It **won't recalculate** `num * num`.

✔ Typically used for **expensive calculations**.

------------------------------------------------------------------------

# 2️⃣ useCallback

👉 Used to **memoize a function**.

React recreates the function **only when dependencies change**.

### Example

``` jsx
import { useCallback } from "react";

function App() {

  const handleClick = useCallback(() => {
    console.log("Clicked");
  }, []);

  return <button onClick={handleClick}>Click</button>;
}
```

### What happens

-   React keeps the **same function reference** between renders.
-   Useful when **passing functions to memoized child components**.

------------------------------------------------------------------------

# 3️⃣ Simple Difference

  Hook          Stores     Use case
  ------------- ---------- -----------------------------
  useMemo       Value      Expensive calculations
  useCallback   Function   Prevent function recreation

------------------------------------------------------------------------

# 4️⃣ Easy Way to Remember

    useMemo → memoize VALUE
    useCallback → memoize FUNCTION

------------------------------------------------------------------------

# 5️⃣ Real Example (with React.memo)

``` javascript
const handleClick = useCallback(() => {
  console.log("clicked");
}, []);
```

If `Child` is wrapped with **React.memo**,
`useCallback` prevents **unnecessary child re-renders**.