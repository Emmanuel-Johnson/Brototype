# 🚀 Handling Async Actions in Redux

👉 “Handling async actions” = how your app deals with:

- API calls 🌐  
- Delays ⏳  
- Database requests  

---

## 🚀 What are Async Actions?

👉 Async = something that takes time to complete  

Example:

```js
fetch("/api/movies");
```

👉 This doesn’t return data instantly — it waits.

---

## ❌ Problem in Redux

👉 Reducers must be pure functions:

- No API calls  
- No delays  
- No side effects  

❌ WRONG:

```js
const reducer = (state, action) => {
  const data = await fetch("/api"); // ❌ not allowed
};
```

---

## ✅ Solution: Handle async OUTSIDE reducers

There are 3 main ways:

---

## 1️⃣ Redux Thunk (Most common)

👉 Write async logic inside a function:

```js
export const fetchMovies = () => async (dispatch) => {
  dispatch({ type: "FETCH_START" });

  const res = await fetch("/api/movies");
  const data = await res.json();

  dispatch({ type: "FETCH_SUCCESS", payload: data });
};
```

### 🧠 Flow

- dispatch(fetchMovies())  
- API call happens  
- Dispatch success/failure  
- Reducer updates state  

### 📦 State Example

```js
{
  loading: true,
  data: [],
  error: null
}
```

---

## 2️⃣ Redux Toolkit (createAsyncThunk) 🔥

👉 BEST way today

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

### 🧠 In slice:

```js
extraReducers: (builder) => {
  builder
    .addCase(fetchMovies.pending, (state) => {
      state.loading = true;
    })
    .addCase(fetchMovies.fulfilled, (state, action) => {
      state.loading = false;
      state.movies = action.payload;
    })
    .addCase(fetchMovies.rejected, (state) => {
      state.loading = false;
      state.error = "Error";
    });
}
```

### 🔥 What you get automatically:

- loading state ✅  
- success state ✅  
- error handling ✅  

---

## 3️⃣ Redux Saga (Advanced)

👉 Listen to actions and handle async separately:

```js
function* fetchMoviesSaga() {
  try {
    const res = yield call(fetch, "/api/movies");
    const data = yield res.json();

    yield put({ type: "FETCH_SUCCESS", payload: data });
  } catch (e) {
    yield put({ type: "FETCH_ERROR" });
  }
}
```

---

## ⚔️ Which one should YOU use?

👉 Since you're aiming for a job fast:

🥇 Redux Toolkit + createAsyncThunk  

- Industry standard  
- Easy + powerful  

---

## 🧠 Real App Flow

1. UI loads  
2. dispatch(fetchMovies())  
3. loading = true  
4. API call happens  
5. success → data stored  
6. UI updates automatically  

---

## ⚠️ Common Mistakes

- ❌ Doing API calls inside reducer  
- ❌ Not handling loading state  
- ❌ Ignoring error handling  

---

## 🧠 Final Summary

- Async actions = API/delay operations  
- Reducers can’t handle them  
- Use middleware:

  - Thunk ✅  
  - createAsyncThunk 🔥 (BEST)  
  - Saga 😎 (advanced)  