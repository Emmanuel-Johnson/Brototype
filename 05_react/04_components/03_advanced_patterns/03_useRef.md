# 🧠 What is useRef?

`useRef` is a React Hook that lets you:

-   Access DOM elements directly
-   Store a value that does NOT cause re-render when changed

That second point is VERY important.

------------------------------------------------------------------------

## 🧱 1️⃣ Accessing DOM Elements (Most Common Use)

Example: Focus input automatically.

``` jsx
import { useRef, useEffect } from "react";

const Login = () => {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return <input ref={inputRef} />;
};
```

### What's happening?

-   `useRef()` creates a ref object
-   We attach it to input using `ref`
-   `inputRef.current` gives real DOM element
-   We can call `.focus()`

This is useful in:

-   Login forms (LMS)
-   Search bars (E-commerce)
-   Modals
-   Auto-scroll

------------------------------------------------------------------------

## 🧠 2️⃣ Storing Value Without Re-render

``` jsx
import { useRef } from "react";

const Counter = () => {
  const countRef = useRef(0);

  const increase = () => {
    countRef.current += 1;
    console.log(countRef.current);
  };

  return <button onClick={increase}>Click</button>;
};
```

Here:

-   Value updates
-   But component does NOT re-render

Unlike `useState`.

------------------------------------------------------------------------

## ⚡ useRef vs useState

  useState             useRef
  -------------------- ----------------------------------
  Causes re-render     Does NOT re-render
  Used for UI state    Used for DOM or persistent value
  Triggers UI update   Silent storage

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

### 🛒 E-commerce

-   Focus search bar automatically
-   Scroll to top after checkout
-   Store previous cart count

### 🎓 LMS

-   Track video progress timer
-   Store interval ID
-   Prevent re-render performance issues

------------------------------------------------------------------------

## 🔥 Important Concept

`useRef()` returns:

``` js
{ current: value }
```

And that object stays the SAME between renders.

That's why it doesn't trigger re-render.