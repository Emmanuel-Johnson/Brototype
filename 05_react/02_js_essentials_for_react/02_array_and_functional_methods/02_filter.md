# 🧠 filter() in JavaScript

`filter()` is an array method that:

-   Loops through each element
-   Checks a condition
-   Returns a **new array** with only the elements that pass the
    condition
-   Does **NOT** change the original array

------------------------------------------------------------------------

## 🟦 Basic Syntax

``` js
array.filter((item, index) => {
   return condition;
});
```

👉 The function must return **true or false**

-   `true` → keep the item
-   `false` → remove it

------------------------------------------------------------------------

## 🟦 Simple Example

``` js
const numbers = [1, 2, 3, 4, 5];

const evenNumbers = numbers.filter(num => num % 2 === 0);

console.log(evenNumbers);
// [2, 4]
```

What happened?

    1 ❌
    2 ✅
    3 ❌
    4 ✅
    5 ❌

Only even numbers stayed.

Original array is still:

    [1, 2, 3, 4, 5]

------------------------------------------------------------------------

## 🟦 With Objects (Very Important for Your Projects 🚀)

``` js
const users = [
  { name: "John", age: 22 },
  { name: "Anna", age: 25 },
  { name: "Mike", age: 18 }
];

const adults = users.filter(user => user.age >= 21);

console.log(adults);
```

Output:

``` js
[
  { name: "John", age: 22 },
  { name: "Anna", age: 25 }
]
```

This is exactly how you'll filter:

-   Products by category
-   Users by role
-   Orders by status

in your LMS & e-commerce app 🔥

------------------------------------------------------------------------

## 🟦 Difference: map() vs filter()

  map()                       filter()
  --------------------------- ---------------------------------
  Transforms data             Selects data
  Returns same length array   Returns smaller or equal length
  Always returns something    Returns only matching items

Example:

``` js
numbers.map(n => n * 2);     // transforms
numbers.filter(n => n > 2);  // selects
```

------------------------------------------------------------------------

## 🧨 Common Mistake

Forgetting to return:

``` js
const result = numbers.filter(num => {
   num > 2;  // ❌ no return
});
```

This gives:

    []

Correct:

``` js
const result = numbers.filter(num => num > 2);
```

------------------------------------------------------------------------

## 🎯 Simple Definition (Interview Style)

`filter()` is an array method that creates a new array containing only
the elements that satisfy a given condition.