# 🪝 Rules of Hooks (React)

Hooks were introduced in React 16.8 and they come with strict rules.

There are only **2 main rules**.

Simple. But VERY important.

------------------------------------------------------------------------

# ✅ Rule 1: Only Call Hooks at the Top Level

👉 Don't call hooks inside:

-   ❌ if statements
-   ❌ loops
-   ❌ nested functions
-   ❌ try/catch blocks
-   ❌ conditions

------------------------------------------------------------------------

## ❌ Wrong

``` js
if (isLoggedIn) {
  useEffect(() => {
    console.log("Hello");
  }, []);
}
```

------------------------------------------------------------------------

## ✅ Correct

``` js
useEffect(() => {
  if (isLoggedIn) {
    console.log("Hello");
  }
}, [isLoggedIn]);
```

Notice the difference?

We moved the condition **inside** the hook.

------------------------------------------------------------------------

# 🧠 Why This Rule Exists

React tracks hooks by order of execution.

Internally it does something like:

-   Hook #1 → useState
-   Hook #2 → useEffect
-   Hook #3 → useRef

If you skip one during a render, the order breaks.

React gets confused and assigns wrong state to the wrong hook.

That's when chaos begins.

------------------------------------------------------------------------

# ✅ Rule 2: Only Call Hooks from React Functions

You can call hooks only:

-   ✅ Inside React functional components
-   ✅ Inside custom hooks

You CANNOT call hooks:

-   ❌ Inside normal JavaScript functions
-   ❌ Outside components
-   ❌ Inside class components

------------------------------------------------------------------------

## ❌ Wrong

``` js
function fetchData() {
  useEffect(() => {
    console.log("Fetching...");
  }, []);
}
```

That's just a normal function. React isn't controlling it.

------------------------------------------------------------------------

## ✅ Correct (Custom Hook)

``` js
function useFetchData() {
  useEffect(() => {
    console.log("Fetching...");
  }, []);
}
```

Notice the name starts with `use`.

That's a convention React uses to identify hooks.

------------------------------------------------------------------------

# 🎯 The Two Rules in One Line

-   Call hooks only at the top level
-   Call hooks only inside React components or custom hooks

That's it.

------------------------------------------------------------------------

# ⚠️ Bonus: ESLint Enforces This

React's official lint rules will stop you from breaking these rules.

They exist because without them, the hooks system breaks internally.

<br>
<br>
<br>

# 🧠 Why Hooks Should Not Be Used in Conditionals

## 🧠 Short Answer

Hooks should not be used in conditionals because:

React depends on the **order of hooks being the same on every render**.

If a hook is inside a condition, that order can change.

When the order changes → React assigns state incorrectly → bugs happen.

------------------------------------------------------------------------

# 🔍 What React Actually Does

Consider this component:

``` js
function Example({ show }) {
  const [count, setCount] = useState(0);

  if (show) {
    useEffect(() => {
      console.log("Hello");
    }, []);
  }

  const [name, setName] = useState("Emmanuel");

  return <div>{count}</div>;
}
```

Looks harmless, right?

Let's simulate renders.

------------------------------------------------------------------------

# 🟢 First Render (show = true)

React sees hooks in this order:

1️⃣ useState → count
2️⃣ useEffect
3️⃣ useState → name

Internally React stores:

-   Hook #1 → count state
-   Hook #2 → effect
-   Hook #3 → name state

Everything works.

------------------------------------------------------------------------

# 🔴 Second Render (show = false)

Now the condition is false.

React sees:

1️⃣ useState → count
2️⃣ useState → name

But internally React still expects:

-   Hook #1 → count
-   Hook #2 → effect
-   Hook #3 → name

React matches hooks **by position**, not by name.

Now the name state gets assigned where the effect used to be.

State becomes mismatched.

------------------------------------------------------------------------

# 🚨 What Happens Next?

You may see:

-   State switching randomly
-   Effects not running properly
-   Weird unpredictable bugs

------------------------------------------------------------------------

# 🧠 The Core Problem

Hooks are **not tracked by name**.

They are tracked by **order of execution**.

React internally assumes:

-   First hook call → first state
-   Second hook call → second state/effect
-   Third hook call → third state/ref

If one hook is skipped → everything shifts.

------------------------------------------------------------------------

# 🧠 Why Normal Functions Don't Have This Problem

Normal functions:

-   Don't preserve state between renders
-   Don't rely on call order

Hooks DO preserve state.

That's why React must keep the order stable.

------------------------------------------------------------------------

# ✅ Correct Way to Handle Conditions

Instead of:

``` js
if (show) {
  useEffect(() => {
    console.log("Hello");
  }, []);
}
```

Do this:

``` js
useEffect(() => {
  if (show) {
    console.log("Hello");
  }
}, [show]);
```

Now:

-   Hook order never changes
-   Condition is inside the hook
-   React stays happy

------------------------------------------------------------------------

# 🎯 One-Line Mental Model

Hooks must run in the same order every render.

Conditionals break that guarantee.