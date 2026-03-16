# 📝 Basic To-Do App (Enter + Display)

## 1️⃣ Basic To-Do App Code

```jsx
import { useState } from "react";

export default function App() {
  const [todo, setTodo] = useState("");
  const [todos, setTodos] = useState([]);

  function handleSubmit(e) {
    e.preventDefault();

    if (todo.trim() === "") return;

    setTodos((prev) => [...prev, todo]);
    setTodo("");
  }

  return (
    <div>
      <h2>To-Do App</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter todo"
          value={todo}
          onChange={(e) => setTodo(e.target.value)}
        />

        <button type="submit">Add</button>
      </form>

      <ul>
        {todos.map((t, index) => (
          <li key={index}>{t}</li>
        ))}
      </ul>
    </div>
  );
}
```

---

# 2️⃣ How It Works

## State

```js
const [todo, setTodo] = useState("");
```

Stores the **current input text**.

Example when user types:

```
"Buy milk"
```

---

```js
const [todos, setTodos] = useState([]);
```

Stores **all todos in an array**.

Example:

```
["Buy milk", "Study React", "Go gym"]
```

---

# 3️⃣ Input Field

```jsx
<input
  value={todo}
  onChange={(e) => setTodo(e.target.value)}
/>
```

### Flow

```
User types
   ↓
onChange runs
   ↓
setTodo() updates state
   ↓
Component re-renders
```

---

# 4️⃣ Adding Todo

```js
function handleSubmit(e) {
  e.preventDefault();

  setTodos((prev) => [...prev, todo]);
}
```

### Example

```
prev = ["Buy milk"]
todo = "Study React"
```

New array:

```
["Buy milk", "Study React"]
```

`prev` ensures we always use the **latest state**.

---

# 5️⃣ Display Todos

```jsx
{todos.map((t, index) => (
  <li key={index}>{t}</li>
))}
```

Example array:

```
["Buy milk", "Study React"]
```

Output:

```
• Buy milk
• Study React
```

---

# ✅ Flow of the App

```
User types todo
      ↓
todo state updates
      ↓
User clicks Add
      ↓
todo added to todos array
      ↓
Component re-renders
      ↓
todos.map() displays list
```
