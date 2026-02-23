# 🧠 What is a Higher-Order Function?

A **higher-order function (HOF)** is a function that:

-   Takes another function as an argument
    **OR**
-   Returns another function

That's it.

If a function works with another function → it's higher-order.

------------------------------------------------------------------------

## 🟦 1️⃣ Function That Takes a Function (Very Common)

### Example:

``` js
function greet(name) {
  return "Hello " + name;
}

function processUserInput(callback) {
  const name = "Emmanuel";
  console.log(callback(name));
}

processUserInput(greet);
```

Here:

-   `processUserInput` takes `greet` as an argument
-   So `processUserInput` is a higher-order function

------------------------------------------------------------------------

## 🟦 2️⃣ Function That Returns a Function

``` js
function multiplyBy(x) {
  return function(y) {
    return x * y;
  };
}

const double = multiplyBy(2);

console.log(double(5)); 
// 10
```

Here:

-   `multiplyBy` returns another function
-   So it's a higher-order function

This concept is used a LOT in advanced JS and React.

------------------------------------------------------------------------

## 🔥 Real Examples You Already Know

These are all higher-order functions:

-   `map()`
-   `filter()`
-   `reduce()`
-   `forEach()`
-   `setTimeout()`

Example:

``` js
[1, 2, 3].map(num => num * 2);
```

`map()` takes a function → so it's higher-order.

------------------------------------------------------------------------

## 🧠 Why Is This Powerful?

Because functions become:

-   Reusable
-   Flexible
-   More dynamic
-   More functional programming style

This is what makes JavaScript powerful.

------------------------------------------------------------------------

## 🎯 Simple Definition (Interview Style)

A higher-order function is a function that either accepts another
function as an argument or returns a function.