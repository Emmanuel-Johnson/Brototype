# 🧠 Hooks vs Normal Functions

At first glance, hooks look like functions.

    useState()
    useEffect()
    useRef()

So... are they just functions?

👉 Technically: Yes.
👉 Conceptually: No.

Let's break it down.

------------------------------------------------------------------------

# 1️⃣ What Is a Normal JavaScript Function?

A normal function:

-   Can be called anywhere
-   Has no special rules
-   Just runs and returns something

Example:

``` js
function add(a, b) {
  return a + b;
}
```

You can call it:

-   Inside loops
-   Inside conditions
-   Anywhere

No restrictions.

------------------------------------------------------------------------

# 2️⃣ What Is a Hook?

A hook is a special React function that:

-   Connects your component to React's internal system
-   Stores data between renders
-   Tells React when to re-render

Example:

``` js
const [count, setCount] = useState(0);
```

This is not just returning a value.

It is:

-   Registering state inside React
-   Linking it to THIS component instance
-   Tracking updates
-   Triggering re-renders

That's way beyond a normal function.

------------------------------------------------------------------------

# 🚨 The BIG Difference

  Normal Function             Hook
  --------------------------- ---------------------------------
  Just executes               Connects to React internals
  No rules                    Must follow Rules of Hooks
  No memory between renders   Preserves state between renders
  Doesn't trigger re-render   Can trigger re-render

------------------------------------------------------------------------

# 🔥 Example That Shows the Difference

## ❌ Normal Function

``` js
function counter() {
  let count = 0;
  count++;
  return count;
}
```

Every time the component renders → `count` resets to `0`.

No persistence.

------------------------------------------------------------------------

## ✅ useState Hook

``` js
const [count, setCount] = useState(0);
```

Even after re-render → value persists.

That's because React stores it internally.

------------------------------------------------------------------------

# 🧩 Why Hooks Have Rules (Normal Functions Don't)

Hooks depend on call order.

React internally tracks something like:

-   Hook #1 → state
-   Hook #2 → effect
-   Hook #3 → ref

If you put a hook inside an `if` statement, the order changes.

React gets confused.

Normal functions don't care about call order.

Hooks DO.

------------------------------------------------------------------------

# 🧠 Super Clear Mental Model

Normal function = Calculator

Hook = Plugging into React's brain

Hooks talk to React's engine.
Normal functions don't.