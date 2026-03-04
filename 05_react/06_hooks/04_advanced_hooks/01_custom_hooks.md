# React Custom Hooks

A **Custom Hook** in React is simply a JavaScript function that uses
React hooks (`useState`, `useEffect`, etc.) so you can **reuse logic
across components**.

Think of it like:

👉 **Move repeated hook logic into one reusable function.**

---

# 1️⃣ Why Custom Hooks?

Sometimes multiple components need the same logic.

Examples:

- Fetching API data
- Form handling
- Window resize detection
- Authentication check

Instead of repeating code in many components, we create a **custom
hook**.

---

# 2️⃣ Basic Rule

Custom hooks must start with **`use`**.

Examples:

    useFetch
    useAuth
    useForm
    useWindowSize

This naming convention tells React that it is a **hook function**.

---

# 3️⃣ Simple Example

## Custom Hook

```jsx
import { useState } from "react";

function useCounter() {
  const [count, setCount] = useState(0);

  const increase = () => {
    setCount(count + 1);
  };

  return { count, increase };
}

export default useCounter;
```

## Using the Hook

```jsx
import useCounter from "./useCounter";

function App() {
  const { count, increase } = useCounter();

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increase}>Increase</button>
    </div>
  );
}
```

Now the logic is **reusable**.

---

# 4️⃣ Real Example (API Fetch Hook)

```jsx
import { useState, useEffect } from "react";

function useFetch(url) {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setData(data));
  }, [url]);

  return data;
}
```

### Usage

```javascript
const users = useFetch("/api/users");
```

---

# 5️⃣ Structure of a Custom Hook

    function useSomething() {
       useState()
       useEffect()
       useRef()

       return something
    }

---

# 6️⃣ Important Rule

Custom hooks **follow the same rules as React hooks**.

They **cannot be called inside**:

    ❌ loops
    ❌ conditions
    ❌ nested functions

---

# 7️⃣ Real Usage in Large Apps

In real React projects like **LMS or E-commerce apps**, custom hooks are
often used for:

    useAuth()     → login status
    useCart()     → shopping cart logic
    useFetch()    → API calls
    useDebounce() → search optimization

They help keep components **clean and maintainable**.

---

# ✅ One-Line Definition

**Custom Hook = reusable hook logic**
