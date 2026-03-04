# 🧠 What is useState?

`useState` is a React Hook that lets a functional component store and
update data.

Before hooks → only class components could have state.
Now → functional components can have state too.

------------------------------------------------------------------------

## 📦 Basic Syntax

``` js
const [state, setState] = useState(initialValue);
```

-   `state` → current value
-   `setState` → function to update it
-   `initialValue` → starting value

------------------------------------------------------------------------

## 🔥 Simple Example (Counter)

``` js
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => setCount(count + 1)}>
        Increase
      </button>
    </div>
  );
}
```

### What happens here?

1️⃣ Component loads → `count = 0`
2️⃣ Button click → `setCount(count + 1)`
3️⃣ React updates state
4️⃣ Component re-renders
5️⃣ UI shows new value

------------------------------------------------------------------------

# 🧠 Important Things to Understand

## 1️⃣ Changing state causes re-render

When you call `setCount()`, React re-renders the component.

------------------------------------------------------------------------

## 2️⃣ You MUST use the setter function

❌ Wrong:

``` js
count = 5
```

✅ Correct:

``` js
setCount(5)
```

React only tracks updates through the setter function.

------------------------------------------------------------------------

## 3️⃣ State is preserved between renders

Even when the component re-renders, the value doesn't reset.

That's why it's called **state** --- it remembers.

------------------------------------------------------------------------

# 🧩 useState with Different Types

### Number

``` js
useState(0)
```

### String

``` js
useState("Emmanuel")
```

### Boolean

``` js
useState(false)
```

### Object

``` js
useState({ name: "", age: 0 })
```

### Array

``` js
useState([])
```

------------------------------------------------------------------------

# 🧠 Very Important (For Your Projects)

In your e-commerce project, things like:

-   Cart items
-   Product quantity
-   Modal open/close
-   Logged-in status

👉 All of these use `useState`.

If you don't store it in the backend and just use `useState`,
closing the tab = data gone.

------------------------------------------------------------------------

# 🪝 Mental Model

Think of `useState` like:

> "Hey React, please remember this value for this component."