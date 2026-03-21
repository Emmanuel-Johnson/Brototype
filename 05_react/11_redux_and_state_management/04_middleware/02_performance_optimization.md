# 🚀 Redux Performance Optimization

## 🤔 Why Performance Issues Happen in Redux

👉 Main problem:

Too many unnecessary re-renders

When Redux state updates:

- Components subscribed to store may re-render 😵‍💫  
- Even if data didn’t actually change  

---

## 🧠 Goal

- Only re-render when needed  
- Keep state minimal & efficient  

---

## 🔥 1️⃣ Normalize Your State (VERY IMPORTANT)

❌ Bad (nested, heavy):

```js
{
  users: [
    { id: 1, name: "John", posts: [...] }
  ]
}
```

✅ Good (normalized):

```js
{
  users: {
    byId: {
      1: { id: 1, name: "John" }
    },
    allIds: [1]
  }
}
```

👉 Why?

- Faster updates  
- Less re-rendering  

---

## ⚡ 2️⃣ Use useSelector Smartly

❌ Bad:

```js
const state = useSelector((state) => state);
```

👉 Causes re-render on ANY change 😬  

✅ Good:

```js
const movies = useSelector((state) => state.movies);
```

👉 Only re-renders when movies changes  

---

## 🧠 3️⃣ Memoization (Huge win 🔥)

Use createSelector (Reselect)

```js
import { createSelector } from "@reduxjs/toolkit";

const selectMovies = (state) => state.movies;

export const selectPopularMovies = createSelector(
  [selectMovies],
  (movies) => movies.filter(m => m.rating > 8)
);
```

👉 Prevents recalculating every time  

---

## ⚡ 4️⃣ Avoid Unnecessary State Updates

❌ Bad:

```js
return {
  ...state,
  movies: [...state.movies] // no real change
};
```

👉 Creates new reference → re-render  

✅ Good:

👉 Only update when data actually changes  

---

## 🔥 5️⃣ Split Components Properly

👉 Big component = bad  

- ❌ One component using entire state  
- ✅ Smaller components using specific slices  

---

## ⚡ 6️⃣ Use React.memo

```js
export default React.memo(MyComponent);
```

👉 Prevents re-render if props didn’t change  

---

## 🧠 7️⃣ Use RTK Entity Adapter (Pro Level 🔥)

```js
import { createEntityAdapter } from "@reduxjs/toolkit";

const moviesAdapter = createEntityAdapter();
```

👉 Gives:

- normalized state automatically  
- optimized selectors  

---

## ⚡ 8️⃣ Batch Updates (Advanced)

👉 React automatically batches updates in modern versions  

- Reduces multiple re-renders  

---

## 🔥 9️⃣ Avoid Heavy Logic in Components

❌ Bad:

```js
const filtered = movies.filter(...)
```

👉 Runs on every render  

✅ Good:

👉 Move to selector (memoized)  

---

## 🧠 Real Problem Example

👉 Without optimization:

Typing in input → whole app re-renders 😬  

👉 With optimization:

Only that component updates ✅  

---

## ⚠️ Golden Rules

- Keep state minimal  
- Avoid unnecessary object/array creation  
- Use memoization  
- Select only what you need  

---

## 🧠 Final Summary

👉 Performance = controlling re-renders  

Do this:

- Normalize state ✅  
- Smart useSelector ✅  
- Memoized selectors ✅  
- Split components ✅  
- Use RTK tools ✅  

---

## 🧠 Pro Tip (For You 👇)

Since you're aiming job fast:

👉 Focus on:

- useSelector optimization  
- createAsyncThunk  
- basic memoization  

👉 Don’t go too deep into Saga-level optimization now  