# 🛠️ What is a Transpiler?

A transpiler is a tool that converts code from:

One version of a language
↓
Another version of the SAME language

That's it.

It's like a translator between dialects of the same language.

------------------------------------------------------------------------

# 🧠 Simple Definition (Interview Style)

A transpiler converts modern code into older compatible code without
changing the language.

------------------------------------------------------------------------

# 🔥 Real Example (JavaScript)

You write modern JS:

``` js
const greet = () => {
  console.log("Hello");
};
```

Old browsers don't understand arrow functions.

A transpiler converts it to:

``` js
var greet = function() {
  console.log("Hello");
};
```

Still JavaScript.
Just older style.

------------------------------------------------------------------------

# 🧩 Why "Trans" + "Compiler"?

Compiler → converts language A → language B

Transpiler → converts language A → A (but different version)

That's why it's called a **source-to-source compiler**.

------------------------------------------------------------------------

# 🌍 Popular Transpilers

## 🔹 Babel

-   ES6+ → ES5
-   JSX → JavaScript
-   TypeScript → JavaScript

## 🔹 TypeScript compiler (tsc)

-   TypeScript → JavaScript

## 🔹 SWC

-   Fast JS/TS transpiler (written in Rust)

## 🔹 esbuild

-   Extremely fast transpiler + bundler

------------------------------------------------------------------------

# 🖼️ How It Fits in Your React Project

When you write:

``` jsx
<h1>Hello</h1>
```

Browser does NOT understand JSX.

So transpiler converts it into:

``` js
React.createElement("h1", null, "Hello")
```

Then browser can run it.

------------------------------------------------------------------------

# ⚙️ Transpiler vs Compiler vs Bundler

  Tool         What it does
  ------------ -----------------------------------------------------
  Transpiler   Converts same language to older/newer version
  Compiler     Converts one language to another (C → Machine code)
  Bundler      Combines many files into fewer optimized files

------------------------------------------------------------------------

# 🎯 Why It Matters

In your:

-   LMS
-   E-commerce

You write modern React code.

Without transpiler:

-   Old browsers break
-   JSX won't work
-   TypeScript won't work

Transpiler makes your modern dev experience possible.

------------------------------------------------------------------------

# 🧠 Quick Analogy

You speak modern English slang.

Transpiler converts it into:
Formal English so everyone understands.

Same meaning. Different style.