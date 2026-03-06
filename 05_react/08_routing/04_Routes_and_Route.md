# Routes & Route

In React routing, **Routes** and **Route** are components from **React
Router** used to define which component should render for a specific
**URL path**.

------------------------------------------------------------------------

# 1️⃣ Routes

**Routes** is a container that holds all the route definitions.

It checks the **current URL** and finds the **matching route**.

### Example

``` jsx
<Routes>
  ...
</Routes>
```

Think of it as a **route manager** that decides which page to show.

------------------------------------------------------------------------

# 2️⃣ Route

**Route** defines a mapping between a **URL path** and a **React
component**.

### Example

``` jsx
<Route path="/about" element={<About />} />
```

Meaning:

    /about → About component

------------------------------------------------------------------------

# Basic Example

``` javascript
import { BrowserRouter, Routes, Route } from "react-router-dom";

function Home() {
  return <h1>Home Page</h1>;
}

function About() {
  return <h1>About Page</h1>;
}

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

# How It Works

When user visits:

    http://localhost:3000/about

### Flow

    BrowserRouter
          ↓
    Routes checks URL
          ↓
    Route path="/about" matches
          ↓
    <About /> component renders

------------------------------------------------------------------------

# Multiple Routes Example

``` jsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  <Route path="/products" element={<Products />} />
</Routes>
```

### Mapping

  URL           Component
  ------------- -----------
  `/`           Home
  `/about`      About
  `/products`   Products

------------------------------------------------------------------------

# Important Rule

**Route must be inside Routes.**

### ❌ Wrong

``` jsx
<Route path="/" element={<Home />} />
```

### ✅ Correct

``` jsx
<Routes>
  <Route path="/" element={<Home />} />
</Routes>
```

------------------------------------------------------------------------

# Simple Definition

**Routes** → container that looks for matching routes
**Route** → defines which component should render for a URL path

💡 **Quick way to remember:**

    Routes → checks URL
    Route  → defines page