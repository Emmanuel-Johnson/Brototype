# Event Handlers in React ⚛️

Event handlers in React are functions that run when a user interacts
with the UI --- like clicking a button, typing in an input, submitting a
form, etc.

Think of them as **"what should happen when something happens."**

## Example interactions

- Click
- Typing
- Hover
- Submit form
- Focus / Blur

---

# 1️⃣ Basic Event Handler

In React we pass a **function reference** to an event.

```javascript
function App() {
  function handleClick() {
    alert("Button clicked!");
  }

  return <button onClick={handleClick}>Click Me</button>;
}
```

### ⚡ Flow

User Clicks Button
↓
onClick fires
↓
handleClick() runs

### Important

❌ Wrong

```jsx
<button onClick={handleClick()}>
```

This executes **immediately during render.**

✅ Correct

```jsx
<button onClick={handleClick}>
```

---

# 2️⃣ Using Arrow Function in Event

Sometimes you need to **pass arguments**.

```javascript
function App() {
  function greet(name) {
    alert("Hello " + name);
  }

  return <button onClick={() => greet("Emmanuel")}>Say Hello</button>;
}
```

---

# 3️⃣ Event Object (Synthetic Event)

React wraps browser events inside something called **SyntheticEvent**.

It works the **same across all browsers.**

Example:

```javascript
function handleClick(event) {
  console.log(event);
}

<button onClick={handleClick}>Click</button>;
```

You can access things like:

- event.target
- event.preventDefault()
- event.stopPropagation()

---

# 4️⃣ Handling Input Change

Very common in **React forms.**

```javascript
function App() {
  const handleChange = (e) => {
    console.log(e.target.value);
  };

  return <input type="text" onChange={handleChange} />;
}
```

Every time the user types → **onChange triggers**

---

# 5️⃣ Prevent Default Behavior

Used in **forms**.

```javascript
function handleSubmit(e) {
  e.preventDefault();
  console.log("Form submitted");
}

<form onSubmit={handleSubmit}>
  <button type="submit">Submit</button>
</form>;
```

This **prevents page reload.**

---

# 6️⃣ Event Bubbling

Events **propagate upward** in the DOM tree.

```jsx
<div onClick={() => console.log("DIV clicked")}>
  <button onClick={() => console.log("BUTTON clicked")}>Click</button>
</div>
```

### Output

BUTTON clicked
DIV clicked

Because the event **bubbles up.**

---

# 7️⃣ Stop Propagation

To stop bubbling:

```javascript
function handleClick(e) {
  e.stopPropagation();
}
```

---

# 8️⃣ Event Capturing

React also supports **capturing phase**.

```jsx
<div onClickCapture={() => console.log("Captured")}>
```

### Flow

Capturing phase
↓
Target
↓
Bubbling phase

---

# 9️⃣ Debouncing Events

Used to **limit how often an event fires.**

Example: **Search input**

Without debounce → API call every keypress
With debounce → wait **500ms**

Example with **lodash**

```javascript
import debounce from "lodash.debounce";

const handleSearch = debounce((value) => {
  console.log(value);
}, 500);
```

---

# 🔟 Common React Events

Event Usage

---

onClick Button click
onChange Input change
onSubmit Form submit
onMouseEnter Hover
onMouseLeave Hover leave
onFocus Input focus
onBlur Input blur
onKeyDown Key press

---

# 🧠 Important Interview Concepts

For **React interviews / real projects remember:**

- Event Handlers
- Synthetic Events
- Event Bubbling
- Event Capturing
- Prevent Default
- Stop Propagation
- Debouncing
- Controlled Inputs

---

# ⚡ One Important Thing Many Beginners Miss

React events are **camelCase.**

❌ HTML

    onclick
    onchange

✅ React

    onClick
    onChange

---

# 🚀 Advanced Concept

React uses **event delegation**.

Instead of attaching event listeners to every element, React attaches
most events to the **root container** and handles them internally for
better performance.
