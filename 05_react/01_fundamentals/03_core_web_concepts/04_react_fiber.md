# ⚡ What is React Fiber?

React Fiber is the new reconciliation engine of React.

It was introduced in:

👉 React version 16.

Before that, React's rendering was synchronous and blocking.

Fiber changed everything.

------------------------------------------------------------------------

# 🧠 Why React Fiber Was Created

## Old React problem:

When state changes:

1.  React builds new Virtual DOM
2.  Compares with old Virtual DOM
3.  Updates real DOM

All in one go.

If the component tree is big...

🚨 UI freezes.

You couldn't:

-   Pause work
-   Prioritize work
-   Split work

That's bad for large apps.

------------------------------------------------------------------------

# 🔥 What Fiber Does

React Fiber allows:

-   Splitting rendering work into chunks
-   Pausing work
-   Resuming later
-   Prioritizing important updates
-   Non-blocking rendering

In simple words:

> Fiber makes React asynchronous and interruptible.

------------------------------------------------------------------------

# 🏗️ Before vs After Fiber

## ❌ Old React (Stack Reconciler)

    Update → Render entire tree → Commit → Done

Blocking. All at once.

------------------------------------------------------------------------

## ✅ React Fiber

    Update
       ↓
    Break work into small units
       ↓
    Pause if needed
       ↓
    Resume
       ↓
    Commit only necessary changes

Smooth. Smart.

------------------------------------------------------------------------

# 🧩 What is a "Fiber"?

A Fiber is a JavaScript object representing a unit of work.

Each component becomes a Fiber node.

So instead of a simple Virtual DOM tree, React now uses a:

👉 Fiber Tree

Each fiber stores:

-   Component type
-   Props
-   State
-   Parent
-   Child
-   Sibling
-   Effect info

It's like a smarter Virtual DOM node.

------------------------------------------------------------------------

# 🎯 Key Superpowers of Fiber

## 1️⃣ Time Slicing

React can pause rendering to let browser handle:

-   Animations
-   Scrolling
-   User input

So UI doesn't freeze.

------------------------------------------------------------------------

## 2️⃣ Priority Scheduling

Example:

-   User typing in input → HIGH priority
-   Loading hidden sidebar → LOW priority

Fiber lets React prioritize properly.

------------------------------------------------------------------------

## 3️⃣ Concurrent Rendering

With modern React (18+):

You can use features like:

``` js
startTransition()
```

That's powered by Fiber.

------------------------------------------------------------------------

# 🧠 Important: Fiber ≠ Virtual DOM

-   Virtual DOM → Concept
-   Fiber → Implementation of reconciliation

Fiber replaced the old reconciliation algorithm.

------------------------------------------------------------------------

# 🚀 Why This Matters

In your:

-   🛒 E-commerce app → filtering products
-   📚 LMS → switching lessons
-   📊 Admin dashboard → heavy UI

Without Fiber → UI might freeze
With Fiber → Smooth experience

Even if you don't see it, Fiber is working silently.

------------------------------------------------------------------------

# 🧠 Real Talk

You don't need to manually "use" Fiber.

But understanding it helps you:

-   Avoid heavy synchronous loops
-   Use `useTransition` properly
-   Understand why re-renders behave differently