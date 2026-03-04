# React Optimization Guidelines

A common rule in React development:

> **First make it work, then optimize only if there is a real
> performance problem.**

Let's break it down.

------------------------------------------------------------------------

# 1️⃣ Do NOT optimize by default

React is already very fast. Most apps **do not need optimization**.

Bad practice:

``` jsx
useMemo(...)
useCallback(...)
React.memo(...)
```

Using these **everywhere** makes code:

-   Harder to read
-   Harder to maintain
-   Sometimes even **slower**

------------------------------------------------------------------------

# 2️⃣ Optimize when there is unnecessary re-render

Example situation:

-   Parent component re-renders
-   Child components re-render
-   But their **props didn't change**

Then you can use:

    React.memo

Typical cases:

-   Big components
-   List items
-   Complex UI

------------------------------------------------------------------------

# 3️⃣ Optimize expensive calculations

Example:

``` javascript
const result = bigArray
  .filter(...)
  .map(...)
  .reduce(...);
```

If this runs on **every render**, it may slow the app.

Use:

``` javascript
const result = useMemo(() => expensiveCalculation(), [deps]);
```

This ensures the calculation only runs when **dependencies change**.

------------------------------------------------------------------------

# 4️⃣ Optimize when passing functions to memoized children

Example:

``` jsx
<Child onClick={handleClick} />
```

Every render creates a **new function reference**, so `React.memo` won't
work.

Solution:

``` javascript
const handleClick = useCallback(() => {
  console.log("clicked");
}, []);
```

------------------------------------------------------------------------

# 5️⃣ When lists are very large

Example:

-   500+ items
-   Complex UI rendering

Possible optimizations:

-   `React.memo`
-   `useMemo`
-   Virtualized lists (like `react-window`)

------------------------------------------------------------------------

# 🔑 Simple Rule

    React.memo  → prevent component re-render
    useMemo     → prevent expensive calculation
    useCallback → prevent function recreation

But use them **only when needed**.

------------------------------------------------------------------------

# 🧠 Real Developer Workflow

Most React developers follow this order:

    1️⃣ Build the feature
    2️⃣ Test functionality
    3️⃣ Measure performance
    4️⃣ Optimize only slow parts