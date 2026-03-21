# 🚀 What is Redux Thunk?

👉 **Redux Thunk** is a middleware that lets you write async logic (like API calls) inside Redux.

---

## 🧠 Why do we need it?

In normal Redux:

- Actions must be **plain objects**
- No async code allowed ❌

But in real apps, you often need to:

- Fetch data from APIs 🌐
- Wait for responses ⏳
- Then update state

👉 Problem:  
Reducers must be **pure functions** (no API calls)

👉 Solution:  
Use **Redux Thunk** to handle async logic *before* data reaches the reducer

---

## 🔥 Without Thunk (Normal Redux)

```js
dispatch({
  type: "ADD_MOVIES",
  payload: movies
});
```

👉 Works only if data is already available

---

## ⚡ With Redux Thunk

👉 Actions can return functions instead of objects:

```js
const fetchMovies = () => {
  return async (dispatch) => {
    const res = await fetch("/api/movies");
    const data = await res.json();

    dispatch({
      type: "ADD_MOVIES",
      payload: data
    });
  };
};
```

👉 Dispatch like this:

```js
dispatch(fetchMovies());
```

---

## 🧩 What’s happening here?

Step by step:

1. `fetchMovies()` returns a function  
2. Thunk intercepts it 🛑  
3. Runs async code  
4. Dispatches a normal action  

---

## 🧠 Key Concept

Thunk gives access to:

```js
(dispatch, getState)
```

### Example:

```js
const example = () => (dispatch, getState) => {
  const state = getState();
  console.log(state);
};
```

---

## 💡 Real-Life Analogy

👉 Without Thunk  
You can only send the **final result**

👉 With Thunk  
You can:

- Fetch data  
- Wait  
- Process it  
- THEN send result  

---

## ⚙️ Redux Toolkit (Important 🔥)

Good news 👀

👉 If you're using **Redux Toolkit**:

✅ Thunk is already included by default  
❌ No need to install anything  

---

## 🧪 Example in Redux Toolkit

```js
export const fetchMovies = () => async (dispatch) => {
  const res = await fetch("/api/movies");
  const data = await res.json();

  dispatch(addMovie(data));
};
```

---

## ⚠️ Important Points

- Reducers → ❌ No async  
- Thunk → ✅ Async allowed  
- Actions → Can be functions (because of Thunk)  

---

## 🧠 Quick Summary

- Redux Thunk = async logic handler  
- Lets actions be functions  
- Used for API calls, delays, side effects  
- Built into Redux Toolkit  