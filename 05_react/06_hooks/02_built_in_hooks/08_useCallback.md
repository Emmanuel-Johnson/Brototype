# 🧠 What is useCallback?

`useCallback` returns a memoized version of a function.

It prevents the function from being recreated on every render.

------------------------------------------------------------------------

## 🧩 Syntax

``` js
const memoizedFunction = useCallback(() => {
  // logic
}, [dependencies]);
```

It will recreate the function only when dependencies change.

------------------------------------------------------------------------

## 🔥 Why Do We Need It?

Because in React:

Every render = new function reference.

Example:

``` js
function App() {
  const handleClick = () => {
    console.log("Clicked");
  };

  return <Child onClick={handleClick} />;
}
```

Even if nothing changes,
`handleClick` is recreated every render.

So if `Child` is wrapped in `React.memo`,
it will still re-render ❌

Why?

Because:

    oldFunction !== newFunction

Different reference.

------------------------------------------------------------------------

## ✅ Fix With useCallback

``` js
import { useCallback } from "react";

function App() {
  const handleClick = useCallback(() => {
    console.log("Clicked");
  }, []);

  return <Child onClick={handleClick} />;
}
```

Now the function reference stays stable.

If `Child` is memoized → it won't re-render unnecessarily.

Boom 💥

------------------------------------------------------------------------

## 💡 Practical Example (E-commerce)

``` js
const ProductItem = React.memo(function ProductItem({ product, addToCart }) {
  console.log("Rendered:", product.name);
  return (
    <button onClick={() => addToCart(product)}>
      Add {product.name}
    </button>
  );
});
```

Parent:

``` js
const addToCart = useCallback((product) => {
  dispatch({ type: "ADD_ITEM", payload: product });
}, [dispatch]);
```

Now:

If theme changes →
Parent re-renders →
`ProductItem` will NOT re-render (unless `product` changes).

That's real-world performance optimization.

------------------------------------------------------------------------

## ⚠️ Very Important Rule

Don't use `useCallback` everywhere.

Wrong usage:

``` js
const handleClick = useCallback(() => {
  setCount(count + 1);
}, [count]);
```

Here, the function changes every time `count` changes anyway.

Sometimes a normal function is perfectly fine.

------------------------------------------------------------------------

## 🧠 useCallback vs useMemo

They're actually related:

    useCallback(fn, deps)

is basically:

    useMemo(() => fn, deps)

Difference:

-   `useMemo` → memoizes value
-   `useCallback` → memoizes function

------------------------------------------------------------------------

## 🎯 When You Should Use It

Use `useCallback` when:

-   Passing functions to memoized child components
-   Preventing unnecessary re-renders
-   Working with large lists
-   Optimizing performance-sensitive areas

Don't use it just because "it looks professional" 😅