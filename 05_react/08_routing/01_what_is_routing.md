# Routing

Routing means deciding which **component or page** should be shown based
on the **URL**.

In simple terms:
👉 Routing connects a **URL path** to a **specific page/component**.

------------------------------------------------------------------------

## Example

  URL           Page Shown
  ------------- ---------------
  `/`           Home page
  `/products`   Products page
  `/about`      About page

So when a user goes to:

    www.site.com/products

The router shows the **Products component**.

------------------------------------------------------------------------

# Why Routing is Needed

Without routing, a website would have **only one page**.

Routing lets us build **multiple pages inside one application**.

Example website pages:

-   Home
-   Login
-   Dashboard
-   Products
-   Cart

Each page has its **own route (URL path)**.

------------------------------------------------------------------------

# Example in React (React Router)

We use **React Router**.

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

### Meaning

-   `/` → **Home component**
-   `/about` → **About component**

------------------------------------------------------------------------

# What Happens Internally

    User clicks link
    ↓
    URL changes
    ↓
    Router checks the path
    ↓
    Matching component renders

------------------------------------------------------------------------

# Real Example

If a user clicks **Products**:

    /products

Router shows:

``` jsx
<Products />
```

Without refreshing the page.

------------------------------------------------------------------------

# Types of Routing

## 1. Client-side Routing

Used in **React apps**.

-   Browser **does NOT reload** the page.
-   Routing happens inside JavaScript.

Example: **React Router**

------------------------------------------------------------------------

## 2. Server-side Routing

Used in **backend frameworks** like **Django**.

The **server decides** which page to send.

Example:

    /products → Django view → HTML page

------------------------------------------------------------------------

# Simple Definition (Interview Style)

> Routing is the process of mapping a **URL path** to a **specific
> component or page** in an application.

<br>
<br>
<br>

# Routing in React Applications

Routing in a React application means displaying different components
based on the URL **without reloading the page**.

Instead of loading a completely new HTML page, React changes the
**component inside the same page**.

This is called **client-side routing**.

------------------------------------------------------------------------

# Library Used for Routing

React usually uses **React Router** to handle routing.

It allows us to map:

**URL paths → React components**

## Example

  URL           Component Rendered
  ------------- --------------------
  `/`           Home
  `/about`      About
  `/products`   Products

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

export default App;
```

------------------------------------------------------------------------

# What Happens

User visits `/`

Router checks the path

`<Home />` component is rendered

If user goes to `/about`:

    URL → /about

React renders:

``` jsx
<About />
```

No page reload happens.

------------------------------------------------------------------------

# Important Components in React Routing

## 1. BrowserRouter

Wraps the whole app and **enables routing**.

``` jsx
<BrowserRouter>
  <App />
</BrowserRouter>
```

------------------------------------------------------------------------

## 2. Routes

Container for **all routes**.

``` jsx
<Routes>
  ...
</Routes>
```

------------------------------------------------------------------------

## 3. Route

Defines which component should render for a **specific path**.

``` jsx
<Route path="/about" element={<About />} />
```

Meaning:

    /about → About component

------------------------------------------------------------------------

# Navigation Between Pages

Instead of using `<a>` tag, React uses **Link**.

``` javascript
import { Link } from "react-router-dom";

<Link to="/about">About</Link>
```

### Why?

-   `<a>` reloads the page
-   `Link` changes the component **without refresh**

------------------------------------------------------------------------

# Real Application Flow

    User clicks navigation link
            ↓
    URL changes
            ↓
    Router checks matching route
            ↓
    Correct component renders

------------------------------------------------------------------------

# Example Website Routing

| URL           | Component       |
| ------------- | --------------- |
| `/`           | Home            |
| `/login`      | Login           |
| `/dashboard`  | Dashboard       |
| `/products`   | Product List    |
| `/products/1` | Product Details |

------------------------------------------------------------------------

# One-Line Definition

> Routing in React is the process of rendering different components
> based on the URL using **client-side routing**.