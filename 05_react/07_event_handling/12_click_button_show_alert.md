# Click Button → Show Alert in React ⚛️

A common beginner example of event handling is showing an alert when a
button is clicked.
This is done using the **onClick** event handler.

------------------------------------------------------------------------

# Basic Example

``` javascript
function App() {

  function handleClick() {
    alert("Button clicked!");
  }

  return (
    <button onClick={handleClick}>
      Click Me
    </button>
  );
}
```

## What happens

User clicks button
↓
onClick event triggers
↓
handleClick() function runs
↓
Alert appears

------------------------------------------------------------------------

# Using Arrow Function

You can also write it with an arrow function.

``` javascript
function App() {
  return (
    <button onClick={() => alert("Button clicked!")}>
      Click Me
    </button>
  );
}
```

------------------------------------------------------------------------

# Passing Arguments Example

``` javascript
function App() {

  function greet(name) {
    alert("Hello " + name);
  }

  return (
    <button onClick={() => greet("Emmanuel")}>
      Say Hello
    </button>
  );
}
```

Clicking the button will show:

    Hello Emmanuel

------------------------------------------------------------------------

# Simple Flow

Button Click
↓
onClick handler
↓
Function executes
↓
Alert shown

------------------------------------------------------------------------

# Why This Example Is Important

This simple pattern is used for many real actions like:

-   Opening a modal
-   Adding a product to cart
-   Deleting an item
-   Showing notifications
-   Triggering API calls

### Example from real apps

``` jsx
<button onClick={() => addToCart(productId)}>
  Add to Cart
</button>
```

------------------------------------------------------------------------

# ✅ Interview One‑Liner

**In React, we use the `onClick` event handler to run a function when a
button is clicked, such as showing an alert.**