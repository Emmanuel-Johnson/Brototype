# Event Bubbling & Capturing in React ⚛️

When an event happens in the DOM, it travels through three phases.

Capturing Phase
↓
Target Phase
↓
Bubbling Phase

Understanding this helps explain how events move through elements.

------------------------------------------------------------------------

# 1️⃣ Event Bubbling

Event bubbling means the event starts from the **target element** and
moves **upward to its parent elements**.

## Example

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

### When the button is clicked

    Button clicked
    Div clicked

### Flow

Button (target)
↓
Div (parent)
↓
Higher parent elements

So the event **bubbles upward**.

------------------------------------------------------------------------

# 2️⃣ Event Capturing

Capturing is the **opposite direction**.

The event travels **from the parent down to the target element**.

    Parent
     ↓
    Child
     ↓
    Target

React supports capturing using **Capture events**.

## Example

``` jsx
<div onClickCapture={() => console.log("Div captured")}>
  <button onClick={() => console.log("Button clicked")}>
    Click
  </button>
</div>
```

### Output

    Div captured
    Button clicked

### Flow

Capturing phase
↓
Target phase
↓
Bubbling phase

------------------------------------------------------------------------

# 3️⃣ Full Event Flow

When you click a button:

1.  Capturing phase (top → down)
2.  Target phase
3.  Bubbling phase (down → up)

### Visualization

    Document
      ↓
    Parent Div
      ↓
    Button  (Target)
      ↑
    Parent Div
      ↑
    Document

------------------------------------------------------------------------

# 4️⃣ Stopping Bubbling

You can stop bubbling using:

    e.stopPropagation()

## Example

``` jsx
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
```

### Output

    Button clicked

The event **does not reach the div**.

------------------------------------------------------------------------

# 5️⃣ Why This Matters in Real Projects

Event bubbling is used in:

-   Dropdown menus
-   Modals
-   Cards with buttons
-   Event delegation

## Example

``` jsx
<div onClick={() => openProduct()}>
  <button
    onClick={(e) => {
      e.stopPropagation();
      addToCart();
    }}
  >
    Add to Cart
  </button>
</div>
```

### Without stopPropagation()

    Add to cart
    Open product

### With stopPropagation()

    Add to cart

------------------------------------------------------------------------

# Quick Comparison

  Concept     Direction
  ----------- -----------------
  Capturing   Parent → Target
  Bubbling    Target → Parent

------------------------------------------------------------------------

# 💡 Interview Definition

**Event bubbling is when an event propagates from the target element to
its parent elements.
Event capturing is when the event travels from parent elements down to
the target element.**