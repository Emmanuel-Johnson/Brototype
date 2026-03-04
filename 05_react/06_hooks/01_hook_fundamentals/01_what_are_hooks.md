# 🪝 What Are Hooks in React?

Hooks are **special functions** that let functional components use React
features like:

-   State
-   Lifecycle
-   Context
-   Refs
-   Performance optimizations

👉 Before Hooks, only **class components** could use state and lifecycle
methods.
Hooks completely changed that.

📅 Introduced in **React 16.8 (2019)**

------------------------------------------------------------------------

## 🧠 Simple Definition

> Hooks let you "hook into" React features inside functional components.

That's it.

------------------------------------------------------------------------

# 🚀 Why Hooks Were Needed

## ❌ Before Hooks (Class Component)

``` js
class Component extends React.Component {
  state = { count: 0 };

  componentDidMount() {}
}
```

## ✅ After Hooks (Functional Component)

``` js
function Component() {
  const [count, setCount] = useState(0);
}
```

Cleaner.
Less boilerplate.
Easier to reuse logic.

------------------------------------------------------------------------

# 🔥 Most Important Hooks (You MUST Master These)

## 1️⃣ useState

👉 Adds state to functional components.

``` js
const [count, setCount] = useState(0);
```

-   `count` → current value
-   `setCount` → function to update state
-   Triggers re-render when changed

------------------------------------------------------------------------

## 2️⃣ useEffect

👉 Handles side effects (API calls, timers, DOM changes)

Replaces:

-   `componentDidMount`
-   `componentDidUpdate`
-   `componentWillUnmount`

Example:

``` js
useEffect(() => {
  console.log("Component mounted");
}, []);
```

⚠️ That empty dependency array is important.

------------------------------------------------------------------------

## 3️⃣ useRef

👉 Stores a value that does **NOT** trigger re-render
👉 Also used to access DOM elements

``` js
const inputRef = useRef(null);
```

Useful for: - Focusing inputs - Storing previous values - Persisting
mutable values

------------------------------------------------------------------------

## 4️⃣ useContext

👉 Used for global state without prop drilling.

Perfect for: - Authentication state - Theme - User data - Cart
management

------------------------------------------------------------------------

# 🧩 Rules of Hooks (Very Important)

Hooks:

- ✅ Must be used inside functional components
- ✅ Must be called at the top level
- ❌ Cannot be inside loops, conditions, or nested functions

Why?
React depends on **call order** to track state correctly.

------------------------------------------------------------------------

# 💡 Why Hooks Are Powerful (Especially for Projects)

If you're building:

-   LMS
-   E-commerce site

Hooks help you:

-   Manage form state
-   Handle authentication
-   Fetch API data
-   Store cart items
-   Manage timers
-   Handle focus
-   Optimize performance

Without hooks → your code becomes messy very fast.

------------------------------------------------------------------------

# 🎯 One-Line Mental Model

> Hooks = React's way of giving superpowers to functional components.