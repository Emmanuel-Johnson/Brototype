# 🔹 What is an IIFE?

IIFE = Immediately Invoked Function Expression

It's a function that:

-   Is defined
-   And runs immediately
-   All in one go

------------------------------------------------------------------------

# 🟦 Basic Syntax

``` js
(function () {
  console.log("Hello");
})();
```

It runs instantly.

No need to call it separately.

------------------------------------------------------------------------

# 🟦 With Arrow Function

``` js
(() => {
  console.log("Hello");
})();
```

Modern style.

------------------------------------------------------------------------

# 🔹 Why Do We Use IIFE?

Main reason:

👉 To create a private scope

Before ES6 (before `let` and `const`), we only had `var`.

`var` had global scope problems.

So developers used IIFE to avoid polluting the global scope.

------------------------------------------------------------------------

# 🧨 Problem Without IIFE

``` js
var name = "John";

function greet() {
  console.log(name);
}
```

`name` is global. Anyone can change it.

------------------------------------------------------------------------

# ✅ Using IIFE to Protect Variables

``` js
(function () {
  var secret = "Hidden";

  console.log(secret);
})();

console.log(secret); // ❌ Error
```

Now `secret` is private.

------------------------------------------------------------------------

# 🔹 How It Works (Important Concept)

Normally:

``` js
function greet() {}
```

This is a **function declaration**.

But IIFE must be a **function expression**.

That's why we wrap it in parentheses:

``` js
(function() {})
```

The parentheses force JavaScript to treat it as an expression.

Then:

``` js
()
```

Calls it immediately.

------------------------------------------------------------------------

# 🔹 IIFE With Parameters

``` js
(function (name) {
  console.log("Hello " + name);
})("John");
```

Runs instantly with argument.

------------------------------------------------------------------------

# 🔹 Real-World Usage

Before ES6 modules:

-   Used in libraries
-   Used to avoid global variable conflicts
-   Used in old jQuery code

Example (old style):

``` js
(function () {
  // all code here is private
})();
```

------------------------------------------------------------------------

# 🔹 Is IIFE Still Used Today?

Less common now because we have:

-   `let` and `const`
-   ES Modules (`import` / `export`)
-   Block scope `{ }`

Modern replacement:

``` js
{
  let secret = "hidden";
}
```

But you should know IIFE for:

-   Interviews
-   Understanding old code
-   Understanding scope deeply

------------------------------------------------------------------------

# 🔥 Interview Definition

An IIFE (Immediately Invoked Function Expression) is a function that is
defined and executed immediately after its creation, mainly used to
create a private scope and avoid polluting the global namespace.