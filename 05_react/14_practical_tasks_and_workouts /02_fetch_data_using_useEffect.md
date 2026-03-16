## 1️⃣ Basic Example – Fetch Data with useEffect

```javascript
import { useState, useEffect } from "react";

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => {
        setUsers(data);
      });
  }, []);

  return (
    <div>
      <h1>User List</h1>
      {users.map((user) => (
        <p key={user.id}>{user.name}</p>
      ))}
    </div>
  );
}

export default App;
```

---

# 2️⃣ How This Works

## useState

```javascript
const [users, setUsers] = useState([]);
```

* Stores the fetched data.
* Initially an empty array.

---

## useEffect

```javascript
useEffect(() => {
```

* Runs **after the component renders**.

---

## fetch()

```javascript
fetch("https://jsonplaceholder.typicode.com/users")
```

* Sends a **GET request** to the API.

---

## Convert Response to JSON

```javascript
.then((response) => response.json())
```

* Converts the **Response object → JavaScript object**.

---

## Save Data to State

```javascript
.then((data) => {
  setUsers(data);
});
```

* Stores API data inside React state.

---

## Dependency Array

```javascript
}, []);
```

Empty array means:

* ✅ Runs **only once**
* ✅ Similar to **componentDidMount** in class components

---

# 3️⃣ Flow (Important)

```
Component renders
       ↓
useEffect runs
       ↓
API call happens
       ↓
Data received
       ↓
setUsers(data)
       ↓
Component re-renders with data
```

---

# 4️⃣ Modern Way (Async / Await)

Cleaner version:

```javascript
import { useState, useEffect } from "react";

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("https://jsonplaceholder.typicode.com/users");
      const data = await response.json();
      setUsers(data);
    }

    fetchData();
  }, []);

  return (
    <div>
      {users.map((user) => (
        <p key={user.id}>{user.name}</p>
      ))}
    </div>
  );
}

export default App;
```

---

# 5️⃣ Very Important Rule

❌ Don't do this:

```javascript
useEffect(async () => {
```

React **does not allow async directly inside useEffect**.

Instead:

✅ Create an async function inside useEffect.

```javascript
useEffect(() => {
  async function fetchData() {}
  fetchData();
}, []);
```

---

# 6️⃣ Real Example Used in Projects

In projects like **LMS** or **E-commerce**:

```javascript
useEffect(() => {
  fetch("http://localhost:5000/products")
    .then((res) => res.json())
    .then((data) => setProducts(data));
}, []);
```

---

💡 **Interview Tip**

`useEffect` is used to handle **side effects** in React.

Examples:

* API calls
* Timers
* Subscriptions
* DOM manipulation
