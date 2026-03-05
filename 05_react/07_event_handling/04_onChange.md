# onChange in React ⚛️

`onChange` is an event handler that runs whenever the value of an input
element changes.

It is mostly used with:

-   `<input>`
-   `<textarea>`
-   `<select>`

In React, **onChange is very important for handling form data.**

------------------------------------------------------------------------

# Basic Example

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

## Flow

User types in input
↓
onChange triggers
↓
handleChange() runs
↓
e.target.value contains the typed text

------------------------------------------------------------------------

# What is `e.target.value`?

-   `e` → SyntheticEvent object
-   `target` → the HTML element that triggered the event
-   `value` → the current value inside the input

### Example

If user types:

    Hello

Console output:

    H
    He
    Hel
    Hell
    Hello

Because **onChange runs every time the input value changes.**

------------------------------------------------------------------------

# Example with State (Real React Usage)

Most of the time `onChange` is used with **React state**.

``` javascript
import { useState } from "react";

function App() {

  const [name, setName] = useState("");

  const handleChange = (e) => {
    setName(e.target.value);
  };

  return (
    <>
      <input type="text" onChange={handleChange} />
      <p>Hello {name}</p>
    </>
  );
}
```

## What happens here

User types → onChange fires
↓
handleChange runs
↓
setName updates state
↓
Component re-renders
↓
UI updates

This is called a **Controlled Component**.

------------------------------------------------------------------------

# Example with Select

``` javascript
function App() {

  const handleChange = (e) => {
    console.log(e.target.value);
  };

  return (
    <select onChange={handleChange}>
      <option value="React">React</option>
      <option value="Vue">Vue</option>
      <option value="Angular">Angular</option>
    </select>
  );
}
```

When user selects an option → **onChange runs.**

------------------------------------------------------------------------

# Important Difference (React vs HTML)

### In HTML

`change` event → triggers **when input loses focus**

### In React

`onChange` → triggers **on every keystroke**

So React `onChange` behaves more like the native **input event**.

------------------------------------------------------------------------

# Common Use Cases

You will use `onChange` for:

-   Form inputs
-   Search bars
-   Login forms
-   Filtering data
-   Live validation
-   Controlled inputs

### Example

``` jsx
<input
  type="text"
  value={search}
  onChange={(e) => setSearch(e.target.value)}
/>
```

------------------------------------------------------------------------

# 💡 Interview Definition

**onChange is a React event handler that fires whenever the value of an
input element changes and is commonly used to update component state.**