# 🔹 SPREAD OPERATOR (...)

Spread expands elements.

------------------------------------------------------------------------

# 🟦 1️⃣ Spread with Arrays

## Copy an array

``` js
const arr1 = [1, 2, 3];

const arr2 = [...arr1];

console.log(arr2); // [1, 2, 3]
```

Without spread, you'd just copy the reference.

------------------------------------------------------------------------

## Merge arrays

``` js
const a = [1, 2];
const b = [3, 4];

const combined = [...a, ...b];

console.log(combined); // [1, 2, 3, 4]
```

------------------------------------------------------------------------

# 🟦 2️⃣ Spread with Objects

``` js
const user = { name: "John", age: 22 };

const updatedUser = {
  ...user,
  age: 25
};

console.log(updatedUser);
```

Used heavily in React state updates.

------------------------------------------------------------------------

# 🟦 3️⃣ Spread in Function Call

``` js
const numbers = [5, 10, 15];

console.log(Math.max(...numbers));
```

Spreads array into individual values.

------------------------------------------------------------------------

# 🔹 REST OPERATOR (...)

Rest collects multiple values into one variable.

------------------------------------------------------------------------

# 🟦 1️⃣ Rest in Function Parameters

``` js
function add(...numbers) {
  return numbers.reduce((sum, num) => sum + num, 0);
}

console.log(add(1, 2, 3, 4)); // 10
```

All arguments are collected into an array.

------------------------------------------------------------------------

# 🟦 2️⃣ Rest in Destructuring (Arrays)

``` js
const nums = [1, 2, 3, 4];

const [first, ...rest] = nums;

console.log(first); // 1
console.log(rest);  // [2, 3, 4]
```

Rest collects remaining elements.

------------------------------------------------------------------------

# 🟦 3️⃣ Rest in Object Destructuring

``` js
const person = {
  name: "Emma",
  age: 25,
  city: "London"
};

const { name, ...details } = person;

console.log(details);
// { age: 25, city: "London" }
```

Super useful in React props handling.

------------------------------------------------------------------------

# 🧠 Spread vs Rest Difference

  Spread                         Rest
  ------------------------------ ----------------------------------
  Expands values                 Collects values
  Used when calling or copying   Used when defining
  Used in arrays/objects         Used in parameters/destructuring

Same symbol. Different job.

------------------------------------------------------------------------

# 🔥 Real React Example (Very Important)

Updating state:

``` js
setUser(prev => ({
  ...prev,
  age: 26
}));
```

If you don't use spread, you'll overwrite entire object.

This is daily React coding.

------------------------------------------------------------------------

# 🔥 Interview Definition

Spread operator expands elements of an iterable, while Rest operator
collects multiple elements into a single array. Both use `...` syntax
but behave differently based on context.