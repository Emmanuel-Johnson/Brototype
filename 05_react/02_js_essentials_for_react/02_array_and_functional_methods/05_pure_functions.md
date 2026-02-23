# 🧠 What is a Pure Function?

A **pure function** is a function that:

✅ Always returns the same output for the same input
✅ Has no side effects

That's it.

------------------------------------------------------------------------

## 🟦 Rule 1: Same Input → Same Output

``` js
function add(a, b) {
  return a + b;
}

add(2, 3); // 5
add(2, 3); // 5
add(2, 3); // 5
```

Always **5**.

This is PURE ✅

------------------------------------------------------------------------

## 🟦 Rule 2: No Side Effects

A side effect means:

-   Changing a global variable
-   Modifying an external object
-   Making API calls
-   Changing DOM
-   Console logging (technically a side effect)

### Example of NOT pure:

``` js
let total = 0;

function addToTotal(num) {
  total += num;   // modifies external variable ❌
}
```

This is NOT pure.

------------------------------------------------------------------------

## 🟦 Example of Impure Function

``` js
let count = 0;

function increment() {
  count++;
  return count;
}
```

Call it multiple times:

``` js
increment(); // 1
increment(); // 2
increment(); // 3
```

Same input (none), different output ❌

So it's impure.

------------------------------------------------------------------------

## 🟦 Pure Version of That

``` js
function increment(count) {
  return count + 1;
}
```

Now:

``` js
increment(0); // 1
increment(0); // 1
```

Predictable ✅

------------------------------------------------------------------------

## 🔥 Why Pure Functions Matter (Especially for You 👀)

In:

-   React
-   Redux
-   Functional programming
-   Backend logic

Pure functions:

-   Are easier to test
-   Are easier to debug
-   Avoid hidden bugs
-   Make your app predictable

React components ideally behave like pure functions:
Same props → same UI.

------------------------------------------------------------------------

## 🧠 Quick Comparison

  Pure              Impure
  ----------------- ------------------
  Predictable       Unpredictable
  No side effects   Has side effects
  Easier to test    Harder to test

------------------------------------------------------------------------

## 🎯 Interview Definition

A pure function is a function that always returns the same output for
the same input and does not cause any side effects.