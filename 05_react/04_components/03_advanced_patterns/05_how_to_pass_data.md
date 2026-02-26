# 🔄 Passing Data in React

------------------------------------------------------------------------

## 1️⃣ Passing Data from Parent to Child (Props)

This is the most common way.

### 🧠 Concept:

Parent component sends data as props.

### Example:

#### Parent.jsx

``` jsx
function Parent() {
  const name = "Emmanuel";

  return <Child username={name} />;
}
```

#### Child.jsx

``` jsx
function Child(props) {
  return <h1>Hello {props.username}</h1>;
}
```

OR using destructuring (cleaner 👇)

``` jsx
function Child({ username }) {
  return <h1>Hello {username}</h1>;
}
```

👉 Here:

-   `username` is a prop
-   `name` value is passed from Parent
-   Data flows downward only

------------------------------------------------------------------------

## 2️⃣ Passing Multiple Data

``` jsx
<Child name="Emmanuel" age={22} isStudent={true} />
```

``` jsx
function Child({ name, age, isStudent }) {
  return (
    <>
      <p>Name: {name}</p>
      <p>Age: {age}</p>
      <p>Student: {isStudent ? "Yes" : "No"}</p>
    </>
  );
}
```

You can pass:

-   Strings
-   Numbers
-   Boolean
-   Arrays
-   Objects
-   Even Functions 😎

------------------------------------------------------------------------

## 3️⃣ Passing Array / Object

``` jsx
const products = ["Laptop", "Phone", "Watch"];

<Child items={products} />
```

``` jsx
function Child({ items }) {
  return (
    <ul>
      {items.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </ul>
  );
}
```

This is SUPER important for your e-commerce project.

------------------------------------------------------------------------

## 4️⃣ Passing Function (Child → Parent Communication)

React cannot send data directly upward.

So we pass a function from parent.

``` jsx
function Parent() {
  const handleClick = (data) => {
    console.log("Received from child:", data);
  };

  return <Child sendData={handleClick} />;
}
```

``` jsx
function Child({ sendData }) {
  return (
    <button onClick={() => sendData("Hello Parent")}>
      Send Data
    </button>
  );
}
```

🔥 Now child can send data to parent using callback.

This is VERY important for:

-   Add to cart
-   Form submit
-   Delete item
-   Updating state

You'll use this everywhere in your LMS and e-commerce projects.

------------------------------------------------------------------------

## 5️⃣ Passing Data Between Siblings

Sibling → Sibling ❌ directly not possible

### Solution:

Lift state up to common parent.

    Parent
     ├── ChildA
     └── ChildB

Parent holds state, passes to both.

------------------------------------------------------------------------

## 6️⃣ Global Data (Advanced)

When project becomes bigger (like your production-level apps):

-   Context API
-   Redux
-   Zustand

But first master props + state perfectly.

------------------------------------------------------------------------

## 🚀 Important Rule

React = One-way data flow

Parent → Child

Always remember this.