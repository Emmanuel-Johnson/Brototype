# 🚀 What is Redux?

Redux is a state management library used mainly in React apps to manage and share data across components.

---

## 🧠 In Plain English

Instead of passing data manually through props from parent → child → child (called **prop drilling**), Redux gives you:

👉 One central place (**store**) to keep all your app data

Any component can:

- 📥 Read data from it  
- 📤 Update data in it  

---

## 🏗️ Core Idea (3 Things)

### 1. Store

👉 The global state container

```js
const store = {
  movies: [],
  user: {}
};
```

---

### 2. Actions

👉 What you want to do

```js
{ type: "ADD_MOVIE", payload: "Inception" }
```

---

### 3. Reducer

👉 A function that updates state based on action

```js
(state, action) => {
  if (action.type === "ADD_MOVIE") {
    state.movies.push(action.payload);
  }
}
```

---

## 🔄 How It Works (Flow)

1. Component sends an action  
2. Action goes to reducer  
3. Reducer updates the store  
4. UI automatically updates  

👉 Simple flow:

UI → Action → Reducer → Store → UI updates

---

## 🤔 Why Use Redux?

You use Redux when:

- Your app has lots of shared state  
- Props become messy (**prop drilling 😵‍💫**)  
- You want predictable state changes  

---

## ⚠️ When NOT to Use Redux

Don’t use Redux if:

- Your app is small  
- Only a few components need data  

👉 In that case, just use:

- `useState`  
- `useContext`  

---

## 💡 Modern Redux (Important for You)

Since you're learning React + Redux:

👉 Use **Redux Toolkit (RTK)** — NOT old Redux

### Why?

- Less code  
- Easier to understand  
- Industry standard now  

---

## 🎯 Bottom Line

👉 Redux = centralized state management  
👉 Helps avoid messy props  
👉 Makes large apps easier to manage  