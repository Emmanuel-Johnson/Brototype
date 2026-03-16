# React Counter with Start & Stop (useEffect + setInterval)

## 1️⃣ Counter with Start & Stop

``` javascript
import { useState, useEffect } from "react";

function Counter() {
  const [count, setCount] = useState(0);
  const [running, setRunning] = useState(false);

  useEffect(() => {
    let interval;

    if (running) {
      interval = setInterval(() => {
        setCount((prev) => prev + 1);
      }, 1000);
    }

    return () => clearInterval(interval);
  }, [running]);

  return (
    <div>
      <h1>Counter: {count}</h1>

      <button onClick={() => setRunning(true)}>
        Start
      </button>

      <button onClick={() => setRunning(false)}>
        Stop
      </button>
    </div>
  );
}

export default Counter;
```

------------------------------------------------------------------------

# 2️⃣ How This Works

## useState

``` javascript
const [count, setCount] = useState(0);
```

Stores the **counter value**.

``` javascript
const [running, setRunning] = useState(false);
```

Controls whether the **timer is running**.

------------------------------------------------------------------------

## useEffect

``` javascript
useEffect(() => { ... }, [running]);
```

This runs whenever **`running` changes**.

------------------------------------------------------------------------

## When Start is clicked

``` javascript
setRunning(true)
```

-   `useEffect` runs
-   It creates an **interval**

``` javascript
setInterval(() => {
  setCount(prev => prev + 1)
}, 1000)
```

The counter increases **every 1 second**.

------------------------------------------------------------------------

## When Stop is clicked

``` javascript
setRunning(false)
```

The **cleanup function** inside `useEffect` runs:

``` javascript
clearInterval(interval)
```

The timer **stops**.

------------------------------------------------------------------------

# 3️⃣ Cleaner Version (with Reset)

You can add a **Reset button**:

``` javascript
<button onClick={() => setCount(0)}>
  Reset
</button>
```

------------------------------------------------------------------------

# ✅ Skills You Learn From This

-   `useState`
-   `useEffect`
-   `setInterval`
-   `clearInterval`
-   **Cleanup functions**

Common real‑world uses:

-   Timers
-   Polling APIs
-   Countdowns
-   Auto refresh systems