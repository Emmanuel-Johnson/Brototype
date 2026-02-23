# What is async / await?

👉 **async / await is just a nicer way to write Promises.**

It does NOT replace promises.
It uses promises behind the scenes.

------------------------------------------------------------------------

## 🧠 What does `async` do?

When you put `async` before a function:

``` javascript
async function hello() {
  return "Hi";
}
```

That function automatically returns a **Promise**.

So this:

``` javascript
hello();
```

Is actually:

    Promise { "Hi" }

Even if you return a normal value, JavaScript wraps it inside a Promise.

------------------------------------------------------------------------

## 🧠 What does `await` do?

`await` means:

> "Wait here until this promise finishes... then continue."

⚠️ Important: It only works inside `async` functions.

------------------------------------------------------------------------

## 🔥 Without async/await (Using .then)

``` javascript
fetch("https://jsonplaceholder.typicode.com/todos/1")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

Works fine.

But it can become messy if you have many steps.

------------------------------------------------------------------------

## 😌 With async/await (Cleaner)

``` javascript
async function getData() {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.log(error);
  }
}

getData();
```

Much cleaner, right?

It looks synchronous...
but it's still asynchronous.

------------------------------------------------------------------------

## 🤯 Does `await` block JavaScript?

No.

It pauses only that async function,
not the entire program.

Example:

``` javascript
async function test() {
  console.log("Start");

  await new Promise(resolve => setTimeout(resolve, 2000));

  console.log("End");
}

test();
console.log("Outside");
```

### Output:

    Start
    Outside
    End

See?

JavaScript didn't freeze.

------------------------------------------------------------------------

## 🧩 Simple Mental Model

-   **Promise** = "I will give you result later."
-   **await** = "Okay... I'll wait for you."
-   **async** = "This function works with promises."

------------------------------------------------------------------------

## 🏆 One-Line Definition

**async/await is syntax sugar that makes promise-based code look like
normal synchronous code.**