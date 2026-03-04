# 🧠 What is useEffect?

`useEffect` is a React Hook that lets you handle side effects inside
functional components.

------------------------------------------------------------------------

## 🤔 What is a "side effect"?

Anything that happens outside normal rendering.

### Examples:

-   API calls
-   Timers (`setTimeout`, `setInterval`)
-   DOM manipulation
-   Event listeners
-   Subscriptions
-   Local storage
-   Cleanup logic

Basically:

> If it touches something outside React's render → it's a side effect.

------------------------------------------------------------------------

## 📦 Basic Syntax

``` js
useEffect(() => {
  // side effect code here
}, [dependencies]);
```

Two parts matter:

- 1️⃣ The function → what to run
- 2️⃣ The dependency array → when to run it

------------------------------------------------------------------------

# 🔥 Example 1 --- Runs Once (Like componentDidMount)

``` js
import { useEffect } from "react";

function App() {
  useEffect(() => {
    console.log("Component mounted");
  }, []);

  return <h1>Hello</h1>;
}
```

### Why only once?

Because the dependency array is empty:

``` js
[]
```

That means:

👉 Run only after first render.

Perfect for:

-   Fetching data from backend (Django API)
-   Initial setup

------------------------------------------------------------------------

# 🔁 Example 2 --- Run When State Changes

``` js
import { useState, useEffect } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log("Count changed:", count);
  }, [count]);

  return (
    <button onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}
```

Now it runs:

-   First render
-   Every time `count` changes

------------------------------------------------------------------------

# ❌ What If No Dependency Array?

``` js
useEffect(() => {
  console.log("Runs every render");
});
```

👉 Runs after every single render.

Usually not what you want.

------------------------------------------------------------------------

# 🧹 Cleanup Function (VERY Important)

``` js
useEffect(() => {
  const interval = setInterval(() => {
    console.log("Running...");
  }, 1000);

  return () => {
    clearInterval(interval);
  };
}, []);
```

The return function is called when:

-   Component unmounts
-   Before effect runs again

This prevents:

-   Memory leaks
-   Duplicate timers
-   Multiple event listeners

------------------------------------------------------------------------

# 🧠 Mental Model (Very Important)

React flow:

- 1️⃣ Component renders
- 2️⃣ DOM updates
- 3️⃣ THEN `useEffect` runs

So:

Rendering first. Effect second.

------------------------------------------------------------------------

# 🔥 Real Example for Your Projects

``` js
useEffect(() => {
  fetch("http://localhost:8000/api/products")
    .then(res => res.json())
    .then(data => setProducts(data));
}, []);
```

That's how frontend talks to Django backend.

Without `useEffect`, your API call would run on every render and destroy
performance.

------------------------------------------------------------------------

# 🪝 Quick Comparison

| Hook      | Purpose             |
| --------- | ------------------- |
| useState  | Store data (state)  |
| useEffect | Handle side effects |

  <br>
  <br>
  <br>

# 🧠 Exact Lifecycle Mapping (Hooks vs Class)

In class components, we had:

-   componentDidMount
-   componentDidUpdate
-   componentWillUnmount

In functional components, `useEffect` replaces all three.

------------------------------------------------------------------------

## 🎯 componentDidMount → useEffect with []

### Class:

``` js
componentDidMount() {
  console.log("Mounted");
}
```

### Hooks version:

``` js
useEffect(() => {
  console.log("Mounted");
}, []);
```

- ✅ Runs once
- ✅ After first render

------------------------------------------------------------------------

## 🔁 componentDidUpdate → useEffect with dependencies

### Class:

``` js
componentDidUpdate(prevProps, prevState) {
  if (prevState.count !== this.state.count) {
    console.log("Count updated");
  }
}
```

### Hooks:

``` js
useEffect(() => {
  console.log("Count updated");
}, [count]);
```

- ✅ Runs after render
- ✅ Runs when `count` changes

------------------------------------------------------------------------

## 🧹 componentWillUnmount → Cleanup function

### Class:

``` js
componentWillUnmount() {
  console.log("Component removed");
}
```

### Hooks:

``` js
useEffect(() => {
  return () => {
    console.log("Component removed");
  };
}, []);
```

That return function is the cleanup.

------------------------------------------------------------------------

# 🧹 Cleanup (Unmount Logic) --- Deep Understanding

The cleanup runs in two situations:

- ✅ 1. When component unmounts
- ✅ 2. Before the effect runs again (if dependencies changed)

------------------------------------------------------------------------

## 🔥 Example with Timer

``` js
useEffect(() => {
  const interval = setInterval(() => {
    console.log("Running...");
  }, 1000);

  return () => {
    clearInterval(interval);
  };
}, []);
```

### What happens?

- 1️⃣ Component mounts
- 2️⃣ Timer starts
- 3️⃣ If component unmounts → cleanup runs → timer stops

If you don't clean it:

💀 Timer keeps running in memory → memory leak.

------------------------------------------------------------------------

## 🔥 Example with Event Listener

``` js
useEffect(() => {
  const handleScroll = () => {
    console.log("Scrolling");
  };

  window.addEventListener("scroll", handleScroll);

  return () => {
    window.removeEventListener("scroll", handleScroll);
  };
}, []);
```

Without cleanup:

-   Every re-render adds a new listener
-   You get multiple logs
-   App performance drops

------------------------------------------------------------------------

# 🧠 Super Clear Timeline

``` js
useEffect(() => {
  console.log("Effect running");

  return () => {
    console.log("Cleanup running");
  };
}, [count]);
```

If `count` changes, flow is:

- 1️⃣ Render happens
- 2️⃣ Cleanup runs (from previous effect)
- 3️⃣ New effect runs

Important:

👉 Cleanup runs BEFORE the next effect.

------------------------------------------------------------------------

# 🔥 For Your Django + React Projects

Imagine:

-   User opens product page
-   You start a websocket / polling
-   User navigates away

If you don't clean up:

- ❌ API keeps calling
- ❌ Memory leak
- ❌ Unexpected bugs

Cleanup prevents that.

------------------------------------------------------------------------

# 🧠 Ultimate Mental Model

`useEffect` is like:

> "After React finishes rendering, do this extra work.
> And if needed, clean it up before leaving or re-running."