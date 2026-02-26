# 🧱 Built-in Components in React

There are two common meanings when we say "built-in components" in
React.

------------------------------------------------------------------------

## 1️⃣ Built-in DOM Components (Most Common Meaning)

These are the HTML elements React already understands.

### Examples:

-   `<div>`
-   `<h1>`
-   `<p>`
-   `<button>`
-   `<input>`
-   `<form>`
-   `<ul>`
-   `<li>`

### Example:

``` jsx
const App = () => {
  return <h1>Hello</h1>;
};
```

`<h1>` is a built-in DOM component.

React converts it to real HTML in the browser.

------------------------------------------------------------------------

### 🔑 Important Rule

-   Lowercase → Built-in DOM element
-   Capitalized → Custom component

``` jsx
<MyComponent />   // ✅ Custom component
<div />           // ✅ Built-in DOM component
```

If you write:

``` jsx
<myComponent />
```

React thinks it's a DOM tag --- not your component.

👉 Capital letter rule matters.

------------------------------------------------------------------------

## 2️⃣ Built-in React Components / APIs

React also provides special components & helpers built into the library.

Examples:

-   `React.Fragment`
-   `React.StrictMode`
-   `Suspense`
-   `Profiler`

------------------------------------------------------------------------

## 🧩 React Fragment

Instead of adding unnecessary `<div>`:

``` jsx
<>
  <h1>Hello</h1>
  <p>World</p>
</>
```

This is shorthand for:

``` jsx
<React.Fragment>
  <h1>Hello</h1>
  <p>World</p>
</React.Fragment>
```

It groups elements without adding extra DOM nodes.

Very useful for clean UI structure.

------------------------------------------------------------------------

## 🚦 React StrictMode

Used in development:

``` jsx
<React.StrictMode>
  <App />
</React.StrictMode>
```

It helps detect:

-   Unsafe lifecycle usage
-   Deprecated APIs
-   Potential bugs

Only works in development mode.

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

### 🎓 LMS

-   `<div>` → Built-in DOM component
-   `<CourseCard />` → Custom component
-   `<> </>` → React Fragment

### 🛒 E-commerce

-   `<form>` → Built-in
-   `<CheckoutForm />` → Custom component

------------------------------------------------------------------------

## 🧠 Quick Rule to Remember

| Type             | Starts With    | Example         |
| ---------------- | -------------- | --------------- |
| Built-in DOM     | lowercase      | `<div>`         |
| Custom Component | Capital letter | `<ProductCard>` |
