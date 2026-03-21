# 🧠 The 3 Core Principles of Redux

---

## 1️⃣ Single Source of Truth

👉 All your app state lives in **ONE place (the store)**

Instead of:

multiple states everywhere 😵‍💫

You have:

```js
const store = {
  user: {},
  movies: [],
  cart: []
};
```

### 💡 Why this matters:

- Easy to debug  
- No confusion about where data is  
- Everything is predictable  

👉 Think: **one brain controlling the whole app**

---

## 2️⃣ State is Read-Only

👉 You cannot directly change the state

❌ Wrong:

```js
state.movies.push("Inception");
```

✅ Correct:

```js
dispatch({
  type: "ADD_MOVIE",
  payload: "Inception"
});
```

### 💡 Meaning:

- You must send an action  
- Redux controls how state changes  

👉 This prevents:

- Random bugs  
- Unexpected changes  

---

## 3️⃣ Changes with Pure Functions (Reducers)

👉 Reducers are **pure functions**

A pure function:

- Same input → same output  
- No side effects  

### Example:

```js
function movieReducer(state, action) {
  switch (action.type) {
    case "ADD_MOVIE":
      return {
        ...state,
        movies: [...state.movies, action.payload]
      };
    default:
      return state;
  }
}
```

### 💡 Why this matters:

- Predictable behavior  
- Easy testing  
- Easy debugging  

---

## 🔄 Put Together (Simple Flow)

👉 These 3 principles combine into:

**Single Store → Action → Reducer → New State**

---

## ⚠️ Small Reality Check (Important)

In **Redux Toolkit (RTK)**:

You can write code that looks like mutation:

```js
state.movies.push(action.payload);
```

👉 But internally, Redux still keeps things **immutable (using Immer)**

So don’t get confused — the principle still stands ✅

---

## 🎯 Final Summary

- 🧠 Single source of truth → one store  
- 🚫 State is read-only → use actions  
- ⚙️ Pure functions → reducers control changes  