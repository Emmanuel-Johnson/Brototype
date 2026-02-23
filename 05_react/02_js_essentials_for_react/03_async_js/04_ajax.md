# 🌐 What is AJAX?

AJAX stands for:

**Asynchronous JavaScript And XML**

But don't get confused by "XML".
Today we mostly use **JSON**, not XML.

------------------------------------------------------------------------

## 🧠 Simple Meaning

AJAX =
👉 "Send request to server without refreshing the page."

That's it.

------------------------------------------------------------------------

## 🤯 Why AJAX Was Important?

### Before AJAX:

-   You click a button
-   Page reloads
-   Whole website refreshes

### After AJAX:

-   Click button
-   Only small data updates
-   No page refresh

That's why websites became smooth and fast.

------------------------------------------------------------------------

## 🏗 Real Example

Think about:

-   Instagram likes ❤️
-   Amazon cart update 🛒
-   Chat messages 💬

Page doesn't reload, right?

That's AJAX concept.

------------------------------------------------------------------------

## 🛠 How AJAX Was Done Earlier (Old Way)

Before `fetch`, developers used:

**XMLHttpRequest**

``` javascript
const xhr = new XMLHttpRequest();

xhr.open("GET", "https://jsonplaceholder.typicode.com/todos/1");

xhr.onload = function () {
  console.log(JSON.parse(xhr.responseText));
};

xhr.send();
```

This is AJAX.

But it's messy 😅

------------------------------------------------------------------------

## 🚀 Modern Version of AJAX

Today we use:

-   `fetch()`
-   `axios`
-   `async/await`

They all follow the AJAX concept.

So:

-   **AJAX is the concept**
-   **fetch/axios are tools to implement it**

------------------------------------------------------------------------

## 🔥 Connection With What You Learned

  Concept       Meaning
  ------------- ----------------------------
  Promise       Future result
  async/await   Cleaner promise handling
  fetch         Modern way to do AJAX
  AJAX          Update page without reload

See how everything connects? 🔥

------------------------------------------------------------------------

## 🏆 One-Line Definition

**AJAX is a technique to communicate with a server asynchronously
without refreshing the webpage.**