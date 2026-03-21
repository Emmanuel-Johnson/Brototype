# 🚀 What is Redux Middleware?

👉 **Middleware** is like a middle layer between:

dispatch(action) → middleware → reducer

👉 It can:

- intercept actions  
- modify them  
- delay them  
- run side effects (API calls, logging, etc.)  

---

## 🧠 Simple Idea

👉 Without middleware:

Component → dispatch → reducer → state update  

👉 With middleware:

Component → dispatch → 🛑 middleware → reducer → state  

---

## 🔥 Why do we need Middleware?

Because Redux by default:

- only handles sync actions  
- reducers must be pure  

👉 Middleware helps to:

- handle async (Thunk, Saga)  
- log actions (debugging)  
- handle errors  
- add custom logic  

---

## 🧩 Example: Logger Middleware

```js
const logger = (store) => (next) => (action) => {
  console.log("Dispatching:", action);

  const result = next(action); // pass to next middleware/reducer

  console.log("Next State:", store.getState());

  return result;
};
```

---

## 🧠 What’s happening?

- store → access state  
- next → passes action forward  
- action → current action  

👉 Pattern:

(store) => (next) => (action)

---

## ⚡ Real Flow

```js
dispatch({ type: "ADD_MOVIE" });
```

👉 Middleware:

- catches action  
- runs logic  
- forwards to reducer  

---

## 🔥 Most Important Middlewares

### 1️⃣ Redux Thunk
👉 Allows:

dispatch(function)

Instead of:

dispatch({ type: "ACTION" })

👉 Handles async logic  

---

### 2️⃣ Redux Saga
👉 Listens to actions and runs background tasks  

---

### 3️⃣ Logger Middleware
👉 Logs everything (for debugging)  

---

## ⚙️ Middleware in Redux Toolkit

👉 Redux Toolkit already includes:

- Thunk ✅  
- DevTools ✅  

### Example:

```js
import { configureStore } from "@reduxjs/toolkit";

const store = configureStore({
  reducer: rootReducer,
});
```

👉 Middleware applied automatically 🎉  

---

## 🧠 Real-Life Analogy

👉 Think middleware like a **security + processing gate 🛂**

- You send request (action)  
- Middleware checks/modifies it  
- Then allows it to go inside (reducer)  

---

## ⚠️ Important Rules

- Middleware runs before reducer  
- Must call `next(action)` to continue flow  
- Can stop or change actions if needed  

---

## 🧠 Final Summary

- Middleware = middle layer between dispatch & reducer  
- Used for async, logging, side effects  
- Common ones: Thunk, Saga  
- Built-in in Redux Toolkit  