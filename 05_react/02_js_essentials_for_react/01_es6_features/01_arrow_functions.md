# 🔹 What is an Arrow Function?

An **arrow function** is a shorter way to write a function in
JavaScript.

## Old way

``` js
function greet() {
  console.log("Hello");
}
```

## Arrow way

``` js
const greet = () => {
  console.log("Hello");
};
```

Same job. Cleaner syntax.

------------------------------------------------------------------------

# 🔹 Basic Syntax

## 1️⃣ No parameters

``` js
const sayHi = () => {
  console.log("Hi");
};
```

## 2️⃣ One parameter

``` js
const greet = name => {
  console.log("Hello " + name);
};
```

👉 If only **one parameter** → no need for parentheses.

## 3️⃣ Multiple parameters

``` js
const add = (a, b) => {
  return a + b;
};
```

------------------------------------------------------------------------

# 🔹 Shorter Return (Implicit Return)

If there is only one line and only `return`, you can remove `{}` and
`return`.

``` js
const add = (a, b) => a + b;
```

🔥 This automatically returns the value.

------------------------------------------------------------------------

# 🔹 Returning an Object (Important Trick ⚠️)

If returning an object, wrap it in parentheses:

``` js
const createUser = () => ({
  name: "John",
  age: 20
});
```

Without parentheses → JavaScript thinks `{}` is a function body.

------------------------------------------------------------------------

# 🔹 Biggest Difference: `this` Behavior 🧠

## Normal function

`this` depends on how the function is called.

``` js
const person = {
  name: "John",
  greet: function() {
    console.log(this.name); // works
  }
};
```

## Arrow function

❗ Arrow functions **DO NOT** have their own `this`.

They inherit `this` from the surrounding scope.

``` js
const person = {
  name: "John",
  greet: () => {
    console.log(this.name); // undefined
  }
};
```

Because arrow function doesn't bind its own `this`.

------------------------------------------------------------------------

# 🔹 When Should You Use Arrow Functions?

✅ Callbacks
✅ Array methods (`map`, `filter`, `reduce`)
✅ Small utility functions
✅ Inside React components

## Example

``` js
const numbers = [1, 2, 3];

const doubled = numbers.map(n => n * 2);
```

------------------------------------------------------------------------

# 🔹 When NOT to Use Arrow Functions

❌ Object methods
❌ Constructor functions
❌ When you need dynamic `this`

------------------------------------------------------------------------

# 🔥 Interview Definition

Arrow function is a shorter ES6 syntax for writing functions.
It does not have its own `this`, `arguments`, or `prototype`, and is
mainly used for concise callbacks and functional programming.