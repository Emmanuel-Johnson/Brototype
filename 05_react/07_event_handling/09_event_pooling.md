# Event Pooling in React ⚛️

Event Pooling was a performance optimization used in older versions of
React.

Instead of creating a new event object every time an event occurs, React
would reuse the same event object for multiple events.

This was done to reduce memory usage and improve performance.

------------------------------------------------------------------------

# How Event Pooling Worked (Old React)

When an event happened:

User click
↓
React creates SyntheticEvent
↓
Event handler runs
↓
React clears event properties
↓
Event object reused

After the handler finished, React **nullified the event properties**.

------------------------------------------------------------------------

# Example

``` javascript
function handleClick(e) {
  console.log(e.target); // works

  setTimeout(() => {
    console.log(e.target); // ❌ null in old React
  }, 1000);
}
```

### Why?

Because React **recycled the event object**.

After the handler completed:

    e.target → null
    e.type → null

------------------------------------------------------------------------

# How Developers Fixed It (Old React)

To keep the event, developers used:

    e.persist();

### Example

``` javascript
function handleClick(e) {
  e.persist();

  setTimeout(() => {
    console.log(e.target); // works
  }, 1000);
}
```

`persist()` told React:

> Do NOT reuse this event object

------------------------------------------------------------------------

# React 17+ (Modern React)

Event pooling was **removed in React 17**.

Now:

-   Events are **not reused**
-   Event properties remain accessible
-   `e.persist()` is **no longer needed**

### Example

``` javascript
function handleClick(e) {
  setTimeout(() => {
    console.log(e.target); // works fine
  }, 1000);
}
```

------------------------------------------------------------------------

# Quick Comparison

  React Version   Event Pooling
  --------------- -----------------
  React ≤16       Used pooling
  React 17+       Removed pooling

------------------------------------------------------------------------

# Simple Way to Remember

### Old React

Event created
↓
Handler runs
↓
Event cleared and reused

### Modern React

Event created
↓
Handler runs
↓
Event stays available

------------------------------------------------------------------------

# 💡 Interview Answer

**Event pooling was a performance optimization in older versions of
React where SyntheticEvent objects were reused by clearing their
properties after the event handler executed. This was removed in React
17.**