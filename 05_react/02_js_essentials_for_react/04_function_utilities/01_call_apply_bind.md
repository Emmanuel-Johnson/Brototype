# 🧠 What is `this` in JavaScript?

👉 `this` refers to the object that is calling the function.

That's the simple rule.

But... JavaScript changes behavior depending on how the function is
called. That's why people get confused.

------------------------------------------------------------------------

## 🔥 1️⃣ `this` in Global Scope

``` javascript
console.log(this);
```

In browser → `this = window`

Because `window` is the global object.

------------------------------------------------------------------------

## 🔥 2️⃣ `this` Inside an Object Method

``` javascript
const person = {
  name: "Emmanuel",
  greet: function () {
    console.log(this.name);
  }
};

person.greet();
```

### Output:

    Emmanuel

Why?

Because `person` is calling the function.

👉 `this = person`

------------------------------------------------------------------------

## 🔥 3️⃣ `this` in a Normal Function (Not Inside Object)

``` javascript
function greet() {
  console.log(this);
}

greet();
```

In browser → `this = window`

Because no object is calling it.

In strict mode → `this = undefined`

------------------------------------------------------------------------

## 🔥 4️⃣ `this` in Arrow Function ⚠️

Arrow functions DO NOT have their own `this`.

They take `this` from the surrounding scope.

Example:

``` javascript
const person = {
  name: "Emmanuel",
  greet: () => {
    console.log(this.name);
  }
};

person.greet();
```

This will NOT work like you expect.

Why?

Because arrow function takes `this` from outside (global scope).

So it won't refer to `person`.

------------------------------------------------------------------------

## 🔥 5️⃣ `this` with call()

``` javascript
function greet() {
  console.log(this.name);
}

const user = { name: "John" };

greet.call(user);
```

Here:

👉 `this = user`

Because we manually set it.

------------------------------------------------------------------------

## 🎯 Golden Rule

`this` depends on HOW a function is called.

Not where it is written.

------------------------------------------------------------------------

## 🧩 Quick Summary Table

  Situation         What is `this`?
  ----------------- ------------------------------------------
  Global scope      `window`
  Object method     That object
  Normal function   `window` (or `undefined` in strict mode)
  Arrow function    Inherits from parent
  call/apply/bind   Whatever you set

------------------------------------------------------------------------

## 🏆 One-Line Meaning

**`this` is a reference to the object that is executing the current
function.**

<br>
<br>
<br>

# 🧠 call(), apply(), bind() in JavaScript

## 🧠 First: Why Do We Need Them?

In JavaScript, `this` depends on how a function is called, not where
it's written.

Sometimes we want to manually control it.

That's where:

-   `call()`
-   `apply()`
-   `bind()`

come in.

------------------------------------------------------------------------

## 🔥 Example Setup

``` javascript
function greet() {
  console.log("Hello " + this.name);
}

const person1 = { name: "Emmanuel" };
const person2 = { name: "John" };
```

------------------------------------------------------------------------

## 📞 1️⃣ call()

`call()` runs the function immediately and lets you set `this`.

``` javascript
greet.call(person1); // Hello Emmanuel
greet.call(person2); // Hello John
```

### Syntax:

``` javascript
functionName.call(thisArg, arg1, arg2, ...)
```

------------------------------------------------------------------------

## 📦 2️⃣ apply()

Same as `call()`, but arguments are passed as an array.

``` javascript
function introduce(age, city) {
  console.log(this.name + " is " + age + " from " + city);
}

introduce.apply(person1, [22, "Kochi"]);
```

### Syntax:

``` javascript
functionName.apply(thisArg, [argsArray])
```

------------------------------------------------------------------------

## 🧷 3️⃣ bind()

`bind()` does NOT run immediately.

It returns a new function with fixed `this`.

``` javascript
const newGreet = greet.bind(person1);

newGreet(); // Hello Emmanuel
```

------------------------------------------------------------------------

## 🆚 Difference Summary

  Method    Runs Immediately?   Arguments
  --------- ------------------- ------------------
  call()    ✅ Yes              Normal arguments
  apply()   ✅ Yes              Array arguments
  bind()    ❌ No               Normal arguments

------------------------------------------------------------------------

## 🧠 Real-Life Use Case

Example in React:

``` javascript
class MyComponent extends React.Component {
  handleClick() {
    console.log(this);
  }
}
```

Sometimes `this` becomes undefined.

So we do:

``` javascript
this.handleClick = this.handleClick.bind(this);
```

That's `bind()` in real-world use.

------------------------------------------------------------------------

## 🏆 One-Line Meaning

**call, apply, and bind let you control what `this` refers to inside a
function.**