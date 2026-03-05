# Synthetic Events in React ⚛️

In React, **SyntheticEvent** is a wrapper around the native browser
event.

React creates this wrapper so that events work the same way in **all
browsers**.

Different browsers sometimes implement events slightly differently.
React solves this by providing a **consistent event system**.

So when you handle an event in React, you're actually receiving a
**SyntheticEvent object**, not the raw browser event.

------------------------------------------------------------------------

# Basic Example

``` javascript
function handleClick(event) {
  console.log(event);
}

function App() {
  return (
    <button onClick={handleClick}>
      Click Me
    </button>
  );
}
```

### When the button is clicked

User clicks button
↓
React creates SyntheticEvent
↓
handleClick(event) receives it

------------------------------------------------------------------------

# Accessing Event Properties

SyntheticEvent provides many useful properties.

``` javascript
function handleClick(event) {
  console.log(event.target);
}
```

Example output:

    <button>Click Me</button>

### Common Properties

  Property                  Meaning
  ------------------------- -------------------------------------
  event.target              Element that triggered the event
  event.type                Type of event (click, change, etc.)
  event.preventDefault()    Prevent default browser behavior
  event.stopPropagation()   Stop event bubbling

------------------------------------------------------------------------

# Example with Input

``` javascript
function App() {

  const handleChange = (e) => {
    console.log(e.target.value);
  };

  return (
    <input type="text" onChange={handleChange} />
  );
}
```

### When the user types

onChange event
↓
SyntheticEvent created
↓
e.target.value gives input text

------------------------------------------------------------------------

# SyntheticEvent vs Native Browser Event

  SyntheticEvent             Native Event
  -------------------------- ---------------------------
  Provided by React          Provided by browser
  Cross-browser compatible   Behavior may vary
  Consistent API             Different implementations
  Better performance         Direct DOM event

------------------------------------------------------------------------

# Access Native Event (if needed)

Sometimes you may want the **actual browser event**.

``` javascript
function handleClick(e) {
  console.log(e.nativeEvent);
}
```

`nativeEvent` → original browser event.

------------------------------------------------------------------------

# One Important Thing

Earlier versions of React used **event pooling**.

After the event handler finished, the event object was reused, so you
couldn't access it asynchronously.

### Example problem (old React)

``` javascript
function handleClick(e) {
  setTimeout(() => {
    console.log(e.target); // null in old React
  }, 1000);
}
```

But **React 17+ removed event pooling**, so this problem no longer
exists.

------------------------------------------------------------------------

# Simple Way to Remember

Browser Event
↓
React wraps it
↓
SyntheticEvent
↓
Your Event Handler

------------------------------------------------------------------------

# Real Example Used in Projects

``` javascript
function handleSubmit(e) {
  e.preventDefault();
  console.log("Form submitted");
}
```

Here:

-   `e` → SyntheticEvent
-   `preventDefault()` → stops page reload

------------------------------------------------------------------------

# 💡 Quick Interview Answer

**SyntheticEvent is a cross-browser wrapper around the native DOM event
in React that provides a consistent API for handling events.**