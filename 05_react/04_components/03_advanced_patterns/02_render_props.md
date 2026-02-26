# 🧠 What Are Render Props?

A Render Prop is:

👉 A pattern where a component shares logic by passing a function as a
prop.

That function returns JSX.

So instead of wrapping a component (like HOC),
we pass a function that decides what to render.

------------------------------------------------------------------------

## 🔥 Basic Idea

A component doesn't decide UI.

It gives you data.

You decide UI.

------------------------------------------------------------------------

## 🧩 Simple Example

Let's say we want to reuse mouse tracking logic.

``` jsx
import { useState } from "react";

const MouseTracker = ({ render }) => {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouseMove = (e) => {
    setPosition({ x: e.clientX, y: e.clientY });
  };

  return (
    <div onMouseMove={handleMouseMove} style={{ height: "100vh" }}>
      {render(position)}
    </div>
  );
};
```

Now use it like this:

``` jsx
<MouseTracker
  render={({ x, y }) => (
    <h1>
      Mouse at ({x}, {y})
    </h1>
  )}
/>
```

### What happened?

-   `MouseTracker` manages logic
-   You decide what to render
-   That function is the render prop

------------------------------------------------------------------------

## 🧠 Why Is It Called "Render Prop"?

Because:

You pass a prop that is responsible for rendering something.

Often the prop name is `render`,
but it can also be `children`.

------------------------------------------------------------------------

## 🔥 Very Common Pattern (Using children)

``` jsx
const DataProvider = ({ children }) => {
  const data = "Hello Emmanuel";

  return children(data);
};
```

Use it:

``` jsx
<DataProvider>
  {(data) => <h1>{data}</h1>}
</DataProvider>
```

That function inside is the render prop.

------------------------------------------------------------------------

## 🆚 Render Props vs HOC

  HOC                     Render Props
  ----------------------- ---------------------
  Wraps component         Passes function
  Returns new component   Gives control of UI
  Less flexible UI        More flexible UI

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

Imagine in your LMS:

You create a `WithUser` component that fetches user data.

Instead of hardcoding UI inside it,
you let each page decide how to display the user.

That's render props thinking.

------------------------------------------------------------------------

## ⚠️ Modern React Note

Today, we mostly use:

👉 Custom Hooks instead of render props

Because hooks are cleaner and less nested.

But interviews still ask this.