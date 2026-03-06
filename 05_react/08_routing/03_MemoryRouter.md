# MemoryRouter in React

**MemoryRouter** is a router from **React Router** that stores the
navigation history **in memory instead of the browser URL**.

That means the **URL in the address bar does NOT change**.

------------------------------------------------------------------------

# Simple Idea

### Normal routing

Browser URL changes

    /about
    /products

### MemoryRouter

Routing happens internally and the **URL stays the same**.

The routes are stored inside **JavaScript memory**.

------------------------------------------------------------------------

# Basic Example

``` javascript
import { MemoryRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <MemoryRouter>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>

    </MemoryRouter>
  );
}
```

Here:

    "/"      → Home
    "/about" → About

But the **browser address bar will not change**.

------------------------------------------------------------------------

# When MemoryRouter is Used

## 1️⃣ Testing React components

In **unit tests**, we don't need a real browser URL.

Example testing tools:

-   Jest
-   React Testing Library

------------------------------------------------------------------------

## 2️⃣ React Native apps

**React Native does not have a browser**, so `BrowserRouter` cannot be
used.

------------------------------------------------------------------------

## 3️⃣ Non-browser environments

Examples:

-   Embedded apps
-   Storybook demos
-   Component previews

------------------------------------------------------------------------

# BrowserRouter vs MemoryRouter

  Feature            BrowserRouter     MemoryRouter
  ------------------ ----------------- -----------------------
  Uses browser URL   ✅ Yes            ❌ No
  Stores history     Browser history   In memory
  Used in            Normal web apps   Testing / non-browser
  URL visible        Yes               No

------------------------------------------------------------------------

# Simple Definition

> MemoryRouter is a router that keeps routing history in memory instead
> of using the browser URL.