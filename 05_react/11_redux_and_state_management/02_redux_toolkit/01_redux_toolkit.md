# 🚀 What is Redux Toolkit (RTK)?

👉 **Redux Toolkit (RTK)** is the official, modern way to write Redux.

👉 It removes:

- boilerplate 😵‍💫  
- complexity 😵  

👉 And gives:

- cleaner code ✅  
- built-in best practices ✅  

---

## 🧠 Why RTK exists?

Old Redux was like:

- action types  
- action creators  
- switch cases  
- reducers  

👉 Too much code for simple things 😬  

🔥 RTK solves this → Write LESS code, do MORE work  

---

## ⚙️ Core Features of Redux Toolkit

### 1️⃣ configureStore

👉 Creates store easily

```js
import { configureStore } from "@reduxjs/toolkit";
import movieReducer from "./movieSlice";

export const store = configureStore({
  reducer: {
    movies: movieReducer,
  },
});
```

👉 Automatically adds:

- Thunk middleware ✅  
- DevTools ✅  

---

### 2️⃣ createSlice (MOST IMPORTANT 🔥)

👉 Combines:

- state  
- reducers  
- actions  

```js
import { createSlice } from "@reduxjs/toolkit";

const movieSlice = createSlice({
  name: "movies",
  initialState: {
    movies: [],
  },
  reducers: {
    addMovie: (state, action) => {
      state.movies.push(action.payload);
    },
  },
});

export const { addMovie } = movieSlice.actions;
export default movieSlice.reducer;
```

---

## 🧠 Magic here (VERY IMPORTANT)

👉 Looks like mutation:

```js
state.movies.push(...)
```

👉 But internally uses **Immer**

- state is NOT mutated ❌  
- new state is created ✅  

---

### 3️⃣ Async Handling (createAsyncThunk) 🔥

```js
import { createAsyncThunk } from "@reduxjs/toolkit";

export const fetchMovies = createAsyncThunk(
  "movies/fetchMovies",
  async () => {
    const res = await fetch("/api/movies");
    return res.json();
  }
);
```

### 👉 Handle in slice:

```js
extraReducers: (builder) => {
  builder
    .addCase(fetchMovies.pending, (state) => {
      state.loading = true;
    })
    .addCase(fetchMovies.fulfilled, (state, action) => {
      state.movies = action.payload;
      state.loading = false;
    });
}
```

---

### 4️⃣ Built-in Middleware

👉 No need to install:

- Redux Thunk ✅  
- DevTools ✅  

---

### 5️⃣ RTK Query (Advanced 🔥🔥)

👉 Best for API calls:

- caching  
- auto fetching  
- less code  

👉 (Learn later — high interview value)

---

## 🧠 RTK Flow

1. Component dispatches action  
2. Slice reducer updates state  
3. UI re-renders  

👉 Same Redux flow — but cleaner  

---

## ⚔️ Redux vs Redux Toolkit

| Feature | Old Redux 😵 | RTK 😎 |
|--------|-------------|--------|
| Boilerplate | High | Low |
| Setup | Complex | Easy |
| Async handling | Manual | Built-in |
| Best practice | Manual | Included |

---

## ⚠️ Important Things

- You can “mutate” state (thanks to Immer)  
- Still follows Redux principles  
- Reducers are still pure  

---

## 🧠 Final Summary

👉 Redux Toolkit = modern Redux  
👉 Less code, more power  

Includes:

- configureStore  
- createSlice  
- createAsyncThunk  
- built-in middleware  

---

## 🔥 What YOU should focus on

👉 For job:

**Master:**

- createSlice  
- createAsyncThunk  
- store setup  

👉 Then learn:

- RTK Query 🔥  