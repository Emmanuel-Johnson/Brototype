# 💛 What is jQuery?

jQuery is a JavaScript library.

It was created to make JavaScript:

-   Easier
-   Shorter
-   Cross-browser compatible

Back in the day, writing plain JavaScript was painful. jQuery made it
simple.

------------------------------------------------------------------------

## 🧠 Simple Meaning

jQuery =
👉 "Write less code, do more things."

That was literally its slogan.

------------------------------------------------------------------------

## 🆚 Example: Without jQuery (Old JS)

``` javascript
document.getElementById("btn").addEventListener("click", function() {
  document.getElementById("text").style.color = "red";
});
```

------------------------------------------------------------------------

## ✨ With jQuery

``` javascript
$("#btn").click(function() {
  $("#text").css("color", "red");
});
```

See the difference?

Much shorter. Cleaner (at that time).

------------------------------------------------------------------------

## 🔥 jQuery and AJAX

Before `fetch()` existed, jQuery made AJAX very easy.

``` javascript
$.ajax({
  url: "https://jsonplaceholder.typicode.com/todos/1",
  method: "GET",
  success: function(data) {
    console.log(data);
  }
});
```

That was revolutionary in 2010 😄

------------------------------------------------------------------------

## 🤔 Do We Still Use jQuery Today?

Not much.

Because modern JavaScript now has:

-   `querySelector`
-   `addEventListener`
-   `fetch`
-   `async/await`

And frameworks like:

-   React
-   Vue
-   Angular

So jQuery became less necessary.

------------------------------------------------------------------------

## 🎯 Should YOU Learn jQuery?

Since you're building:

-   Django REST APIs
-   React frontend
-   Production projects

👉 You don't need jQuery.

Just understand what it is for interviews.

------------------------------------------------------------------------

## 🏆 One-Line Definition

**jQuery is a JavaScript library that simplified DOM manipulation and
AJAX before modern JS and frameworks existed.**