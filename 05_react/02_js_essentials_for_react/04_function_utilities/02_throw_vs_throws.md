# 🧨 throw in JavaScript

In JavaScript, we use:

`throw`

Not `throws`.

------------------------------------------------------------------------

## 🔥 Example

``` javascript
function divide(a, b) {
  if (b === 0) {
    throw new Error("Cannot divide by zero");
  }
  return a / b;
}

try {
  divide(10, 0);
} catch (error) {
  console.log(error.message);
}
```

### What happens?

-   `throw` creates an error
-   Execution stops immediately
-   Control goes to `catch`

👉 `throw` = manually create an error

------------------------------------------------------------------------

## 🤔 Then What is `throws`?

`throws` is NOT used in JavaScript.

You might see it in:

-   Java ☕
-   C#
-   TypeScript (in documentation sometimes)

### Example in Java:

``` java
public void readFile() throws IOException {
```

In Java:

`throws` declares that a function may throw an error.
It's part of the method signature.

But in JavaScript ❌ we don't use `throws`.

------------------------------------------------------------------------

## 🧠 Key Difference

  Word     Language        Meaning
  -------- --------------- --------------------------
  throw    JavaScript      Actually create an error
  throws   Java / others   Declare possible error

------------------------------------------------------------------------

## 🚀 Important JavaScript Rule

In JS, you just:

``` javascript
throw new Error("Something went wrong");
```

And handle it with:

``` javascript
try { 
  // code 
} catch (error) { 
  // handle error 
}
```

That's it.

------------------------------------------------------------------------

## 🏆 One-Line Answer

**`throw` is used in JavaScript to raise an error.
`throws` is not used in JavaScript.**