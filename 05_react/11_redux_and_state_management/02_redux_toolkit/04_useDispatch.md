# 🚀 What is useDispatch?

👉 **useDispatch** is a hook from React Redux

👉 It gives you the dispatch function so you can:

- ➡️ send actions to Redux  
- ➡️ update the store  

---

## 🧠 Simple Idea

```js
const dispatch = useDispatch();
```

👉 Now you can do:

```js
dispatch(action);
```

---

## 🔥 Basic Example

```js
import { useDispatch } from "react-redux";
import { addMovie } from "./movieSlice";

const AddMovie = () => {
  const dispatch = useDispatch();

  const handleAdd = () => {
    dispatch(addMovie({ id: 1, name: "Inception" }));
  };

  return <button onClick={handleAdd}>Add Movie</button>;
};
```

---

## 🧩 What’s happening?

- addMovie(...) → creates action  
- dispatch(...) → sends it to reducer  
- reducer updates state  
- UI updates automatically  

---

## ⚡ Flow (VERY IMPORTANT 🔥)

1. User clicks button  
2. dispatch(addMovie(...))  
3. Reducer runs  
4. Store updates  
5. useSelector triggers re-render  

👉 Full cycle complete 🔄  

---

## 🧠 With Async (Thunk)

```js
dispatch(fetchMovies());
```

👉 If it’s a thunk:

- runs async code  
- then dispatches real actions  

---

## 🔥 Multiple Dispatch

```js
dispatch({ type: "FETCH_START" });
dispatch({ type: "FETCH_SUCCESS" });
```

👉 Totally valid  

---

## ⚠️ Common Mistakes

❌ Forgetting to call dispatch  

```js
addMovie(...) // ❌ does nothing
```

❌ Calling dispatch incorrectly  

```js
dispatch(addMovie) // ❌ missing ()
```

---

## 🧠 Clean Pattern

```js
const dispatch = useDispatch();

const handleClick = () => {
  dispatch(addMovie("Interstellar"));
};
```

---

## ⚡ Real-Life Analogy

👉 Think Redux like a company 🏢

- useSelector → reading company data 📊  
- useDispatch → sending instructions 📨  
- reducer → worker processing it 👷  

---

## 🧠 Final Summary

👉 useDispatch:

- gives dispatch function  
- used to send actions  
- triggers state updates  

---

## 🔥 Pro Tip (For YOU)

👉 When building your projects:

- useDispatch → send action  
- useSelector → read updated state  

👉 That’s the core React + Redux loop  