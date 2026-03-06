# BrowserRouter in React

**BrowserRouter** is a component from **React Router** that enables
routing in a React application using the browser's URL.

It listens to **URL changes** and tells React which component should
render.

------------------------------------------------------------------------

# Why BrowserRouter is Needed

React normally shows **one page (SPA -- Single Page Application)**.

BrowserRouter allows React to **change pages based on the URL without
refreshing the browser**.

### Example URLs

  URL           Page
  ------------- ----------
  `/`           Home
  `/about`      About
  `/products`   Products

------------------------------------------------------------------------

# Basic Example

``` javascript
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>

    </BrowserRouter>
  );
}
```

------------------------------------------------------------------------

# What BrowserRouter Does

When the user visits:

    http://localhost:3000/about

### Flow

    BrowserRouter listens to URL
            ↓
    Routes checks path
            ↓
    Matching Route found
            ↓
    <About /> component renders

------------------------------------------------------------------------

# Important Rule

**BrowserRouter must wrap the entire app.**

### Example (common structure)

``` javascript
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { BrowserRouter } from "react-router-dom";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

Now every component inside **App** can use routing.

------------------------------------------------------------------------

# Key Points

-   Provides routing capability
-   Uses **Browser History API**
-   Allows **client-side navigation**
-   Prevents **page reload**

------------------------------------------------------------------------

# Simple Definition

> BrowserRouter is a router component that uses the browser URL to
> enable client-side routing in a React application.