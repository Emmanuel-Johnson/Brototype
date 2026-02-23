# 🔹 What is Optional Chaining?

Optional chaining uses:

`?.`

It safely accesses nested properties without crashing if something is
`null` or `undefined`.

------------------------------------------------------------------------

# 🧨 The Problem (Without Optional Chaining)

``` js
const user = {};

console.log(user.address.city);
```

❌ Error:

Cannot read property 'city' of undefined

Because `address` doesn't exist.

------------------------------------------------------------------------

# ✅ The Solution (With Optional Chaining)

``` js
console.log(user.address?.city);
```

Now:

-   If `address` exists → it gives `city`
-   If `address` is `undefined` → it returns `undefined`
-   No crash

Clean. Safe. Professional.

------------------------------------------------------------------------

# 🟦 1️⃣ Nested Objects Example

``` js
const user = {
  name: "John",
  address: {
    city: "London"
  }
};

console.log(user.address?.city); // London
```

If `address` was missing → no error.

------------------------------------------------------------------------

# 🟦 2️⃣ API Response Example (Very Important)

Imagine backend sends:

``` js
const response = {
  data: {
    user: {
      profile: {
        avatar: "image.jpg"
      }
    }
  }
};
```

Instead of writing this:

``` js
response &&
response.data &&
response.data.user &&
response.data.user.profile &&
response.data.user.profile.avatar
```

We write:

``` js
response.data?.user?.profile?.avatar
```

Much cleaner.

------------------------------------------------------------------------

# 🟦 3️⃣ Optional Chaining with Arrays

``` js
const users = null;

console.log(users?.[0]);
```

If `users` is `null` → no crash.

------------------------------------------------------------------------

# 🟦 4️⃣ Optional Chaining with Functions

``` js
const user = {
  greet() {
    console.log("Hello");
  }
};

user.greet?.();
```

-   If `greet` exists → it runs
-   If not → no error

------------------------------------------------------------------------

# 🔹 Optional Chaining + Nullish Coalescing (Power Combo 🔥)

Sometimes you want a default value.

``` js
const city = user.address?.city ?? "Unknown";
```

If `city` is `undefined` or `null` → `"Unknown"`

This is used a LOT in React UI.

------------------------------------------------------------------------

# 🧠 When Should You Use It?

✅ API responses
✅ Deep nested objects
✅ Optional props in React
✅ When data may not exist yet

Example in React:

``` js
return <p>{user?.name}</p>;
```

If `user` is still loading → no crash.

------------------------------------------------------------------------

# 🔥 Interview Definition

Optional chaining (`?.`) is an ES2020 feature that allows safe access to
nested object properties without throwing errors if an intermediate
property is `null` or `undefined`.