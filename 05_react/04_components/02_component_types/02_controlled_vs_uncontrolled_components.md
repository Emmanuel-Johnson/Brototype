# 🧠 Controlled vs Uncontrolled Components (Forms in React)

This concept is mainly about form inputs.

It answers one question:

👉 **Who controls the input value? React or the DOM?**

------------------------------------------------------------------------

## 🔵 1️⃣ Controlled Component

A controlled component is when:

-   ✅ React controls the input value
-   ✅ The value is stored in state
-   ✅ `onChange` updates state

### Example:

``` jsx
import { useState } from "react";

const LoginForm = () => {
  const [email, setEmail] = useState("");

  return (
    <input
      type="email"
      value={email}
      onChange={(e) => setEmail(e.target.value)}
    />
  );
};
```

### What's happening?

-   The input value comes from `email` state
-   When user types → `onChange` updates state
-   State updates → UI re-renders

React is in control.

------------------------------------------------------------------------

## 💪 Why Controlled is Powerful

-   ✅ Easy validation
-   ✅ Easy error handling
-   ✅ Can disable button conditionally
-   ✅ Can show live preview
-   ✅ Cleaner production logic

In serious apps → we use controlled inputs.

------------------------------------------------------------------------

## 🔴 2️⃣ Uncontrolled Component

An uncontrolled component is when:

-   ❌ React does NOT control the value
-   ❌ The DOM handles it
-   ❌ We use `ref` to read value

### Example:

``` jsx
import { useRef } from "react";

const LoginForm = () => {
  const emailRef = useRef();

  const handleSubmit = () => {
    console.log(emailRef.current.value);
  };

  return (
    <>
      <input type="email" ref={emailRef} />
      <button onClick={handleSubmit}>Submit</button>
    </>
  );
};
```

### Here:

-   The input manages itself
-   We only read the value when needed
-   DOM is in control

------------------------------------------------------------------------

## ⚖️ Controlled vs Uncontrolled

  Controlled                  Uncontrolled
  --------------------------- -------------------------
  Uses `useState`             Uses `useRef`
  React controls value        DOM controls value
  Better for validation       Simpler for quick forms
  Most common in production   Less common

------------------------------------------------------------------------

## 🏗 Real Example (Your Projects)

### 🛒 Checkout Form

Should be **controlled** (validation, errors, payment flow)

### 🎓 LMS Login

Definitely controlled.

------------------------------------------------------------------------

## 🎯 Final Takeaway

Production apps = mostly **controlled components**.