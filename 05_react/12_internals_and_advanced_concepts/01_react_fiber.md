
# React Fiber Overview

React Fiber is the new internal engine (reconciliation algorithm) that React uses to update the UI efficiently.

Think of it like this:

👉 **React Fiber = the brain that decides how and when React updates the UI.**

It was introduced in **React 16** to make rendering faster, smoother, and interruptible.

---

## 1️⃣ Why React Fiber was created

Before Fiber (old React):

React used a **stack-based reconciliation system**.

### Problem

- Rendering was **synchronous**
- Once rendering started, React **could not pause**
- Large UI updates could **block the browser**

### Example

If React updates **1000 components**, it must finish all of them before the browser can do anything else.

### Result

- UI freezes
- Scroll lag
- Poor performance

---

## 2️⃣ What React Fiber solves

React Fiber allows React to:

- ✅ Pause work
- ✅ Split work into small units
- ✅ Prioritize important updates
- ✅ Resume work later

### Example priorities

| Priority | Example |
|--------|--------|
| High | Typing in input |
| Medium | Animation |
| Low | Loading background data |

So React can say:

> "User typing is important — render that first."

---

## 3️⃣ Work in small pieces (Core idea)

Fiber breaks rendering into **small tasks**.

### Old React

Update the **whole component tree at once**

### Fiber React

Update **small pieces of the component tree**

Example tree:

```
App
 ├ Navbar
 ├ Sidebar
 └ Dashboard
      ├ Chart
      └ Table
```

Fiber may render like this:

1. Navbar
2. Pause
3. Sidebar
4. Pause
5. Dashboard

This keeps the browser **responsive**.

---

## 4️⃣ What a Fiber is

A **Fiber** is a JavaScript object representing a component.

Example Fiber structure:

```javascript
{
  type: Component,
  stateNode: DOM element,
  child: next child fiber,
  sibling: next sibling fiber,
  return: parent fiber
}
```

So React creates a **Fiber tree** instead of a normal component tree.

---

## 5️⃣ Fiber Tree Example

Component tree:

```
App
 ├ Header
 └ Profile
      ├ Avatar
      └ Bio
```

Fiber tree stores relationships like:

```
App
 ↓ child
Header
 ↓ sibling
Profile
 ↓ child
Avatar
 ↓ sibling
Bio
```

This structure allows React to **traverse efficiently**.

---

## 6️⃣ Two Phases in Fiber

### 1. Render Phase (Reconciliation)

React calculates **what changes are needed**.

Example:

```
Old UI → New UI
```

React compares them.

✅ This phase **can pause**.

### 2. Commit Phase

React updates the **real DOM**.

Examples:

- add element
- remove element
- update element

❌ This phase **cannot pause**.

---

## 7️⃣ Simple analogy

Imagine **cleaning a big house**.

### Old React

Clean the **entire house without stopping**.

### Fiber

- Clean one room
- Take a break
- Clean next room
- Take a break

So the house work **doesn't block everything else**.

---

## 8️⃣ Features enabled by Fiber

Fiber made possible:

- Concurrent Rendering
- Suspense
- Transitions
- Better animations
- Time slicing

All modern React performance features **depend on Fiber**.

---

## ✅ In one line

**React Fiber is the internal engine that allows React to update the UI in small, prioritized, interruptible units of work.**