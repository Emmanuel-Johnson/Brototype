# 🧠 useContext in React

`useContext` is a React Hook that lets you access global/shared state
without passing props manually through every component (aka **prop
drilling**).

Think of it like:

> "I don't want to pass this value through 5 components. Just give it
> directly where I need it."

------------------------------------------------------------------------

## 🚫 The Problem (Prop Drilling)

Without context:

    App → Layout → Sidebar → Profile → Avatar

If `Avatar` needs `user`, you'd have to pass it through every component.

That gets annoying fast.

------------------------------------------------------------------------

## ✅ The Solution: Context API + useContext

There are 3 steps:

### 1️⃣ Create Context

``` js
import { createContext } from "react";

export const UserContext = createContext();
```

### 2️⃣ Provide the Value

Wrap the part of your app that needs access.

``` js
import { UserContext } from "./UserContext";

function App() {
  const user = { name: "Emmanuel" };

  return (
    <UserContext.Provider value={user}>
      <Profile />
    </UserContext.Provider>
  );
}
```

Now every child inside `Provider` can access `user`.

### 3️⃣ Use the Context

``` js
import { useContext } from "react";
import { UserContext } from "./UserContext";

function Profile() {
  const user = useContext(UserContext);

  return <h1>Hello {user.name}</h1>;
}
```

Boom 💥 No prop drilling.

------------------------------------------------------------------------

# 🔥 Real Example (Theme Toggle)

``` js
import { createContext, useState, useContext } from "react";

const ThemeContext = createContext();

function App() {
  const [theme, setTheme] = useState("light");

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      <Navbar />
    </ThemeContext.Provider>
  );
}

function Navbar() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button onClick={() => setTheme("dark")}>
      Current theme: {theme}
    </button>
  );
}
```

------------------------------------------------------------------------

# 🎯 When to Use useContext

## ✅ Good for:

-   Theme (dark/light mode)
-   Auth user
-   Language
-   Global settings
-   Small--medium global state

## ❌ Not Ideal for:

-   Very complex state logic
-   Heavy state updates across large apps (Redux / Zustand better)

------------------------------------------------------------------------

# 🚀 For LMS & E-Commerce Projects

You'll likely use `useContext` for:

-   Auth user
-   Cart context
-   Theme

Later, when state logic grows, you can move to Redux Toolkit.