# 🔄 React Lifecycle Methods

👉 Lifecycle methods are mainly used in **class components** in React.
In modern React (functional components), we use **Hooks like `useEffect`
instead**.

But understanding lifecycle = understanding how React thinks.

------------------------------------------------------------------------

## 🧠 What Are Lifecycle Methods?

Every React component goes through 3 main phases:

1️⃣ Mounting (Component is created)
2️⃣ Updating (Component re-renders)
3️⃣ Unmounting (Component is removed)

------------------------------------------------------------------------

# 1️⃣ Mounting Phase (Birth)

This happens when a component is added to the DOM for the first time.

### Important lifecycle methods:

-   `constructor()`
-   `render()`
-   `componentDidMount()`

### Flow:

constructor → render → componentDidMount

### Example (Class Component)

``` jsx
class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    console.log("Constructor called");
  }

  componentDidMount() {
    console.log("Component mounted");
  }

  render() {
    return <h1>Hello</h1>;
  }
}
```

### 🔥 Most Important Here:

`componentDidMount()`

Used for:

-   API calls
-   Fetching data
-   Starting timers
-   Setting up subscriptions

------------------------------------------------------------------------

# 2️⃣ Updating Phase (Re-render)

Happens when:

-   Props change
-   State changes

### Important methods:

-   `shouldComponentUpdate()`
-   `render()`
-   `componentDidUpdate()`

### Flow:

shouldComponentUpdate → render → componentDidUpdate

### 🔥 Most Important:

`componentDidUpdate()`

Used for:

-   Reacting to state changes
-   Making API calls after update
-   DOM updates after re-render

### Example:

``` jsx
componentDidUpdate(prevProps, prevState) {
  if (prevState.count !== this.state.count) {
    console.log("Count changed!");
  }
}
```

------------------------------------------------------------------------

# 3️⃣ Unmounting Phase (Death)

When component is removed from DOM.

### Method:

-   `componentWillUnmount()`

Used for:

-   Clearing timers
-   Cancelling API calls
-   Removing event listeners

### Example:

``` jsx
componentWillUnmount() {
  console.log("Component removed");
}
```

Very important for avoiding memory leaks.

------------------------------------------------------------------------

# 🚀 Modern React (Functional Components)

In modern React, we use:

`useEffect()` instead of lifecycle methods.

### Example:

``` jsx
useEffect(() => {
  console.log("Component mounted");

  return () => {
    console.log("Component unmounted");
  };
}, []);
```

This replaces:

-   `componentDidMount`
-   `componentDidUpdate`
-   `componentWillUnmount`

Depending on the dependency array.

------------------------------------------------------------------------

# 🔥 Lifecycle vs useEffect Mapping

  Class Lifecycle Method   Functional Equivalent
  ------------------------ ---------------------------------
  componentDidMount        useEffect(() => {}, [])
  componentDidUpdate       useEffect(() => {}, [dep])
  componentWillUnmount     return cleanup inside useEffect

------------------------------------------------------------------------

# 💡 Real Project Example (E-commerce / LMS)

When your page loads:

✔ Fetch products → componentDidMount
✔ User changes filter → componentDidUpdate
✔ Leaving product page → componentWillUnmount (cleanup)

This is exactly what happens in real production apps.