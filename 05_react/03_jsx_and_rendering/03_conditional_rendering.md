# 🎯 What is Conditional Rendering?

In React, **conditional rendering** means:

Showing different UI based on some condition.

Just like:

``` js
if (user) {
  showDashboard();
}
```

But in JSX, we do it differently.

------------------------------------------------------------------------

## 1️⃣ Using Ternary Operator (Most Common)

``` jsx
const isLoggedIn = true;

<h1>
  {isLoggedIn ? "Welcome Back!" : "Please Login"}
</h1>
```

If `isLoggedIn` is true → shows **"Welcome Back!"**
If false → shows **"Please Login"**

✅ Best when you have **if + else**.

------------------------------------------------------------------------

## 2️⃣ Using Logical AND (&&)

``` jsx
const isLoggedIn = true;

{isLoggedIn && <Dashboard />}
```

If `isLoggedIn` is true → `<Dashboard />` renders
If false → nothing renders

✅ Best when you only need **if (no else)**.

👉 This is called **Short-circuit evaluation**.

------------------------------------------------------------------------

## 3️⃣ Using if Statement (Outside JSX)

Sometimes it's cleaner:

``` jsx
if (!isLoggedIn) {
  return <Login />;
}

return <Dashboard />;
```

✅ Great for bigger components.

------------------------------------------------------------------------

## 4️⃣ Real World Example (eCommerce)

Imagine your cart:

``` jsx
{cartItems.length === 0 ? (
  <p>Your cart is empty</p>
) : (
  <CartItems items={cartItems} />
)}
```

This is how Amazon-style apps work internally.

------------------------------------------------------------------------

## 5️⃣ Loading State (Very Important)

You will use this in your LMS project when fetching data 👇

``` jsx
{loading ? <p>Loading...</p> : <Courses />}
```

Or:

``` jsx
{error && <p>Something went wrong</p>}
```

This is used in almost every API-based app.

------------------------------------------------------------------------

## 🚫 Why not use `if` inside JSX?

Because JSX allows only **expressions**, not **statements**.

❌ This won't work:

``` jsx
<h1>
  {if (true) { "Hello" }}
</h1>
```

------------------------------------------------------------------------

## 🧠 When To Use What?

  Situation     Use
  ------------- ---------------------
  if + else     Ternary `? :`
  Only if       `&&`
  Large logic   `if` outside return

------------------------------------------------------------------------

**Mental Rule:**
Inside `{}` → Only JavaScript expressions.