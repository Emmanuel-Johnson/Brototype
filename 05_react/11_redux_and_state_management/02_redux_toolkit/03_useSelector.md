# 🚀 What is useSelector?

👉 **useSelector** is a hook from React Redux that lets you:

👉 read data from the Redux store inside a component

---

## 🧠 Simple Idea

```js
const data = useSelector((state) => state.something);
```

👉 You are selecting a piece of global state  

---

## 🔥 Basic Example

```js
import { useSelector } from "react-redux";

const MovieList = () => {
  const movies = useSelector((state) => state.movies.movies);

  return (
    <div>
      {movies.map((m) => (
        <p key={m.id}>{m.name}</p>
      ))}
    </div>
  );
};
```

---

## 🧩 What’s happening?

👉 state = entire Redux store  

```js
{
  movies: {
    movies: []
  }
}
```

👉 So:

```js
state.movies.movies
```

---

## ⚡ Important Behavior (VERY IMPORTANT 🔥)

👉 Component re-renders when:

👉 selected value changes  

```js
const movies = useSelector((state) => state.movies.movies);
```

👉 Re-render ONLY if movies changes ✅  

---

## ❌ Bad Usage

```js
const state = useSelector((state) => state);
```

👉 Re-renders on ANY change 😬  

---

## 🧠 Multiple Selectors

```js
const movies = useSelector((state) => state.movies.movies);
const loading = useSelector((state) => state.movies.loading);
```

👉 Totally fine ✅  

---

## 🔥 Cleaner Way (Best Practice)

Create selectors:

```js
const selectMovies = (state) => state.movies.movies;

const movies = useSelector(selectMovies);
```

👉 Reusable + clean code  

---

## ⚡ Advanced: Avoid Unnecessary Re-renders

👉 By default, useSelector uses strict equality (===)

❌ Problem:

```js
const data = useSelector((state) => {
  return { movies: state.movies.movies };
});
```

👉 New object every time → re-render 😬  

---

## ✅ Fix: Use shallowEqual

```js
import { shallowEqual, useSelector } from "react-redux";

const data = useSelector(
  (state) => ({
    movies: state.movies.movies,
  }),
  shallowEqual
);
```

---

## 🧠 Real Flow

1. Component calls useSelector  
2. Subscribes to store  
3. Store updates  
4. If selected data changed → re-render  

---

## ⚠️ Common Mistakes

- ❌ Selecting entire state  
- ❌ Returning new objects every time  
- ❌ Doing heavy calculations inside selector  

---

## 🧠 Pro Tip (For YOU 👇)

👉 Since you're building projects:

- Select only needed data  
- Use simple selectors  
- Avoid unnecessary object creation  

---

## 🧠 Final Summary

👉 useSelector:

- reads data from Redux store  
- triggers re-render when data changes  
- must be used carefully for performance  