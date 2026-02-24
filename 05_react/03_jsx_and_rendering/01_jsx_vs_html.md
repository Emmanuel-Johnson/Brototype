# 🆚 JSX vs HTML

## 1️⃣ What is HTML?

HTML = HyperText Markup Language

It's used to structure web pages.

Example:

``` html
<h1 class="title">Hello</h1>
```

Browser reads this directly.

------------------------------------------------------------------------

## 2️⃣ What is JSX?

JSX = JavaScript XML

Used in React.

It looks like HTML, but it's actually JavaScript syntax.

Example:

``` jsx
<h1 className="title">Hello</h1>
```

JSX is not understood by the browser directly.

It gets converted into JavaScript like this:

``` javascript
React.createElement("h1", { className: "title" }, "Hello");
```

Then the browser understands it.

------------------------------------------------------------------------

## 🔥 Key Differences

### 1️⃣ class vs className

HTML:

``` html
<div class="box"></div>
```

JSX:

``` jsx
<div className="box"></div>
```

Why?
Because `class` is a reserved keyword in JavaScript.

------------------------------------------------------------------------

### 2️⃣ JavaScript inside HTML

HTML ❌ cannot do this:

``` html
<h1>{name}</h1>
```

JSX ✅ can:

``` jsx
<h1>{name}</h1>
```

JSX allows JavaScript inside `{ }`.

Example:

``` jsx
const age = 20;

<h1>{age + 5}</h1>
```

It will show:

    25

That's powerful 💥

------------------------------------------------------------------------

### 3️⃣ Self-closing tags

HTML (sometimes optional):

``` html
<img src="image.png">
```

JSX (mandatory):

``` jsx
<img src="image.png" />
```

In JSX, every tag must be closed.

------------------------------------------------------------------------

### 4️⃣ One Parent Rule

In HTML:

``` html
<h1>Hello</h1>
<p>World</p>
```

In JSX ❌ Not allowed directly.

You must wrap:

``` jsx
<>
  <h1>Hello</h1>
  <p>World</p>
</>
```

Because JSX must return one single parent element.

------------------------------------------------------------------------

### 5️⃣ Attributes are camelCase

HTML:

``` html
<button onclick="handleClick()"></button>
```

JSX:

``` jsx
<button onClick={handleClick}></button>
```

Notice:

`onclick` → `onClick`
JavaScript inside `{ }`

------------------------------------------------------------------------

## 🧠 Simple Mental Model

👉 HTML = Static structure
👉 JSX = HTML + JavaScript power

JSX lets you:

-   Use variables
-   Use conditions
-   Use loops
-   Dynamically render UI

That's why React feels dynamic.

------------------------------------------------------------------------

## 🚀 Quick Comparison Table

| Feature               | HTML             | JSX                      |
| --------------------- | ---------------- | ------------------------ |
| Used in               | Normal web pages | React                    |
| Understood by browser | ✅ Yes            | ❌ No (needs compilation) |
| JS inside             | ❌ No             | ✅ Yes                    |
| `class` attribute     | `class`          | `className`              |
| Self-closing tags     | Optional         | Mandatory (`<br />`)     |
