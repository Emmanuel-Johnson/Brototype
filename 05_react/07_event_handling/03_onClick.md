# onClick in React ⚛️

`onClick` is an event handler in React that runs a function when a user
clicks an element (like a button, div, image, etc.).

It is one of the most commonly used events in React applications.

------------------------------------------------------------------------

# Basic Example

``` javascript
function App() {

  function handleClick() {
    alert("Button clicked");
  }

  return (
    <button onClick={handleClick}>
      Click Me
    </button>
  );
}
```

## Flow

User clicks button
↓
onClick triggers
↓
handleClick() function runs

------------------------------------------------------------------------

# Using Arrow Function

Sometimes you want to run a function with arguments.

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

Here the arrow function allows us to pass parameters.

------------------------------------------------------------------------

# Accessing the Event Object

React automatically passes a **SyntheticEvent** object.

``` javascript
function handleClick(event) {
  console.log(event.target);
}

<button onClick={handleClick}>
  Click
</button>
```

Example output:

    <button>Click</button>

`event.target` → element that triggered the event.

------------------------------------------------------------------------

# Multiple Actions in onClick

You can run multiple statements.

``` jsx
<button
  onClick={() => {
    console.log("Clicked");
    alert("Hello");
  }}
>
  Click
</button>
```

------------------------------------------------------------------------

# Preventing Event Bubbling

``` javascript
function handleClick(e) {
  e.stopPropagation();
}
```

Example:

``` jsx
<div onClick={() => console.log("Div clicked")}>
  <button onClick={(e) => {
    e.stopPropagation();
    console.log("Button clicked");
  }}>
    Click
  </button>
</div>
```

Output:

    Button clicked

The div event won't run because bubbling was stopped.

------------------------------------------------------------------------

# onClick Works on Many Elements

Not only buttons.

``` jsx
<div onClick={() => console.log("Div clicked")}>
  Click this div
</div>
```

------------------------------------------------------------------------

# Important Rule

In React event names use **camelCase**.

Correct:

    onClick
    onChange
    onSubmit

Wrong:

    onclick
    onchange

------------------------------------------------------------------------

# Real Project Examples

You will use `onClick` for things like:

-   Opening a modal
-   Adding item to cart
-   Deleting a product
-   Navigating pages
-   Toggling UI elements

Example:

``` jsx
<button onClick={() => setIsOpen(true)}>
  Open Modal
</button>
```

------------------------------------------------------------------------

# 💡 Interview Definition

**onClick is a React event handler that executes a function when an
element is clicked.**