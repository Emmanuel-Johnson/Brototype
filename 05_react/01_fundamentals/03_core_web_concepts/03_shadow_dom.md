# 🌑 What is Shadow DOM?

Shadow DOM is a browser feature that lets you create a separate, hidden
DOM tree inside an element.

It creates **DOM isolation**.

Think of it like:

> A mini private DOM inside a component.

------------------------------------------------------------------------

# 🧠 Why It Exists

## Problem

Normal DOM is global.

If you write:

``` css
button {
  color: red;
}
```

It affects all buttons everywhere 😬

But what if a component wants:

-   Its own HTML
-   Its own CSS
-   No interference from outside styles

👉 That's where Shadow DOM comes in.

------------------------------------------------------------------------

# 🌳 Normal DOM vs Shadow DOM

## Normal DOM

Everything is visible and accessible.

    document
     └── body
          └── div

## Shadow DOM

An element contains a hidden subtree.

    document
     └── body
          └── <custom-element>
                └── #shadow-root
                      └── internal DOM

------------------------------------------------------------------------

# 🧪 Example

``` js
const host = document.querySelector("#box");

const shadow = host.attachShadow({ mode: "open" });

shadow.innerHTML = `
  <style>
    p { color: red; }
  </style>
  <p>Hello inside shadow DOM</p>
`;
```

Now:

-   The `<p>` is inside shadow DOM
-   Its styles don't leak outside
-   Outside styles don't affect it

Isolation achieved.

------------------------------------------------------------------------

# 🔒 Two Modes

``` js
attachShadow({ mode: "open" })
attachShadow({ mode: "closed" })
```

## Open

You can access:

``` js
element.shadowRoot
```

## Closed

You cannot access `shadowRoot` from outside.

------------------------------------------------------------------------

# 🆚 Shadow DOM vs Virtual DOM

  Feature               Shadow DOM              Virtual DOM
  --------------------- ----------------------- --------------------------
  Purpose               Style & DOM isolation   Performance optimization
  Created by            Browser API             React
  Visible in DevTools   Yes                     No
  Used in               Web Components          React

Different goals. Completely different things.

------------------------------------------------------------------------

# 🌐 Where Is Shadow DOM Used?

## 🔹 Web Components

Custom HTML elements.

Examples:

-   `<my-button>`
-   `<custom-card>`

## 🔹 Browsers Already Use It

Even `<input>` elements use Shadow DOM internally 😮

The UI inside input field is isolated.

------------------------------------------------------------------------

# 🧠 Why This Matters

Right now in React you don't manually use Shadow DOM.

But if:

-   You build reusable UI libraries
-   You work with Web Components
-   You integrate third-party widgets

Then Shadow DOM becomes powerful.

------------------------------------------------------------------------

# 🚀 Quick Analogy

-   **Actual DOM →** Public street
-   **Virtual DOM →** Planning board before construction
-   **Shadow DOM →** Private room inside a building

Different problems. Different solutions.