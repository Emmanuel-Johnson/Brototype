# Debouncing in React ⚛️

Debouncing is a technique used to limit how often a function runs.

Instead of running the function every time an event happens, it waits
for a specific delay and runs only once after the user stops triggering
the event.

This is very useful for **search inputs, API calls, and performance
optimization.**

------------------------------------------------------------------------

# Problem Without Debouncing

Example: Search input

``` jsx
<input onChange={(e) => searchAPI(e.target.value)} />
```

If the user types:

    hello

The API calls happen like this:

    h     → API call
    he    → API call
    hel   → API call
    hell  → API call
    hello → API call

That means **5 API requests.**

This is inefficient.

------------------------------------------------------------------------

# With Debouncing

Debouncing waits until the user stops typing for a certain time.

Example delay: **500ms**

Now the flow becomes:

User typing
↓
User stops typing
↓ (500ms delay)
API call happens once

------------------------------------------------------------------------

# Example Using lodash.debounce

First install lodash debounce:

``` bash
npm install lodash.debounce
```

Example:

``` javascript
import debounce from "lodash.debounce";

const handleSearch = debounce((value) => {
  console.log("Searching:", value);
}, 500);

function App() {
  return (
    <input
      type="text"
      onChange={(e) => handleSearch(e.target.value)}
    />
  );
}
```

Now the API call runs **only once after 500ms of inactivity.**

------------------------------------------------------------------------

# Visualization

### Without debounce

    Typing → API → API → API → API

### With debounce

    Typing → wait → API

------------------------------------------------------------------------

# Real Project Example

Search bar in an e-commerce site:

``` javascript
const handleSearch = debounce((query) => {
  fetch(`/api/products?q=${query}`);
}, 500);

<input
  type="text"
  onChange={(e) => handleSearch(e.target.value)}
/>
```

This prevents **too many API calls.**

------------------------------------------------------------------------

# Where Debouncing is Used

Common use cases:

-   Search inputs
-   Autocomplete
-   API requests
-   Window resize events
-   Scroll events

------------------------------------------------------------------------

# Debounce vs Throttle

  Feature     Debounce                  Throttle
  ----------- ------------------------- ---------------------
  Execution   After user stops action   Runs every interval
  Example     Search input              Scroll tracking

Example:

-   **Debounce** → wait for pause
-   **Throttle** → run every X seconds

------------------------------------------------------------------------

# 💡 Interview Definition

**Debouncing is a technique used to delay the execution of a function
until after a specified time has passed since the last event trigger.**