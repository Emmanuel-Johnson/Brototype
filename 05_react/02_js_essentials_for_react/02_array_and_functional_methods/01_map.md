# 🧠 map() in JavaScript

`map()` is an array method.

It:

-   Goes through each item in an array
-   Applies a function to each item
-   Returns a **new array**
-   Does **NOT** change the original array

------------------------------------------------------------------------

## 🟦 Basic Syntax

``` js
array.map((item, index) => {
   return something;
});
```

-   `item` → current element
-   `index` → position (optional)

It **must return something**, because it builds a new array.

------------------------------------------------------------------------

## 🟦 Simple Example

``` js
const numbers = [1, 2, 3, 4];

const doubled = numbers.map(num => num * 2);

console.log(doubled);
// [2, 4, 6, 8]
```

Original array:

    [1, 2, 3, 4]

New array:

    [2, 4, 6, 8]

-   `numbers` is still `[1, 2, 3, 4]`
-   `doubled` is a new array

------------------------------------------------------------------------

## 🟦 With Objects (Very Important for React 🚀)

``` js
const users = [
  { name: "John", age: 22 },
  { name: "Anna", age: 25 }
];

const names = users.map(user => user.name);

console.log(names);
// ["John", "Anna"]
```

This is super common in React when rendering lists.

------------------------------------------------------------------------

## 🟦 In React (Used Daily in LMS & E-commerce Projects 👀)

``` jsx
{products.map(product => (
  <div key={product.id}>
    {product.name}
  </div>
))}
```

This is how we render dynamic UI.

------------------------------------------------------------------------

## 🟦 Important Difference

  Method        Returns New Array?   Changes Original?
  ------------- -------------------- -------------------
  `map()`       ✅ Yes               ❌ No
  `forEach()`   ❌ No                ❌ No (usually)

-   `map()` → for transforming data
-   `forEach()` → for doing something (like logging)

------------------------------------------------------------------------

## 🧨 Common Mistake

Forgetting `return`:

``` js
const result = numbers.map(num => {
   num * 2;   // ❌ No return
});
```

This gives:

    [undefined, undefined, undefined, undefined]

Correct:

``` js
const result = numbers.map(num => num * 2);
```

------------------------------------------------------------------------

## 🎯 Simple Definition (Exam Style)

`map()` is an array method that creates a new array by applying a
function to each element of the original array.