# 🧠 Stateful vs Stateless Components

This is about whether a component manages its own state or not.

------------------------------------------------------------------------

## 🔵 1️⃣ Stateless Component

A stateless component:

-   ❌ Does NOT manage its own state
-   ✅ Just receives data via props
-   ✅ Just displays UI

It's also called a **Presentational component**.

### Example:

``` jsx
const Welcome = ({ name }) => {
  return <h1>Hello {name}</h1>;
};
```

This component:

-   Doesn't store anything
-   Doesn't update anything
-   Just displays what it receives

It depends on the parent.

------------------------------------------------------------------------

## 🔴 2️⃣ Stateful Component

A stateful component:

-   ✅ Manages its own state
-   ✅ Can change UI dynamically
-   ✅ Uses `useState` (functional) or `this.state` (class)

### Example:

``` jsx
import { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>{count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increase
      </button>
    </div>
  );
};
```

This component:

-   Stores data (`count`)
-   Updates data
-   Re-renders when state changes

That's stateful.

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

### 🛒 E-commerce

-   `ProductCard` → Usually Stateless
-   `CartPage` → Stateful (manages cart items)

### 🎓 LMS

-   `CourseCard` → Stateless
-   `VideoPlayer` → Stateful (current video, progress, etc.)

------------------------------------------------------------------------

## ⚡ Important Modern React Concept

In modern React:

👉 Most components can be functional
👉 Some are stateful
👉 Some are stateless

You don't need separate "types" anymore.

It's just:

**Does this component manage state or not?**

------------------------------------------------------------------------

## 🎯 Architecture Thinking (Very Important for You)

In production apps:

-   Keep components stateless when possible
-   Lift state up to parent components
-   Pass data down via props

This makes apps predictable and scalable.