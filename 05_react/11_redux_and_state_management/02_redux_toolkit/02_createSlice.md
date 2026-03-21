# 🚀 What is createSlice?

👉 **createSlice** is a function from Redux Toolkit that:

- ✅ creates state  
- ✅ creates reducers  
- ✅ creates actions automatically  

👉 All in ONE place 🎯  

---

## 🧠 Why it exists?

Old Redux 😵:

- action types  
- action creators  
- switch cases  

👉 Too much boilerplate  

RTK 😎:

👉 Just write one slice → everything generated  

---

## ⚙️ Basic Syntax

```js
import { createSlice } from "@reduxjs/toolkit";

const slice = createSlice({
  name: "sliceName",
  initialState: {},
  reducers: {}
});
```

---

## 🔥 Real Example (Movies)

```js
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  movies: [],
};

const movieSlice = createSlice({
  name: "movies",
  initialState,
  reducers: {
    addMovie: (state, action) => {
      state.movies.push(action.payload);
    },
    removeMovie: (state, action) => {
      state.movies = state.movies.filter(
        (movie) => movie.id !== action.payload
      );
    },
  },
});
```

---

## 📦 What createSlice gives you

### 1️⃣ Actions (auto-created)

```js
export const { addMovie, removeMovie } = movieSlice.actions;
```

👉 No need to manually write action creators  

---

### 2️⃣ Reducer

```js
export default movieSlice.reducer;
```

👉 This goes into your store  

---

## 🧠 Important Concept (VERY IMPORTANT 🔥)

👉 “Mutation” that is NOT mutation:

```js
state.movies.push(...)
```

👉 Looks like mutation ❌  
👉 Actually NOT mutation ✅  

Because of **Immer**

👉 Internally:

- creates a copy  
- applies changes  
- returns new state  

---

## ⚡ How it works internally

You write:

```js
state.count++
```

👉 RTK converts it to:

```js
return {
  ...state,
  count: state.count + 1
};
```

---

## 🧠 Action Object (Behind the scenes)

If you do:

```js
dispatch(addMovie("Inception"));
```

👉 Internally becomes:

```js
{
  type: "movies/addMovie",
  payload: "Inception"
}
```

---

## 🔥 With Payload Example

```js
dispatch(addMovie({ id: 1, name: "Interstellar" }));
```

👉 In reducer:

```js
action.payload
```

---

## ⚠️ Common Mistakes

❌ Returning AND mutating state together

```js
state.movies.push(...)
return state // ❌ wrong
```

👉 Either:

- mutate (RTK handles it) ✅  
- OR return new state ✅  

---

❌ Using wrong state path

```js
state.push(...) // ❌ if state is object
```

---

## 🧠 Mental Model (Super Important)

👉 Slice = “one feature of your app”

Examples:

- moviesSlice 🎬  
- userSlice 👤  
- cartSlice 🛒  

---

## 🧠 Final Summary

👉 createSlice:

- combines state + reducer + actions  
- reduces boilerplate  
- allows safe “mutation” (Immer)  
- auto-generates action types  

---

## 🔥 What YOU should do next

👉 Since you're building projects:

Create:

- movieSlice  
- userSlice  
- cartSlice  

👉 Practice:

- add / remove / update data  