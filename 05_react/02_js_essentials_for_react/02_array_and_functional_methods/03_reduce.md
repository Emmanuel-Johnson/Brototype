# 🧠 reduce() in JavaScript

`reduce()` is an array method that:

-   Loops through the array
-   Combines all values into one single value
-   Returns that single value

That value can be:

-   A number
-   A string
-   An object
-   An array
-   Anything

------------------------------------------------------------------------

## 🟦 Basic Syntax

``` js
array.reduce((accumulator, currentValue) => {
   return updatedAccumulator;
}, initialValue);
```

### Parameters:

-   `accumulator` → stores the result
-   `currentValue` → current item
-   `initialValue` → starting value

------------------------------------------------------------------------

## 🔥 Example 1 --- Sum of Numbers

``` js
const numbers = [1, 2, 3, 4];

const total = numbers.reduce((acc, num) => {
  return acc + num;
}, 0);

console.log(total);
// 10
```

### How it works internally:

  Step   acc   num   result
  ------ ----- ----- --------
  1      0     1     1
  2      1     2     3
  3      3     3     6
  4      6     4     10

Final result → **10**

------------------------------------------------------------------------

## 🔥 Example 2 --- Count Items

``` js
const fruits = ["apple", "banana", "apple", "orange", "banana"];

const count = fruits.reduce((acc, fruit) => {
  acc[fruit] = (acc[fruit] || 0) + 1;
  return acc;
}, {});

console.log(count);
```

Output:

``` js
{
  apple: 2,
  banana: 2,
  orange: 1
}
```

This is VERY powerful.

------------------------------------------------------------------------

## 🔥 Example 3 --- Total Cart Price (Real Project Situation 👀)

``` js
const cart = [
  { name: "Shirt", price: 500 },
  { name: "Shoes", price: 1500 }
];

const totalPrice = cart.reduce((acc, item) => acc + item.price, 0);

console.log(totalPrice);
// 2000
```

You'll 100% use this in your e-commerce project.

------------------------------------------------------------------------

## 🟦 Difference Between map, filter, reduce

  Method       Purpose
  ------------ ------------------------
  `map()`      Transform every item
  `filter()`   Select some items
  `reduce()`   Combine into one value

------------------------------------------------------------------------

## 🧨 Important Rule

If you don't give `initialValue`, JS uses the first element as the
accumulator.

But best practice?\
👉 **Always provide initial value.**

------------------------------------------------------------------------

## 🎯 Simple Definition (Interview Style)

`reduce()` is an array method that executes a function on each element
to produce a single output value.