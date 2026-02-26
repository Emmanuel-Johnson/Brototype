# 🧠 What Are Higher Order Components (HOC)?

A Higher Order Component (HOC) is:

👉 A function that takes a component and returns a new component.

It's just a pattern.

Not a special React feature.
Just JavaScript + components.

------------------------------------------------------------------------

## 🧩 Simple Definition

``` jsx
const EnhancedComponent = higherOrderFunction(OriginalComponent);
```

It wraps a component and adds extra behavior.

------------------------------------------------------------------------

## 🔥 Basic Example

Imagine you want to add a loading spinner to multiple components.

Instead of repeating logic everywhere...
You create an HOC.

``` jsx
const withLoading = (WrappedComponent) => {
  return function EnhancedComponent({ isLoading, ...props }) {
    if (isLoading) {
      return <p>Loading...</p>;
    }

    return <WrappedComponent {...props} />;
  };
};
```

Now use it:

``` jsx
const ProductListWithLoading = withLoading(ProductList);
```

Boom 💥
You just added loading logic without touching `ProductList`.

That's HOC power.

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

### 🛒 E-commerce

You might want:

-   Authentication check
-   Admin access control
-   Loading wrapper
-   Error boundary wrapper

Instead of repeating code in:

-   `ProductPage`
-   `CartPage`
-   `OrderPage`

You wrap them with an HOC.

------------------------------------------------------------------------

## 🔐 Classic Example: Authentication HOC

``` jsx
const withAuth = (WrappedComponent) => {
  return function(props) {
    const isLoggedIn = true; // example

    if (!isLoggedIn) {
      return <p>Please login</p>;
    }

    return <WrappedComponent {...props} />;
  };
};
```

Use it:

``` jsx
export default withAuth(Dashboard);
```

Now `Dashboard` is protected.

Clean. Reusable. Professional.

------------------------------------------------------------------------

## ⚡ Why Use HOC?

-   Reuse logic
-   Avoid duplication
-   Separate concerns
-   Cleaner architecture

It's like wrapping a gift 🎁
The gift stays the same, wrapping adds an extra layer.

------------------------------------------------------------------------

## 🆚 Modern React Reality

Today, HOCs are less common because:

-   We use custom hooks
-   Hooks are cleaner for logic reuse

But HOCs are still important because:

-   Older projects use them
-   Libraries use them (e.g., Redux used to use `connect()` HOC)