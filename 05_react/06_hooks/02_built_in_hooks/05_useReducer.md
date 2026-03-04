# 🧠 useReducer in React

`useReducer` is a React Hook used for complex state logic.

Think of it like:

-   `useState` = simple state
-   `useReducer` = structured state logic

It works almost exactly like Redux, but inside a component.

------------------------------------------------------------------------

## 🔥 Why Not Just useState?

If you have:

-   Multiple related state values
-   State that depends on previous state
-   Complex update logic
-   Many different state transitions

`useReducer` becomes cleaner.

------------------------------------------------------------------------

## 🏗 The Core Concept

`useReducer` has 3 parts:

-   State
-   Action
-   Reducer function

------------------------------------------------------------------------

## 🧩 Basic Syntax

``` js
const [state, dispatch] = useReducer(reducer, initialState);
```

-   `state` → current state
-   `dispatch` → function to send actions
-   `reducer` → function that decides how state changes
-   `initialState` → starting value

------------------------------------------------------------------------

## 💡 Simple Counter Example

``` js
import { useReducer } from "react";

const initialState = { count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + 1 };

    case "DECREMENT":
      return { count: state.count - 1 };

    default:
      return state;
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <div>
      <h2>{state.count}</h2>
      <button onClick={() => dispatch({ type: "INCREMENT" })}>
        +
      </button>
      <button onClick={() => dispatch({ type: "DECREMENT" })}>
        -
      </button>
    </div>
  );
}
```

------------------------------------------------------------------------

## 🧠 What's Actually Happening?

When you call:

``` js
dispatch({ type: "INCREMENT" })
```

React:

1.  Sends action to reducer
2.  Reducer checks `action.type`
3.  Returns new state
4.  Component re-renders

Very predictable. Very clean.

------------------------------------------------------------------------

## 🆚 useState vs useReducer

### ✅ useState

``` js
const [count, setCount] = useState(0);
```

Best for:

-   Simple values
-   Independent states

------------------------------------------------------------------------

### ✅ useReducer

Best for:

-   Forms with many fields
-   Cart systems
-   Auth logic
-   State machines
-   Complex updates

------------------------------------------------------------------------

## 🛒 Real Example (Cart)

``` js
const initialState = {
  items: [],
  total: 0
};

function reducer(state, action) {
  switch (action.type) {
    case "ADD_ITEM":
      return {
        ...state,
        items: [...state.items, action.payload],
        total: state.total + action.payload.price
      };

    case "REMOVE_ITEM":
      return {
        ...state,
        items: state.items.filter(item => item.id !== action.payload.id),
        total: state.total - action.payload.price
      };

    default:
      return state;
  }
}
```

Now your cart logic is structured and scalable.

------------------------------------------------------------------------

## 🚀 Pro Pattern (Advanced)

You can combine:

-   `useReducer`
-   `useContext`

That's basically mini Redux without installing anything.

Perfect for:

-   Auth system
-   Cart system
-   Global app state (medium scale)

------------------------------------------------------------------------

## 🎯 When You Should Use It

Since you're building real projects:

Use `useReducer` when:

-   Your form has 5+ fields
-   Your cart logic grows
-   You feel `useState` becoming messy