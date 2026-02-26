# 🧠 What is forwardRef?

Normally:

-   `ref` works on DOM elements (`<input />`, `<div />`)
-   ❌ It does NOT automatically work on custom components

Example:

``` jsx
<MyInput ref={inputRef} />
```

This won't work by default.

Why?

Because `ref` does not pass through custom components.

That's where `forwardRef` comes in.

------------------------------------------------------------------------

## 🚀 What Does forwardRef Do?

It allows a parent component to send a `ref` to a child's DOM element.

In simple words:

👉 It forwards the ref from parent → to child's DOM element.

------------------------------------------------------------------------

## ❌ Without forwardRef (This Fails)

``` jsx
const MyInput = () => {
  return <input />;
};

<MyInput ref={inputRef} />  // ❌
```

React will complain.

------------------------------------------------------------------------

## ✅ With forwardRef (Correct Way)

``` jsx
import React, { forwardRef } from "react";

const MyInput = forwardRef((props, ref) => {
  return <input ref={ref} {...props} />;
});
```

Now you can do:

``` jsx
const inputRef = useRef();

<MyInput ref={inputRef} />
```

Now `inputRef.current` points to the actual `<input>`.

Magic unlocked 🔓

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

Imagine in your LMS:

You create a reusable `<Input />` component.

Later, on the Login page, you want:

-   Auto focus
-   Scroll into view
-   Validation focus

If you don't use `forwardRef`, you can't control it from parent.

But with `forwardRef` → full control.

Same in E-commerce:

-   Search bar focus
-   Coupon input focus
-   Checkout field focus

------------------------------------------------------------------------

## 🧠 Why Is This Important?

Because in real-world apps:

-   You build reusable components
-   But sometimes parent needs DOM access

`forwardRef` bridges that gap.

------------------------------------------------------------------------

## ⚡ Modern Note

Often used together with:

-   `useRef`
-   `useImperativeHandle` (even more advanced control)

<br>
<br>
<br>

# 🚀 forwardRef -- Full Working Example

## 🎯 Goal

-   Parent clicks a button
-   It focuses an input inside a child component

Without `forwardRef`, this will NOT work.
With `forwardRef`, it works perfectly.

------------------------------------------------------------------------

## ✅ Example Using forwardRef (Full Working Code)

### 🔹 App.js

``` jsx
import React, { useRef } from "react";
import CustomInput from "./CustomInput";

function App() {
  const inputRef = useRef();

  const handleFocus = () => {
    inputRef.current.focus();
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>forwardRef Example</h2>

      <CustomInput ref={inputRef} />

      <br /><br />

      <button onClick={handleFocus}>
        Focus the input
      </button>
    </div>
  );
}

export default App;
```

------------------------------------------------------------------------

### 🔹 CustomInput.js

``` jsx
import React, { forwardRef } from "react";

const CustomInput = forwardRef((props, ref) => {
  return (
    <input
      ref={ref}
      type="text"
      placeholder="Click button to focus me"
    />
  );
});

export default CustomInput;
```

------------------------------------------------------------------------

## 🧠 What's Happening Here?

### Step 1

Parent creates a ref:

``` jsx
const inputRef = useRef();
```

### Step 2

Parent passes it:

``` jsx
<CustomInput ref={inputRef} />
```

### Step 3

Child receives it because of `forwardRef`:

``` jsx
const CustomInput = forwardRef((props, ref) => {
```

### Step 4

Child attaches it to actual DOM:

``` jsx
<input ref={ref} />
```

### Step 5

Parent can now control that DOM element:

``` jsx
inputRef.current.focus();
```

Boom 💥 input gets focused.

------------------------------------------------------------------------

## ❌ What Happens Without forwardRef?

If you remove `forwardRef` and write:

``` jsx
const CustomInput = () => {
  return <input />;
};
```

React will throw error:

> Function components cannot be given refs

Because functional components don't accept refs by default.