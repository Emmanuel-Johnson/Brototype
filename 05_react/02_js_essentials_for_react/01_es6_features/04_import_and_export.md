# 🔹 Why Import / Export?

Before ES6, everything was in one file or messy script tags.

Now we can:

-   Split code into multiple files
-   Reuse functions
-   Keep code organized
-   Build scalable apps

This is called **Modules**.

------------------------------------------------------------------------

# 🟦 1️⃣ Named Export

You can export multiple things from one file.

📁 math.js

``` js
export const add = (a, b) => a + b;

export const subtract = (a, b) => a - b;
```

📁 app.js

``` js
import { add, subtract } from "./math.js";

console.log(add(5, 3));
```

### Important:

-   Use `{}` when importing named exports
-   Names must match exactly

### Rename While Importing

``` js
import { add as sum } from "./math.js";
```

------------------------------------------------------------------------

# 🟦 2️⃣ Default Export

Only **ONE** default export per file.

📁 greet.js

``` js
export default function greet() {
  console.log("Hello");
}
```

📁 app.js

``` js
import greet from "./greet.js";

greet();
```

-   No `{}` needed
-   You can rename it anything

``` js
import myFunction from "./greet.js";
```

Because default export has no fixed name.

------------------------------------------------------------------------

# 🟦 3️⃣ Export All at Once

Instead of:

``` js
export const a = 1;
export const b = 2;
```

You can do:

``` js
const a = 1;
const b = 2;

export { a, b };
```

------------------------------------------------------------------------

# 🟦 4️⃣ Import Everything

``` js
import * as math from "./math.js";

console.log(math.add(2, 3));
```

Good when there are many exports.

------------------------------------------------------------------------

# 🧠 Named vs Default (Simple Difference)

  Named Export      Default Export
  ----------------- -------------------
  Can export many   Only one
  Must use `{}`     No `{}`
  Name must match   Can rename freely

------------------------------------------------------------------------

# 🔥 React Example (You See This Daily)

``` js
// App.jsx
export default function App() {
  return <h1>Hello</h1>;
}

// main.jsx
import App from "./App";
```

Also:

``` js
import { useState } from "react";
```

That is a named import.

------------------------------------------------------------------------

# 🔹 Important Rules

✅ Always use relative path `./` for local files
✅ Use no `./` for npm packages
✅ Only one default export per file
✅ Add `.js` in vanilla JS (Vite handles automatically sometimes)

------------------------------------------------------------------------

# 🔥 Interview Definition

Import and Export are ES6 module features that allow splitting code into
reusable files and sharing functionality between them.