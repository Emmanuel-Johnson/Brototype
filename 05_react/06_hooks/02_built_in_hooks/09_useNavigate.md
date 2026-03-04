# React Router `useNavigate` Guide

## What is `useNavigate`?

In React Router, **`useNavigate`** is a hook used to programmatically
change routes (navigate to another page).

Think of it like:

👉 **"Move the user to another URL using JavaScript."**

---

## Basic Example

```jsx
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  const goToAbout = () => {
    navigate("/about");
  };

  return (
    <div>
      <button onClick={goToAbout}>Go to About</button>
    </div>
  );
}
```

### What happens here

- `useNavigate()` gives a **navigate function**.
- Calling `navigate("/about")` changes the route to `/about`.
- React Router loads the **About page component**.

---

## Direct Navigation

You can also navigate directly inside JSX.

```jsx
<button onClick={() => navigate("/login")}>Go to Login</button>
```

---

## Navigate with Replace

```javascript
navigate("/dashboard", { replace: true });
```

This **replaces the current history** instead of adding a new one.

### Meaning

Normal navigation:

    Login → Dashboard

Pressing **Back** goes to **Login**.

With replace:

    Login → Dashboard (replace)

Pressing **Back** will **NOT go back to Login**.

### Example Use Case

After login, you usually **don't want the user to go back to the login
page**.

---

## Navigate Back / Forward

```javascript
navigate(-1); // go back
navigate(1); // go forward
```

This works exactly like **browser history navigation**.

Example:

    Home → About → Contact

`navigate(-1)` → goes to **About**.

---

## Real Example (Login Redirect)

```javascript
const navigate = useNavigate();

const handleLogin = () => {
  // after login success
  navigate("/dashboard");
};
```

---

## Quick Summary

Code Meaning

---

`useNavigate()` get navigate function
`navigate("/about")` go to about page
`navigate(-1)` go back
`navigate("/home", { replace: true })` replace history

---

## Real Use Cases in Projects

Since you're building **LMS and E-commerce projects**, `useNavigate` is
commonly used for:

- Redirect after login
- Redirect after form submission
- Redirect after adding items to cart
- Redirect after payment success

<br>
<br>
<br>

# React Router `useNavigate` Explanation

`useNavigate()` just moves the user to a path, but that path must
already exist in your **Router configuration**.

---

# 1️⃣ Example Router Setup

Suppose you defined routes like this in **App.jsx**:

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./Home";
import About from "./About";

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

Here we defined:

    path="/about"

So React Router knows:

    /about → render About component

---

# 2️⃣ Your `navigate("/about")`

In **Home.jsx**:

```javascript
const navigate = useNavigate();

const goToAbout = () => {
  navigate("/about");
};
```

When the button is clicked:

    navigate("/about")

React Router checks the routes and finds:

```jsx
<Route path="/about" element={<About />} />
```

Then it loads the **About component**.

---

# 3️⃣ Folder Structure Example

    src
     ├── App.jsx
     ├── Home.jsx
     ├── About.jsx

---

# 4️⃣ Simple Flow

    Button click
         ↓
    navigate("/about")
         ↓
    React Router checks routes
         ↓
    path="/about"
         ↓
    About component renders

---

# ⚡ Small Tip (Important for Interviews)

`useNavigate()` is used for **programmatic navigation**.

### Example Uses

- After login → redirect to dashboard
- After form submit → redirect to success page
- Button click navigation

---

Since you're in **Brototype week 22 and learning React**, this is a very
common pattern.

Once you build your **LMS or e-commerce project**, you'll use this for
things like:

```javascript
navigate("/login");
navigate("/cart");
navigate("/product/123");
```

<br>
<br>
<br>

# React Router Navigation Methods

## 1️⃣ `<Link>` (Most common for UI navigation)

Use `<Link>` when you want users to click a link to go to another page.

It works like an HTML `<a>` tag, but **without a full page reload**.

### Example

```jsx
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <Link to="/about">Go to About</Link>
    </div>
  );
}
```

### What happens

    User clicks link
         ↓
    URL changes to /about
         ↓
    About component renders

### When to use

Use `<Link>` for:

- Navbar
- Sidebar
- Menu
- Normal page links

Example in real apps:

    Home | Products | Cart | Login

---

## 2️⃣ `useNavigate()` (Programmatic navigation)

Use this when navigation happens because of **logic**, not just clicking
a link.

### Examples

- Login success → go to dashboard
- Form submit → go to success page
- Button click → go somewhere

### Example

```jsx
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  const goToAbout = () => {
    navigate("/about");
  };

  return <button onClick={goToAbout}>Go to About</button>;
}
```

### What happens

    Button click
         ↓
    navigate("/about")
         ↓
    Router loads About page

---

## 3️⃣ `<Navigate />` (Automatic redirect)

Used when you want **automatic redirection**.

### Examples

- User not logged in → redirect to login
- After logout → redirect to home

### Example

```jsx
import { Navigate } from "react-router-dom";

function Dashboard({ isLoggedIn }) {
  if (!isLoggedIn) {
    return <Navigate to="/login" />;
  }

  return <h1>Dashboard</h1>;
}
```

### What happens

    User tries to open Dashboard
         ↓
    Check login
         ↓
    Not logged in
         ↓
    Redirect to /login

---

# ⚡ Super Simple Comparison

Method Use Case

---

`<Link>` User clicks navigation link
`useNavigate()` Navigate using logic / functions
`<Navigate />` Automatic redirect

---

# 🧠 Easy way to remember

    <Link>        → Click navigation
    useNavigate() → Function navigation
    <Navigate/>   → Redirect navigation
