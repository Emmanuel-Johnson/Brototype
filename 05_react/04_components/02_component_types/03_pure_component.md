# 🧠 What Is a Pure Component in React?

A Pure Component is a component that:

👉 Re-renders only when its props or state actually change

It avoids unnecessary re-renders.

------------------------------------------------------------------------

## 🏛 In Class Components

React provides a special class:

``` jsx
import React from "react";

class MyComponent extends React.PureComponent {
  render() {
    return <h1>{this.props.name}</h1>;
  }
}
```

Instead of:

``` jsx
class MyComponent extends React.Component
```

You use:

``` jsx
extends React.PureComponent
```

------------------------------------------------------------------------

## 🔍 What's the Difference?

**Normal class component:**
Re-renders whenever parent re-renders

**Pure component:**
Re-renders only if props/state change (shallow comparison)

------------------------------------------------------------------------

## ⚡ What is Shallow Comparison?

It checks:

-   Old props vs New props
-   Old state vs New state

If they are the same → ❌ No re-render
If different → ✅ Re-render

But it only checks first level (not deep nested objects).

------------------------------------------------------------------------

## 🧩 Modern React Version (Functional Components)

Since we don't use class components much now...

We use:

``` jsx
React.memo()
```

### Example:

``` jsx
import React from "react";

const ProductCard = ({ name }) => {
  console.log("Rendered");
  return <h2>{name}</h2>;
};

export default React.memo(ProductCard);
```

Now:

-   If `name` doesn't change
-   Component will NOT re-render

This is the functional version of `PureComponent`.

------------------------------------------------------------------------

## 🛒 Real Example (Your E-commerce)

Imagine:

-   Parent component re-renders
-   50 `ProductCard`s exist
-   But product data didn't change

Without `memo` → all 50 re-render 😵
With `React.memo` → only changed ones re-render 😌

That's performance optimization.

------------------------------------------------------------------------

## ⚠️ Important Limitation

`PureComponent` / `React.memo` does shallow comparison.

So this won't work properly:

``` jsx
const obj = { price: 100 };
```

If you recreate object every render → it looks "new"
Even if values are same → it re-renders.

That's why immutability matters in React.

------------------------------------------------------------------------

## 🎯 When Should You Use It?

Use when:

-   Component renders many times
-   Expensive UI
-   Large lists
-   Performance issue exists

Don't use it blindly.

Premature optimization = bad architecture.