# 🚀 What is createAsyncThunk?

👉 **createAsyncThunk** is a function from Redux Toolkit used to:

👉 handle async operations (API calls, etc.) easily

---

## 🧠 What problem does it solve?

Without it 😵:

- manually write loading / success / error actions  
- messy async code  

With it 😎:

👉 Everything is auto-handled:

- pending ⏳  
- fulfilled ✅  
- rejected ❌  

---

## ⚙️ Basic Syntax

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

---

## 🧩 What this creates internally

It auto-generates 3 actions:

1. "movies/fetchMovies/pending"  
2. "movies/fetchMovies/fulfilled"  
3. "movies/fetchMovies/rejected"  

---

## 🔥 Use in createSlice

```js
const movieSlice = createSlice({
  name: "movies",
  initialState: {
    movies: [],
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchMovies.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchMovies.fulfilled, (state, action) => {
        state.loading = false;
        state.movies = action.payload;
      })
      .addCase(fetchMovies.rejected, (state, action) => {
        state.loading = false;
        state.error = "Something went wrong";
      });
  },
});
```

---

## ⚡ How to use in component

```js
const dispatch = useDispatch();

useEffect(() => {
  dispatch(fetchMovies());
}, []);
```

---

## 🧠 Flow (VERY IMPORTANT 🔥)

1. dispatch(fetchMovies())  
2. pending → loading = true  
3. API call happens  
4. success → fulfilled  
5. state updates  
6. UI re-renders  

---

## 🔥 With Parameters

```js
export const fetchMovieById = createAsyncThunk(
  "movies/fetchById",
  async (id) => {
    const res = await fetch(`/api/movies/${id}`);
    return res.json();
  }
);
```

👉 Use:

```js
dispatch(fetchMovieById(5));
```

---

## ⚠️ Error Handling (Important)

```js
export const fetchMovies = createAsyncThunk(
  "movies/fetchMovies",
  async (_, { rejectWithValue }) => {
    try {
      const res = await fetch("/api/movies");
      return await res.json();
    } catch (err) {
      return rejectWithValue("API Failed");
    }
  }
);
```

---

## 🧠 Why it's powerful

👉 No need to:

- create action types  
- write thunk manually  
- manage async states manually  

---

## ⚔️ createAsyncThunk vs Thunk

| Feature | Thunk 😌 | createAsyncThunk 🔥 |
|--------|---------|--------------------|
| Boilerplate | More | Less |
| Loading states | Manual | Auto |
| Error handling | Manual | Built-in |
| Recommended | ❌ | ✅ YES |

---

## 🧠 Final Summary

👉 createAsyncThunk:

- handles async logic  
- auto-generates actions  
- simplifies API calls  
- best practice in RTK  

---

## 🔥 What YOU should do next

👉 Since you're building projects:

- Implement fetch movies API  
- Add loading spinner  
- Add error message  

👉 That’s real-world skill 💯  