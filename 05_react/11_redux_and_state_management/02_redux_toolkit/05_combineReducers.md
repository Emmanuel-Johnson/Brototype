# 🚀 What is combineReducers?

👉 **combineReducers** is a function from Redux that lets you:

👉 combine multiple reducers into one root reducer  

---

## 🧠 Why do we need it?

As your app grows:

- movies 🎬  
- users 👤  
- cart 🛒  

👉 You don’t want one big messy reducer 😵‍💫  

👉 Instead, split into small reducers and combine them ✅  

---

## 🔥 Without combineReducers (Bad)

```js
const rootReducer = (state, action) => {
  return {
    movies: movieReducer(state.movies, action),
    users: userReducer(state.users, action),
  };
};
```

👉 Works… but messy and manual 😬  

---

## ✅ With combineReducers

```js
import { combineReducers } from "redux";

const rootReducer = combineReducers({
  movies: movieReducer,
  users: userReducer,
});
```

👉 Clean + scalable 🎯  

---

## 🧩 What happens internally?

👉 Redux creates state like:

```js
{
  movies: movieReducerState,
  users: userReducerState
}
```

👉 Each reducer manages its own slice  

---

## ⚡ Example

```js
const movieReducer = (state = [], action) => {
  switch (action.type) {
    case "ADD_MOVIE":
      return [...state, action.payload];
    default:
      return state;
  }
};

const userReducer = (state = {}, action) => {
  switch (action.type) {
    case "SET_USER":
      return action.payload;
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  movies: movieReducer,
  user: userReducer,
});
```

---

## 🧠 Final State Shape

```js
{
  movies: [...],
  user: {...}
}
```

---

## ⚙️ With Redux Toolkit (IMPORTANT 🔥)

👉 You usually don’t need combineReducers manually  

```js
import { configureStore } from "@reduxjs/toolkit";

export const store = configureStore({
  reducer: {
    movies: movieReducer,
    users: userReducer,
  },
});
```

👉 RTK automatically does combineReducers internally 🎉  

---

## 🧠 Mental Model

👉 Each reducer = mini manager  
👉 combineReducers = team leader combining them  

---

## ⚠️ Important Rules

- Each reducer handles only its slice  
- Keys define state structure  
- Reducers must be pure  

---

## 🔥 Common Mistake

❌ Wrong selector path:

```js
state.movies // ❌ if combined differently
```

👉 Always match structure:

```js
state.movies.movies
```

(depends on your slice)

---

## 🧠 Final Summary

👉 combineReducers:

- combines multiple reducers  
- creates structured state  
- used for scaling apps  

👉 In Redux Toolkit:

- handled automatically ✅  

---

## 🔥 For YOU (Important)

👉 Since you're using RTK:

- Focus on multiple slices  
- Focus on store structure  

👉 Don’t worry too much about manual combineReducers  