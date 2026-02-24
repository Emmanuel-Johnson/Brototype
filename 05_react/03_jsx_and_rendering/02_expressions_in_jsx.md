# 🧠 What Are Expressions in JSX?

In React, you can write **JavaScript expressions** inside `{ }`.

Think of `{ }` as:

> "Hey React, evaluate this JavaScript."

------------------------------------------------------------------------

## ✅ Basic Example

``` jsx
const name = "Emmanuel";

<h1>Hello {name}</h1>
```

**Output:**

    Hello Emmanuel

React evaluates `name` and inserts the value.

------------------------------------------------------------------------

## 🔢 1️⃣ Arithmetic Expressions

``` jsx
<h1>{5 + 5}</h1>
```

**Output:**

    10

You can even do:

``` jsx
const age = 20;

<h1>Next year: {age + 1}</h1>
```

------------------------------------------------------------------------

## 🔁 2️⃣ Ternary (Conditional Rendering)

This is VERY common in React 👇

``` jsx
const isLoggedIn = true;

<h1>{isLoggedIn ? "Welcome" : "Please Login"}</h1>
```

React will show:

    Welcome

⚠ You cannot use `if` directly inside JSX.

❌ Wrong:

``` jsx
<h1>{if (true) { "Yes" }}</h1>
```

Because `if` is a **statement**, not an **expression**.

------------------------------------------------------------------------

## 🧩 3️⃣ Function Calls

You can call functions inside `{}`:

``` jsx
function greet(name) {
  return "Hello " + name;
}

<h1>{greet("Emmanuel")}</h1>
```

**Output:**

    Hello Emmanuel

------------------------------------------------------------------------

## 📦 4️⃣ Rendering Lists (Very Important)

``` jsx
const numbers = [1, 2, 3];

<ul>
  {numbers.map(num => (
    <li key={num}>{num}</li>
  ))}
</ul>
```

Here:

-   `map()` is a JavaScript expression
-   React renders multiple elements
-   This is how **dynamic lists** are built in real apps

------------------------------------------------------------------------

## 🚫 What You CANNOT Put Inside `{}`

You cannot put:

-   `if`
-   `for`
-   `while`
-   `switch`

Because they are **statements**, not expressions.

------------------------------------------------------------------------

## ✅ What You CAN Use Inside `{}`

-   Ternary operator (`condition ? true : false`)
-   `&&` (short-circuit rendering)
-   `.map()`
-   Function calls
-   Arithmetic expressions
-   Variables

------------------------------------------------------------------------

## ⚡ Short-Circuit Trick (Very Common)

``` jsx
{isLoggedIn && <Dashboard />}
```

If `isLoggedIn` is `true` → it renders `<Dashboard />`
If `false` → nothing renders.

------------------------------------------------------------------------

## 🧠 Mental Rule

-   Inside `{}` → Only **JavaScript expressions**
-   Outside `{}` → Normal JSX / HTML-like syntax