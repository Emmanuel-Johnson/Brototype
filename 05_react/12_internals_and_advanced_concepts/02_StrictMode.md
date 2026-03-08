# React StrictMode

**StrictMode** in React is a development tool that helps developers find
potential problems in their React application.

It **does not affect production**. It only runs in **development mode**.

Think of it like:

🧪 **A testing tool that warns you about unsafe or bad React
practices.**

------------------------------------------------------------------------

## 1️⃣ How StrictMode is used

You wrap your app with **StrictMode**.

``` javascript
import React from "react";
import ReactDOM from "react-dom/client";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
      <App />
  </React.StrictMode>
);
```

Structure:

    StrictMode
       ↓
      App

Now React will check **all components inside `App`**.

------------------------------------------------------------------------

## 2️⃣ What StrictMode does

StrictMode helps detect:

### ✅ Unsafe lifecycle methods

Old lifecycle methods like:

-   `componentWillMount`
-   `componentWillReceiveProps`
-   `componentWillUpdate`

These are **deprecated**, and StrictMode warns you.

------------------------------------------------------------------------

### ✅ Unexpected side effects

StrictMode runs some functions **twice in development**.

Example:

``` javascript
useEffect(() => {
  console.log("Effect running");
}, []);
```

You might see:

    Effect running
    Effect running

This is **intentional**.

React does this to **detect side effects**.

------------------------------------------------------------------------

### ✅ Detects deprecated APIs

Examples:

-   `findDOMNode`
-   Legacy Context API

StrictMode shows warnings when these are used.

------------------------------------------------------------------------

### ✅ Ensures reusable state

StrictMode prepares React apps for **future features** like:

-   Concurrent Rendering

------------------------------------------------------------------------

## 3️⃣ Important thing beginners get confused about

StrictMode **does NOT render UI twice in production.**

Only **development mode** behaves this way.

Production builds run normally.

------------------------------------------------------------------------

## 4️⃣ Example Structure

Without StrictMode:

    <App />

With StrictMode:

    StrictMode
       ↓
      App
       ↓
    All child components checked

------------------------------------------------------------------------

## 5️⃣ Simple Analogy

Think of **StrictMode like a code inspector 👮‍♂️**

Normal Mode: - Code runs

StrictMode: - Code runs - Inspector checks for mistakes - Warnings
appear

------------------------------------------------------------------------

## 6️⃣ One-line Interview Answer

**StrictMode is a React development tool that helps identify unsafe
lifecycle methods, side effects, and deprecated APIs in an
application.**