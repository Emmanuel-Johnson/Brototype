# 🧠 What is useRef?

`useRef` lets you:

- 1️⃣ Access DOM elements directly
- 2️⃣ Store a value that does NOT cause re-render

That second point is very important.

------------------------------------------------------------------------

## 📦 Basic Syntax

``` js
const myRef = useRef(initialValue);
```

It returns an object:

``` js
{
  current: initialValue
}
```

You access the value like:

``` js
myRef.current
```

------------------------------------------------------------------------

# 🟢 1️⃣ Using useRef for DOM Access (Most Common)

## Example: Auto Focus Input

``` js
import { useRef, useEffect } from "react";

function Login() {
  const inputRef = useRef(null);

  useEffect(() => {
    inputRef.current.focus();
  }, []);

  return <input ref={inputRef} />;
}
```

### What happens?

- 1️⃣ JSX renders
- 2️⃣ Input mounts
- 3️⃣ `useEffect` runs
- 4️⃣ `inputRef.current` points to actual DOM input
- 5️⃣ `.focus()` runs

Boom 💥 input auto-focused.

------------------------------------------------------------------------

# 🟡 2️⃣ Storing Values Without Re-render

This is the advanced power.

``` js
import { useRef } from "react";

function Counter() {
  const countRef = useRef(0);

  const increase = () => {
    countRef.current += 1;
    console.log(countRef.current);
  };

  return <button onClick={increase}>Increase</button>;
}
```

Notice:

👉 Clicking button does NOT re-render component
👉 Because changing `ref.current` does NOT trigger re-render

Unlike `useState`.

------------------------------------------------------------------------

# 🔥 useRef vs useState (Very Important)

| Feature                  | useState | useRef |
| ------------------------ | -------- | ------ |
| Causes re-render?        | ✅ Yes    | ❌ No   |
| Used for UI display?     | ✅ Yes    | ❌ No   |
| Stores persistent value? | ✅ Yes    | ✅ Yes  |

------------------------------------------------------------------------

# 🧠 When Should You Use useRef?

- ✅ Access DOM elements
- ✅ Store previous value
- ✅ Store timers
- ✅ Store mutable values that shouldn't re-render

------------------------------------------------------------------------

# 🔥 Real Example (Timer Storage)

``` js
import { useRef, useEffect } from "react";

function Timer() {
  const intervalRef = useRef(null);

  useEffect(() => {
    intervalRef.current = setInterval(() => {
      console.log("Running...");
    }, 1000);

    return () => {
      clearInterval(intervalRef.current);
    };
  }, []);

  return <h1>Timer</h1>;
}
```

Here we store interval ID in ref.

Why not state?

Because interval ID does not need UI update.

------------------------------------------------------------------------

# 🧠 Mental Model

Think of `useRef` like:

> A secret box that React does NOT watch for changes.

It persists between renders.
But React doesn't care if you change it.

<br>
<br>
<br>

# 🧠 What Does "Mutable Value" Mean?

Mutable = can change without creating a new value reference.

Example:

``` js
let x = 5;
x = 10; // changed
```

It changed.

But in React, the important question is:

👉 Do we want React to re-render when it changes?

If YES → useState
If NO → useRef

------------------------------------------------------------------------

# 🟡 Why useRef is Perfect for Mutable Values

When you update:

``` js
myRef.current = newValue;
```

React does NOT re-render.

Because React does not track `.current`.

It just keeps it stored between renders.

------------------------------------------------------------------------

# 🔥 Example 1 --- Tracking Previous Value

Very common pattern.

``` js
import { useEffect, useRef } from "react";

function Example({ count }) {
  const prevCount = useRef();

  useEffect(() => {
    prevCount.current = count;
  });

  return (
    <div>
      <p>Current: {count}</p>
      <p>Previous: {prevCount.current}</p>
    </div>
  );
}
```

### What's happening?

-   `prevCount.current` stores old value
-   It updates after render
-   It does NOT trigger extra re-renders

This is storing a mutable value safely.

------------------------------------------------------------------------

# 🔥 Example 2 --- Storing Timer ID

``` js
const intervalRef = useRef(null);

useEffect(() => {
  intervalRef.current = setInterval(() => {
    console.log("Running");
  }, 1000);

  return () => clearInterval(intervalRef.current);
}, []);
```

### Why useRef?

Because:

-   Interval ID is not UI data
-   We just need to store it
-   No reason to re-render

Perfect use case.

------------------------------------------------------------------------

# 🔥 Example 3 --- Tracking Renders

``` js
const renderCount = useRef(0);

renderCount.current += 1;

console.log("Renders:", renderCount.current);
```

This increases every render.
But doesn't cause new renders.

If this was state → infinite loop 💀

------------------------------------------------------------------------

# 🧠 The Real Difference (Deep Understanding)

## useState

-   Immutable updates
-   Triggers re-render
-   Used for UI

## useRef

-   Mutable container
-   No re-render
-   Used for internal logic

------------------------------------------------------------------------

# ⚡ Think About Your E-commerce Project

### Things that should use useRef:

-   Timeout IDs
-   Scroll position tracking
-   Previous product ID
-   Storing websocket instance

### Things that should use useState:

-   Cart count
-   Selected product
-   Modal visibility
-   Logged-in status

Big difference.

------------------------------------------------------------------------

# 🎯 Clean Mental Model

`useRef` =

> "Remember this, but don't re-render when it changes."