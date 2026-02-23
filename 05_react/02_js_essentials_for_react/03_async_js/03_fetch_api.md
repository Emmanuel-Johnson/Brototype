# 🌍 What is Fetch API?

Fetch API is a built-in JavaScript function used to make HTTP requests.

Basically:

It helps your frontend talk to a server.

For example:

-   React → Django API
-   Browser → Backend
-   Website → Database (through API)

------------------------------------------------------------------------

## 🧠 Very Simple Meaning

`fetch()` = "Go get me data from this URL."

------------------------------------------------------------------------

## 🔥 Basic Example

``` javascript
fetch("https://jsonplaceholder.typicode.com/todos/1")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error));
```

### What's happening?

-   `fetch()` sends request
-   It returns a **Promise**
-   When response comes → `.then()` runs
-   If error → `.catch()` runs

------------------------------------------------------------------------

## 🚀 Same Thing Using async/await (Cleaner)

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

Much easier to read, right?

------------------------------------------------------------------------

## 🧩 Important: Fetch Has 2 Steps

Many beginners miss this 👇

### Step 1 --- Fetch the response

``` javascript
const response = await fetch(url);
```

### Step 2 --- Convert to JSON

``` javascript
const data = await response.json();
```

Because the response body also comes as a Promise.

------------------------------------------------------------------------

## ⚠️ Important Thing Most People Don't Know

`fetch()` only rejects if:

-   Network fails
-   No internet

If server returns:

-   404
-   500

It **DOES NOT automatically throw error.**

You must check:

``` javascript
if (!response.ok) {
  throw new Error("Something went wrong");
}
```

------------------------------------------------------------------------

## 🧠 Real Example (Like You'll Do in React + Django)

``` javascript
async function getProducts() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/products/");

    if (!response.ok) {
      throw new Error("Failed to fetch products");
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

This is exactly what you'll do in your e-commerce project.

------------------------------------------------------------------------

## 🎯 Why Fetch Is Important For You

Since you're building:

-   LMS
-   E-commerce
-   Django REST Framework API
-   React frontend

Fetch (or axios) is the bridge between them.

Without fetch → frontend can't get backend data.

------------------------------------------------------------------------

## 🏆 One-Line Meaning

**Fetch API is how JavaScript talks to servers using HTTP requests.**