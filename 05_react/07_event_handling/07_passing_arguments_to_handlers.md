# Passing Arguments to Event Handlers in React ⚛️

Sometimes an event handler needs extra data (like an ID, name, or
value).
In those cases, we pass arguments to the handler using an **arrow
function**.

------------------------------------------------------------------------

# Basic Example

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

## What happens

User clicks button
↓
Arrow function runs
↓
greet("Emmanuel") executes

------------------------------------------------------------------------

# Why We Use an Arrow Function

If you do this:

❌ **Wrong**

``` jsx
<button onClick={greet("Emmanuel")} />
```

### Problem

Component renders
↓
greet() runs immediately
↓
Not waiting for click

So the function executes **during render**, not on click.

------------------------------------------------------------------------

# Correct Way

``` jsx
<button onClick={() => greet("Emmanuel")} />
```

Here the arrow function **delays execution until the click happens**.

------------------------------------------------------------------------

# Passing Event + Arguments

Sometimes you need **both the event object and custom data**.

``` javascript
function handleClick(id, e) {
  console.log("Product ID:", id);
}

<button onClick={(e) => handleClick(10, e)}>
  Click
</button>
```

### Flow

User clicks
↓
Arrow function runs
↓
handleClick(10, e)

------------------------------------------------------------------------

# Real Project Example

Common in **lists or products**.

``` javascript
function deleteProduct(id) {
  console.log("Deleting product", id);
}

<button onClick={() => deleteProduct(5)}>
  Delete
</button>
```

Used for things like:

-   Delete item
-   Add to cart
-   Update product
-   View details

------------------------------------------------------------------------

# Example with Mapping (Very Common)

``` javascript
const products = [
  { id: 1, name: "Laptop" },
  { id: 2, name: "Phone" }
];

function App() {

  const handleClick = (id) => {
    console.log("Product clicked:", id);
  };

  return (
    <div>
      {products.map((p) => (
        <button key={p.id} onClick={() => handleClick(p.id)}>
          {p.name}
        </button>
      ))}
    </div>
  );
}
```

This is **extremely common in real React apps.**

------------------------------------------------------------------------

# Another Method (Using bind)

Less common but possible:

``` jsx
<button onClick={greet.bind(null, "Emmanuel")} />
```

But usually developers prefer **arrow functions**.

------------------------------------------------------------------------

# Simple Rule to Remember

Need to pass arguments?
↓
Use arrow function

Example:

``` jsx
onClick={() => myFunction(argument)}
```

------------------------------------------------------------------------

# 💡 Interview Definition

**Passing arguments to event handlers in React is done using an arrow
function so the handler receives custom values when the event occurs.**