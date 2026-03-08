# Basic React Project Structure

A simple and commonly used structure:

```
my-app
│
├── node_modules
├── index.html
│
├── src
│   ├── components
│   ├── pages
│   ├── hooks
│   ├── services
│   ├── utils
│   ├── assets
│   ├── App.jsx
│   └── main.jsx
│
├── package.json
├── package-lock.json
└── README.md
```

This structure keeps the project organized and helps teams collaborate more easily. A well-structured React project improves readability, scalability, and maintainability. :contentReference[oaicite:0]{index=0}

---

# 1️⃣ `src` Folder (Most Important)

Everything related to your application lives inside `src`.

```
src
│
├── components
├── pages
├── hooks
├── services
├── utils
├── assets
```

The `src` folder usually contains the **main application files like `App.jsx` and the entry file (`main.jsx` or `index.js`)** which render the React app into the DOM. :contentReference[oaicite:1]{index=1}

---

# 2️⃣ Components Folder

Reusable UI components.

```
components
│
├── Button.jsx
├── Navbar.jsx
├── Card.jsx
```

Example:

```jsx
function Button() {
  return <button>Click</button>;
}
```

Best practice:

- Components should be **small**
- Components should be **reusable**

Reusable UI elements like buttons, inputs, and modals usually live inside the components folder. :contentReference[oaicite:2]{index=2}

---

# 3️⃣ Pages Folder

Each page of your application.

```
pages
│
├── Home.jsx
├── Login.jsx
├── Dashboard.jsx
```

Example routes:

```
/login
/dashboard
/profile
```

Pages represent **full screens**, not small UI parts.

---

# 4️⃣ Hooks Folder

Custom React hooks.

```
hooks
│
├── useAuth.js
├── useFetch.js
```

Example:

```javascript
function useAuth() {
  // authentication logic
}
```

Custom hooks help reuse logic across multiple components.

---

# 5️⃣ Services Folder

API calls or backend communication.

```
services
│
├── api.js
├── authService.js
```

Example:

```javascript
import axios from "axios";

export const getUsers = () => {
  return axios.get("/api/users");
};
```

Keeping API logic in services keeps components clean.

---

# 6️⃣ Utils Folder

Helper functions.

```
utils
│
├── formatDate.js
├── validation.js
```

Example:

```javascript
export function formatDate(date) {
  return new Date(date).toLocaleDateString();
}
```

Utilities contain reusable helper logic.

---

# 7️⃣ Assets Folder

Static files.

```
assets
│
├── images
├── icons
├── styles
```

Examples:

```
logo.png
background.jpg
```

Assets include images, icons, fonts, and other static resources.

---

# 8️⃣ Best Practices

## 1. Keep components small

One component = one responsibility.

Bad:

```
Dashboard.jsx → 800 lines
```

Good:

```
Dashboard
 ├ StatsCard
 ├ RecentOrders
 └ Chart
```

---

## 2. Use clear naming

Good:

```
UserCard.jsx
ProductList.jsx
AuthService.js
```

Bad:

```
file1.jsx
data.js
```

---

## 3. Group related files

Example:

```
components
 └ Navbar
     ├ Navbar.jsx
     ├ Navbar.css
     └ Navbar.test.js
```

---

## 4. Avoid deep nesting

Bad:

```
src/a/b/c/d/e/component.jsx
```

Good:

```
src/components/component.jsx
```

React projects should avoid too many nested folders because it becomes harder to navigate and maintain. :contentReference[oaicite:3]{index=3}

---

# Simple Real-World Structure (Used in Many Companies)

```
src
│
├── components
├── pages
├── layouts
├── hooks
├── services
├── utils
├── context
├── assets
├── routes
└── store
```

Large projects often add folders like **layouts, routes, context, and state stores** to handle scaling and team collaboration.