# 🌳 What is DOM?

**DOM = Document Object Model**

It's a tree representation of your HTML page created by the browser.

When the browser loads HTML:

-   It reads the HTML file
-   Converts it into objects
-   Builds a tree structure

JavaScript can then:

-   Read it
-   Modify it
-   Delete parts
-   Add new elements

👉 So DOM is basically HTML converted into JavaScript objects.

------------------------------------------------------------------------

# 🧠 Example

## HTML:

``` html
<body>
  <h1>Hello</h1>
  <p>Welcome</p>
</body>
```

## DOM Tree:

    Document
     └── html
          └── body
               ├── h1
               └── p

Each of these is a **node (object)**.

------------------------------------------------------------------------

# 🔹 Core DOM Concepts

## 1️⃣ Document Object

The entry point.

``` js
console.log(document);
```

Everything starts from `document`.

Examples:

-   `document.title`
-   `document.body`
-   `document.URL`

------------------------------------------------------------------------

## 2️⃣ Selecting Elements

You must select before modifying.

``` js
document.getElementById("id")
document.getElementsByClassName("class")
document.getElementsByTagName("p")
document.querySelector(".class")
document.querySelectorAll("p")
```

🔥 Modern JS mostly uses:

-   `querySelector()`
-   `querySelectorAll()`

------------------------------------------------------------------------

## 3️⃣ Changing Content

``` js
element.innerText
element.textContent
element.innerHTML
```

Example:

``` js
document.querySelector("h1").innerText = "Hello Emmanuel"
```

Boom --- UI changed.

------------------------------------------------------------------------

## 4️⃣ Changing Styles

``` js
element.style.color = "red"
element.style.backgroundColor = "black"
```

------------------------------------------------------------------------

## 5️⃣ Creating & Adding Elements

``` js
const newDiv = document.createElement("div")
newDiv.innerText = "New Element"
document.body.appendChild(newDiv)
```

------------------------------------------------------------------------

## 6️⃣ Removing Elements

``` js
element.remove()
```

------------------------------------------------------------------------

## 7️⃣ Event Handling (Very Important 🚀)

This is how interactivity works.

``` js
button.addEventListener("click", function() {
  alert("Clicked!")
})
```

Common events:

-   click
-   submit
-   change
-   input
-   mouseover

------------------------------------------------------------------------

## 8️⃣ Traversing the DOM

Move around the tree:

``` js
element.parentNode
element.children
element.firstElementChild
element.lastElementChild
element.nextElementSibling
element.previousElementSibling
```

------------------------------------------------------------------------

# 🧠 How This Connects to React

In vanilla JS, you manually:

-   Select
-   Update
-   Re-render

In React, you:

-   Change state
-   React updates DOM automatically

React uses something called **Virtual DOM** to optimize this.

So DOM knowledge = React superpower.

------------------------------------------------------------------------

# 🚀 Quick Real-World Example

``` html
<button id="btn">Click</button>
<p id="text">Hello</p>
```

``` js
const btn = document.getElementById("btn")
const text = document.getElementById("text")

btn.addEventListener("click", () => {
  text.innerText = "You clicked!"
})
```

That's DOM manipulation.

------------------------------------------------------------------------

# 🏗️ DOM Types of Nodes

-   **Element Node** → `<div>`
-   **Text Node** → "Hello"
-   **Attribute Node** → `class="box"`
-   **Comment Node** → `<!-- comment -->`

------------------------------------------------------------------------

# 🎯 Why DOM Matters

Since you're building:

-   LMS project
-   E-commerce project

You'll deal with:

-   Form handling
-   Dynamic product rendering
-   Event listeners
-   Conditional UI updates

Even if React hides it, understanding DOM makes debugging 10x easier.