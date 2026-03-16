# React useEffect Cleanup Function (Component Unmount)

## Print a Message When a Component Unmounts

In React, to print a message when a component unmounts, you use the **cleanup function** of `useEffect`.

When React removes a component from the DOM, the **function returned from `useEffect` runs**.

---

# Example: Print Message on Unmount

```javascript
import { useEffect } from "react";

function MyComponent() {

  useEffect(() => {
    console.log("Component Mounted");

    return () => {
      console.log("Component Unmounted");
    };

  }, []);

  return <h2>Hello Component</h2>;
}

export default MyComponent;
```

---

# How It Works

## 1️⃣ Component Mounts

When the component appears on the screen:

```javascript
console.log("Component Mounted");
```

---

## 2️⃣ Component Unmounts

When the component is removed:

```javascript
return () => {
  console.log("Component Unmounted");
};
```

This function is called the **cleanup function**.

---

# Lifecycle Flow

```
Component Mount
      ↓
useEffect runs
      ↓
Component works
      ↓
Component removed
      ↓
Cleanup function runs
```

---

# Example with Button (to See Unmount)

```javascript
import { useState } from "react";
import MyComponent from "./MyComponent";

function App() {
  const [show, setShow] = useState(true);

  return (
    <div>
      <button onClick={() => setShow(!show)}>
        Toggle Component
      </button>

      {show && <MyComponent />}
    </div>
  );
}

export default App;
```

If you click **Toggle Component**, React removes `MyComponent`, and the console prints:

```
Component Unmounted
```

---

# Real Use Cases for Unmount Cleanup

Developers use this cleanup function to:

* Clear intervals
* Remove event listeners
* Cancel API requests
* Close subscriptions

---

# Example: Clearing an Interval

```javascript
useEffect(() => {
  const interval = setInterval(() => {
    console.log("Running...");
  }, 1000);

  return () => clearInterval(interval);
}, []);
```

---

# 💡 Important Rule (React Interviews)

The function returned from `useEffect` runs:

* When the **component unmounts**
* **Before the effect runs again** if dependencies change
