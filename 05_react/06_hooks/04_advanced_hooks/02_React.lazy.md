# React.lazy

`React.lazy` is used for **lazy loading components** in React.

Lazy loading means a component is **loaded only when it is needed**, not
when the app first loads.

👉 This helps **reduce bundle size** and **improve performance**.

------------------------------------------------------------------------

# 1️⃣ Why React.lazy?

Normally React loads **all components at the start**.

Example:

    App loads
    ├── Home
    ├── About
    ├── Dashboard
    ├── Profile

Even if the user **never visits Dashboard**, it still loads.

With **lazy loading**, React loads the component **only when the user
navigates to it**.

------------------------------------------------------------------------

# 2️⃣ Basic Example

``` jsx
import React, { lazy, Suspense } from "react";

const About = lazy(() => import("./About"));

function App() {
  return (
    <Suspense fallback={<h1>Loading...</h1>}>
      <About />
    </Suspense>
  );
}

export default App;
```

### Explanation

-   `lazy()` → dynamically imports the component
-   `Suspense` → shows a loading UI while the component loads

------------------------------------------------------------------------

# 3️⃣ Lazy Loading with React Router

This is the **most common use case**.

``` jsx
import { lazy, Suspense } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<h1>Loading...</h1>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

Now:

-   `Home` loads first
-   `About` loads **only when the user visits `/about`**

------------------------------------------------------------------------

# 4️⃣ Normal Import vs Lazy Import

## Normal Import

``` javascript
import About from "./About";
```

Loads **immediately**.

## Lazy Import

``` javascript
const About = React.lazy(() => import("./About"));
```

Loads **only when used**.

------------------------------------------------------------------------

# 5️⃣ Easy Way to Remember

    React.lazy → lazy load components
    Suspense   → loading UI

------------------------------------------------------------------------

# 6️⃣ Where it is used in real apps

In large apps like **LMS or E-commerce platforms**, lazy loading is
commonly used for:

-   Dashboard pages
-   Admin panels
-   Reports
-   Analytics pages
-   Heavy components

This helps make the **initial page load faster**.

------------------------------------------------------------------------

# ✅ One-line Summary

**React.lazy loads components only when they are needed.**

<br>
<br>
<br>

# React Suspense

`Suspense` is a React component used to **show a fallback UI while
something is loading**.

It is most commonly used with **React.lazy** for lazy-loaded components.

Think of it like:

> **Show this loading UI until the component finishes loading.**

------------------------------------------------------------------------

# 1️⃣ Basic Example

``` jsx
import React, { lazy, Suspense } from "react";

const About = lazy(() => import("./About"));

function App() {
  return (
    <Suspense fallback={<h1>Loading...</h1>}>
      <About />
    </Suspense>
  );
}

export default App;
```

### What happens

1.  `About` component starts loading.
2.  While loading → React shows the **fallback UI**.
3.  When loading finishes → **About component renders**.

------------------------------------------------------------------------

# 2️⃣ What `fallback` means

`fallback` is the **UI shown while loading**.

Example:

``` jsx
<Suspense fallback={<p>Loading page...</p>}>
```

You can show:

-   Text
-   Spinner
-   Loader animation
-   Skeleton UI

Example:

``` jsx
<Suspense fallback={<Spinner />}>
```

------------------------------------------------------------------------

# 3️⃣ Using Suspense with React Router (Very Common)

``` jsx
import { lazy, Suspense } from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<h2>Loading...</h2>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

Here:

-   Pages load **only when visited**
-   `Suspense` shows the **loading UI**

------------------------------------------------------------------------

# 4️⃣ Simple Flow

    User opens page
          ↓
    Component lazy loads
          ↓
    Suspense shows fallback
          ↓
    Component finishes loading
          ↓
    Actual component renders

------------------------------------------------------------------------

# 5️⃣ Easy Way to Remember

    React.lazy → load component later
    Suspense   → show loading UI

They are usually **used together**.

------------------------------------------------------------------------

# Real Pattern Used in Apps

In large apps like **LMS or E-commerce dashboards**, you will often see:

``` jsx
const Page = lazy(() => import("./Page"));

<Suspense fallback={<Loader />}>
   <Page />
</Suspense>
```

This keeps the **initial bundle smaller** and **apps load faster**.

------------------------------------------------------------------------

# ✅ One-Line Summary

**Suspense shows a loading UI while a lazy component is loading.**

<br>
<br>
<br>

# Code Splitting in React

Code Splitting is a technique used to split your JavaScript bundle into smaller pieces so the browser loads only the code needed for the current page, instead of loading the entire app at once.

This improves performance and loading speed 🚀.

---

# Why Code Splitting is Needed

In a big React app:

```
App
 ├ Home
 ├ About
 ├ Dashboard
 ├ Settings
 └ Profile
```

If everything is bundled together:

```
bundle.js (2MB)
```

When the user opens **Home**, the browser still downloads:

- About
- Dashboard
- Settings
- Profile

even though they are not needed.

That wastes time.

**Code splitting solves this.**

---

# Without Code Splitting

Everything loads immediately.

User opens **Home**

Browser downloads:

- Home
- About
- Dashboard
- Settings
- Profile

**Large bundle → slower first load**

---

# With Code Splitting

Only the required component loads.

User opens **Home**

→ Only **Home** loads

User clicks **About**

→ **About loads then**

So the app becomes **faster**.

---

# React Code Splitting

React usually uses:

- `React.lazy()`
- `Suspense`

---

# Example

## Normal Import (No Code Splitting)

```javascript
import About from "./About";
```

This loads **About immediately**.

---

## Lazy Import (Code Splitting)

```javascript
import { lazy, Suspense } from "react";

const About = lazy(() => import("./About"));
```

Now **About loads only when needed**.

---

# Using Suspense

```javascript
import { lazy, Suspense } from "react";

const About = lazy(() => import("./About"));

function App() {
  return (
    <Suspense fallback={<h1>Loading...</h1>}>
      <About />
    </Suspense>
  );
}
```

### Explanation

User opens page  
↓  
React loads **About component**  
↓  
While loading → shows **"Loading..."**  
↓  
After load → shows **About page**

---

# Real Example With React Router

This is where code splitting is very useful.

```javascript
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { lazy, Suspense } from "react";

const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));

function App() {
  return (
    <BrowserRouter>
      <Suspense fallback={<h1>Loading...</h1>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

Now:

```
/        → loads Home
/about   → loads About only when visited
```

Perfect for **large apps**.

---

# Quick Summary

| Concept | Meaning |
|------|------|
| Code Splitting | Splitting bundle into smaller chunks |
| Goal | Faster loading |
| React Tool | React.lazy() |
| Loading UI | Suspense |
| Best Use | Large apps + routing |

---

# Interview Definition

> Code Splitting is a technique that splits the JavaScript bundle into smaller chunks so that only the required code loads when needed, improving application performance.