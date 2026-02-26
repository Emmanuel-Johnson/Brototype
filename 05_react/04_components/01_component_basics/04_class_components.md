# 🏛 What Are Class Components in React?

Before Hooks existed, React components were written using ES6 classes.

Instead of a function, you write a class that extends `React.Component`.

------------------------------------------------------------------------

## 🧠 Basic Structure

``` jsx
import React from "react";

class Welcome extends React.Component {
  render() {
    return <h1>Hello 👋</h1>;
  }
}
```

### Key things here:

-   `class` keyword
-   `extends React.Component`
-   Must have a `render()` method
-   `render()` returns JSX

Without `render()` → it won't work.

------------------------------------------------------------------------

## 🔥 Adding State in Class Component

``` jsx
class Counter extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      count: 0
    };
  }

  increase = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        <p>{this.state.count}</p>
        <button onClick={this.increase}>Increase</button>
      </div>
    );
  }
}
```

### Notice the differences:

-   State is inside `this.state`
-   Updating state uses `this.setState()`
-   Everything uses `this`
-   More complex
-   More boilerplate

------------------------------------------------------------------------

## 🆚 Class vs Functional (Why Class Is Rare Now)

  Class Component          Functional Component
  ------------------------ ----------------------
  Uses `this`              No `this` confusion
  Uses lifecycle methods   Uses Hooks
  More code                Cleaner & shorter
  Older pattern            Modern standard

After React introduced Hooks (React 16.8), functional components became
powerful enough to replace class components.

Now in real projects (like your LMS & E-commerce),
you should NOT be writing new class components.

You only need to understand them because:

-   Old projects still use them
-   Interviewers may ask about them

------------------------------------------------------------------------

## 🧠 Important Concept: Lifecycle in Classes

Class components use lifecycle methods like:

-   `componentDidMount()`
-   `componentDidUpdate()`
-   `componentWillUnmount()`

In functional components, we use:

-   `useEffect()`

Much cleaner.