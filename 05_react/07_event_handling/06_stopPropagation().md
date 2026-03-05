# stopPropagation() in React ⚛️

`stopPropagation()` is used to stop an event from bubbling up to parent
elements.

Normally, events in the DOM bubble upward from the child element to its
parent.

Child → Parent → Grandparent

`stopPropagation()` stops this upward flow.

------------------------------------------------------------------------

# Example Without stopPropagation()

``` javascript
function App() {
  return (
    <div onClick={() => console.log("Div clicked")}>
      <button onClick={() => console.log("Button clicked")}>
        Click
      </button>
    </div>
  );
}
```

## When the button is clicked

    Button clicked
    Div clicked

### Why?

Button click
↓
Button handler runs
↓
Event bubbles up
↓
Div handler runs

------------------------------------------------------------------------

# Example With stopPropagation()

``` javascript
function App() {
  return (
    <div onClick={() => console.log("Div clicked")}>
      <button
        onClick={(e) => {
          e.stopPropagation();
          console.log("Button clicked");
        }}
      >
        Click
      </button>
    </div>
  );
}
```

## Output

    Button clicked

Now the event does **not reach the parent div.**

------------------------------------------------------------------------

# Event Flow Visualization

### Normal event flow

    Button
      ↓
    Div
      ↓
    Parent elements

### With stopPropagation()

    Button
      ↓
    Event stops here ❌

------------------------------------------------------------------------

# Real Project Example

Very common in **cards, modals, and dropdowns.**

``` jsx
<div onClick={() => console.log("Open product page")}>
  <button
    onClick={(e) => {
      e.stopPropagation();
      console.log("Add to cart");
    }}
  >
    Add to Cart
  </button>
</div>
```

### Why?

Without `stopPropagation()`

    Add to Cart
    Open product page

With `stopPropagation()`

    Add to Cart

So clicking **Add to Cart** won't open the product page.

------------------------------------------------------------------------

# Difference from preventDefault()

  Method              Purpose
  ------------------- --------------------------------
  preventDefault()    Stops browser default behavior
  stopPropagation()   Stops event bubbling

### Example

-   preventDefault → stop page reload
-   stopPropagation → stop parent events

------------------------------------------------------------------------

# 💡 Interview Definition

**stopPropagation() is a method used to prevent an event from bubbling
up to parent elements in the DOM.**