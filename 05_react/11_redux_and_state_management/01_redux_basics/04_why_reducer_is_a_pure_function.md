# 🧠 Why Reducer is a Pure Function?

## ⚙️ First — what is a pure function?

A pure function means:

- Same input → same output ✅  
- No side effects ❌  
- Doesn’t modify external data ❌  

**Example:**

```js
function add(a, b) {
  return a + b;
}
```

👉 Always predictable ✔️

---

## 🔥 Now — Reducer in Redux

A reducer:

```js
(state, action) => newState
```

👉 It takes:

- current state  
- action  

👉 Returns:

- new updated state  

---

## 🎯 Why MUST it be pure?

### 1️⃣ Predictability (Most Important)

If reducer is pure:

👉 Same state + same action → same result

```js
(state = { count: 0 }, action) => {
  if (action.type === "INCREMENT") {
    return { count: state.count + 1 };
  }
}
```

👉 Always gives correct result  
👉 No surprises  

---

### 2️⃣ Easy Debugging 🐞

Redux has tools like time travel debugging

👉 You can:

- Go back to previous states  
- Replay actions  

👉 This ONLY works if reducers are pure  

---

### 3️⃣ No Side Effects 🚫

Reducer should NOT:

- Call API ❌  
- Use setTimeout ❌  
- Change global variables ❌  

❌ **Wrong:**

```js
(state, action) => {
  fetch("/api/data"); // ❌ side effect
  return state;
}
```

👉 This makes behavior unpredictable  

---

### 4️⃣ Immutability (No direct changes)

Reducers should NOT mutate state directly:

❌ **Wrong:**

```js
state.count++;
```

✅ **Correct:**

```js
return {
  ...state,
  count: state.count + 1
};
```

👉 This keeps state history safe  

---

## 🤯 But wait… in Redux Toolkit you DO mutate?

You’ve probably seen this:

```js
state.count++;
```

👉 Looks like mutation 😵‍💫  

But internally:

👉 Redux Toolkit uses **Immer**

👉 It converts it into safe immutable updates  

👉 So still follows pure function rules ✅  

---

## 🔁 Simple Analogy

Think reducer like a calculator:

- Input: numbers + operation  
- Output: result  

👉 Calculator doesn’t:

- Call someone 📞  
- Change outside world 🌍  
- Do random things  

👉 It just calculates → same result every time  

---

## 🎯 Final One-Line Answer (for interview)

👉 **“A reducer is a pure function to ensure predictable, testable, and side-effect-free state updates.”**