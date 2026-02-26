# ⚡ What Are Functional Components in React?

A functional component is just a **JavaScript function that returns JSX
(UI).**

That's it.

Simple. Clean. Modern.

------------------------------------------------------------------------

## 🧠 Basic Example

``` jsx
function Welcome() {
  return <h1>Hello 👋</h1>;
}
```

Or arrow function (most common style now):

``` jsx
const Welcome = () => {
  return <h1>Hello 👋</h1>;
};
```

Both are functional components.

------------------------------------------------------------------------

## 🔥 Why Functional Components Are Important

In modern React:

-   ✅ We use functional components
-   ❌ Class components are mostly outdated
-   ✅ We use Hooks (like `useState`, `useEffect`) inside functional
    components

If you're building production projects (like your LMS & E-commerce),
you'll use functional components everywhere.

------------------------------------------------------------------------

## 🧩 Adding State (Real Power)

Functional components become powerful when you use Hooks.

Example:

``` jsx
import { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </div>
  );
};
```

Now this component:

-   Stores data (`count`)
-   Updates UI dynamically
-   Handles events

This is modern React.

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

### In your E-commerce:

``` jsx
const ProductCard = ({ product }) => {
  return (
    <div>
      <h3>{product.name}</h3>
      <p>₹{product.price}</p>
    </div>
  );
};
```

### In your LMS:

``` jsx
const CourseCard = ({ course }) => {
  return (
    <div>
      <h2>{course.title}</h2>
      <p>{course.instructor}</p>
    </div>
  );
};
```

Each is:

-   Small
-   Focused
-   Reusable

That's clean architecture thinking.

------------------------------------------------------------------------

## 🆚 Functional vs Class (Quick Comparison)

  Functional Component   Class Component
  ---------------------- ------------------------
  Simple function        Uses `class` keyword
  Uses Hooks             Uses lifecycle methods
  Less boilerplate       More code
  Modern standard        Legacy style

You should focus 100% on functional components now.