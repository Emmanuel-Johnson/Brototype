# What is a Promise in JavaScript?

A **Promise** is an object that represents a value that will come later.

That's it.

It's like saying:

> "I promise I'll give you the result... but not right now."

------------------------------------------------------------------------

## 🍕 Real-Life Example

You order food from Zomato.

-   You place order → you don't get food immediately
-   It takes time to prepare

After some time:

✅ You get food (success)
❌ Or restaurant cancels (failure)

That waiting + future result = **Promise**

------------------------------------------------------------------------

## 🧠 Why Do We Need Promises?

Because JavaScript does not wait for slow things like:

-   API calls
-   Database requests
-   File reading
-   `setTimeout`

If JS waited, the whole program would freeze.

Promises help us say:

> "When the work is finished, THEN do this."

------------------------------------------------------------------------

## 🔥 Basic Example

``` javascript
const myPromise = new Promise((resolve, reject) => {
  let success = true;

  if (success) {
    resolve("Task completed!");
  } else {
    reject("Task failed!");
  }
});

myPromise
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.log(error);
  });
```

------------------------------------------------------------------------

## 🧩 Promise Has 3 States

-   **Pending** → waiting
-   **Fulfilled** → success
-   **Rejected** → failed

------------------------------------------------------------------------

## ⚡ Why Not Just Use Normal Code?

### ❌ Without Promise:

``` javascript
const data = fetch("api-url");
console.log(data);
```

**Problem:**

-   `fetch()` takes time.
-   `console.log` runs immediately.
-   You get incomplete result.

------------------------------------------------------------------------

### ✅ With Promise:

``` javascript
fetch("api-url")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

Now JS says:

> "Okay, when fetch finishes... THEN print the data."

------------------------------------------------------------------------

## 🏆 Simple One-Line Meaning

A Promise is a cleaner way to handle asynchronous work in JavaScript.