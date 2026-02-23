# 🔹 What is Destructuring?

Destructuring means:

Taking values out of arrays or objects and storing them in variables ---
easily.

------------------------------------------------------------------------

Instead of doing this messy thing 👇

``` js
const user = {
  name: "John",
  age: 22
};

const name = user.name;
const age = user.age;
```

You do this 👇

``` js
const { name, age } = user;
```

Boom. Clean. Simple.

------------------------------------------------------------------------

# 🟦 1️⃣ Object Destructuring

## Basic Example

``` js
const person = {
  name: "Emma",
  age: 25,
  city: "London"
};

const { name, age } = person;

console.log(name); // Emma
console.log(age);  // 25
```

It matches by property name.

------------------------------------------------------------------------

## Rename While Destructuring

``` js
const { name: personName } = person;

console.log(personName);
```

Now variable name is `personName`.

------------------------------------------------------------------------

## Default Values

``` js
const { country = "India" } = person;
```

If `country` doesn't exist → it uses `"India"`.

------------------------------------------------------------------------

# 🟦 2️⃣ Array Destructuring

Array destructuring works by position.

``` js
const numbers = [10, 20, 30];

const [a, b] = numbers;

console.log(a); // 10
console.log(b); // 20
```

------------------------------------------------------------------------

## Skip Values

``` js
const [first, , third] = numbers;
```

Skips second value.

------------------------------------------------------------------------

## Swap Variables (Cool Trick 🔥)

``` js
let x = 5;
let y = 10;

[x, y] = [y, x];

console.log(x); // 10
console.log(y); // 5
```

Interview favorite 😎

------------------------------------------------------------------------

# 🟦 3️⃣ Destructuring in Function Parameters (VERY IMPORTANT)

Instead of:

``` js
function greet(user) {
  console.log(user.name);
}
```

We write:

``` js
function greet({ name }) {
  console.log(name);
}
```

Super clean.

------------------------------------------------------------------------

# 🟦 4️⃣ React Example (You'll See This Daily)

``` js
function User({ name, age }) {
  return <h1>{name} - {age}</h1>;
}
```

That `{ name, age }` is destructuring props.

------------------------------------------------------------------------

# 🧠 Why Destructuring is Important

✅ Cleaner code
✅ Less repetition
✅ Professional look
✅ Essential in React
✅ Used in API responses
✅ Used in hooks (`useState`)

Example:

``` js
const [count, setCount] = useState(0);
```

That is array destructuring.

------------------------------------------------------------------------

# 🔥 Interview Definition

Destructuring is an ES6 feature that allows extracting values from
arrays or properties from objects into separate variables using a
shorter syntax.