# Common Form & Keyboard Events in React ⚛️

React provides several events to handle user input in forms and keyboard
interactions.
These events help capture typing, form submission, focus changes, and
key presses.

------------------------------------------------------------------------

# 1️⃣ onChange

Runs whenever the value of an input changes.

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

### Flow

User types
↓
onChange fires
↓
e.target.value contains input text

### Used for

-   Search bars
-   Login forms
-   Controlled inputs

------------------------------------------------------------------------

# 2️⃣ onSubmit

Used when a form is submitted.

``` javascript
function handleSubmit(e) {
  e.preventDefault();
  console.log("Form submitted");
}

<form onSubmit={handleSubmit}>
  <button type="submit">Submit</button>
</form>
```

### Why `preventDefault()`?

Without it → page reload
With it → React handles form

------------------------------------------------------------------------

# 3️⃣ onFocus

Runs when an input gets focus.

``` jsx
<input
  type="text"
  onFocus={() => console.log("Input focused")}
/>
```

### Example uses

-   Highlight input field
-   Show suggestions

------------------------------------------------------------------------

# 4️⃣ onBlur

Runs when the input loses focus.

``` jsx
<input
  type="text"
  onBlur={() => console.log("Input lost focus")}
/>
```

### Used for

-   Validation
-   Hiding dropdown suggestions

### Example

Click input → focus
Click outside → blur

------------------------------------------------------------------------

# 5️⃣ onKeyDown

Runs when any key is pressed down.

``` jsx
<input
  type="text"
  onKeyDown={(e) => console.log(e.key)}
/>
```

### Example output

    a
    Enter
    Backspace
    ArrowUp

### Common uses

-   Detect Enter key
-   Keyboard shortcuts

### Example

``` javascript
function handleKeyDown(e) {
  if (e.key === "Enter") {
    console.log("Search triggered");
  }
}
```

------------------------------------------------------------------------

# 6️⃣ onKeyUp

Runs when a key is released.

``` jsx
<input
  type="text"
  onKeyUp={(e) => console.log("Key released")}
/>
```

### Flow

Key pressed → onKeyDown
Key released → onKeyUp

------------------------------------------------------------------------

# 7️⃣ onKeyPress (Deprecated)

Older React versions used this event.

Now developers use:

-   onKeyDown
-   onKeyUp

------------------------------------------------------------------------

# Summary Table

  Event       When it fires
  ----------- ---------------------
  onChange    Input value changes
  onSubmit    Form submitted
  onFocus     Element gets focus
  onBlur      Element loses focus
  onKeyDown   Key pressed
  onKeyUp     Key released

------------------------------------------------------------------------

# 💡 Real React App Examples

These events are used in:

-   Login forms
-   Search bars
-   Chat inputs
-   Form validation
-   Keyboard shortcuts

### Example

``` jsx
<input
  value={search}
  onChange={(e) => setSearch(e.target.value)}
  onKeyDown={(e) => e.key === "Enter" && searchProducts()}
/>
```