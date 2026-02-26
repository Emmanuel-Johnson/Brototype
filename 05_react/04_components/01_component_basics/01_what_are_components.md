# 🚀 What Are Components in React?

Components are the **building blocks** of a React application.

Think of them like **LEGO pieces 🧱**
Each piece does one small job.
Combine them → you build a full website.

Instead of writing one huge HTML file, React lets you break UI into
small, reusable pieces.

------------------------------------------------------------------------

## 🧠 Simple Definition

A component is a **JavaScript function that returns JSX (UI).**

``` jsx
function Welcome() {
  return <h1>Hello Emmanuel 👋</h1>;
}
```

That's a component.

------------------------------------------------------------------------

## 🔹 Why Components Matter

Because they help you:

-   ✅ Reuse code
-   ✅ Keep UI organized
-   ✅ Make complex apps manageable
-   ✅ Build dynamic interfaces

For example, in your e-commerce project, you might have:

-   `Navbar` component
-   `ProductCard` component
-   `Cart` component
-   `Checkout` component

Instead of rewriting UI again and again.

------------------------------------------------------------------------

## 🔹 Types of Components

### 1️⃣ Functional Components (Modern & Most Used)

``` jsx
function Button() {
  return <button>Click Me</button>;
}
```

Or arrow function:

``` jsx
const Button = () => {
  return <button>Click Me</button>;
};
```

👉 This is what you'll use 99% of the time.

------------------------------------------------------------------------

### 2️⃣ Class Components (Older Style)

``` jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello</h1>;
  }
}
```

These are older. Today we mostly use functional components with hooks.

------------------------------------------------------------------------

## 🔹 How Components Work Together

You can use one component inside another.

``` jsx
function App() {
  return (
    <div>
      <Welcome />
      <Button />
    </div>
  );
}
```

So:

-   `App` → Parent
-   `Welcome` & `Button` → Child components

This is how full applications are structured.

------------------------------------------------------------------------

## 🔥 Real Example (From Your Projects)

### In your LMS:

-   `<CourseCard />`
-   `<CourseList />`
-   `<VideoPlayer />`
-   `<ProgressBar />`

### In your E-commerce:

-   `<ProductCard />`
-   `<CartItem />`
-   `<OrderSummary />`

Each does one clear job. That's good architecture.

------------------------------------------------------------------------

## 🎯 Big Picture

React apps are just:

👉 Many small components
👉 Talking to each other
👉 Rendering dynamic UI

**Master components → you master React.**