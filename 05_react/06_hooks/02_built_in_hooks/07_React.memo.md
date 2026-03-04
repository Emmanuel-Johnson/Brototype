# 🧠 What is React.memo?

`React.memo` is a higher-order component that prevents a component from
re-rendering if its props haven't changed.

Think of it like:

> "Hey React... if the props are the same, don't re-render this
> component."

------------------------------------------------------------------------

## 🔥 Why Do We Need It?

Normally, when a parent re-renders → all child components re-render.

Even if their props didn't change.

That's wasted work.

------------------------------------------------------------------------

## 💡 Basic Example (Without React.memo)

``` js
function Child({ name }) {
  console.log("Child rendered");
  return <h2>{name}</h2>;
}

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <Child name="Emmanuel" />
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </div>
  );
}
```

Click button →
Parent re-renders →
Child also re-renders ❌
Even though `name` didn't change.

------------------------------------------------------------------------

## ✅ Now With React.memo

``` js
const Child = React.memo(function Child({ name }) {
  console.log("Child rendered");
  return <h2>{name}</h2>;
});
```

Now:

Click button →
Parent re-renders →
Child does NOT re-render ✅
Because props didn't change.

Boom 💥

------------------------------------------------------------------------

## 🧠 How It Works

`React.memo` does a shallow comparison of props.

If:

    oldProps === newProps

It skips re-render.

------------------------------------------------------------------------

## ⚠️ Very Important: Objects & Functions Problem

This will still re-render:

``` js
<Child user={{ name: "Emmanuel" }} />
```

Why?

Because every render creates a NEW object:

    { name: "Emmanuel" } !== { name: "Emmanuel" }

Different reference → re-render.

------------------------------------------------------------------------

## 🔥 Solution

Use `useMemo` or `useCallback`:

``` js
const user = useMemo(() => ({ name: "Emmanuel" }), []);
```

Now it won't recreate the object.

This is why these hooks are connected.

------------------------------------------------------------------------

## 🛒 Real World Example (E-commerce)

Imagine:

-   `ProductList`
-   `ProductItem` (100+ items)

If parent re-renders,
you don't want 100 items re-rendering unnecessarily.

Wrap `ProductItem`:

``` js
const ProductItem = React.memo(function ProductItem({ product }) {
  return <div>{product.name}</div>;
});
```

Big performance win.

------------------------------------------------------------------------

## 🚫 When NOT To Use React.memo

Don't use it for:

-   Tiny components
-   Components that always change
-   If there's no performance issue

Because it also adds comparison overhead.

------------------------------------------------------------------------

## 🎯 Quick Comparison

  Tool          What it memoizes
  ------------- ------------------
  useMemo       Value
  useCallback   Function
  React.memo    Component

Together they form the performance optimization trio.