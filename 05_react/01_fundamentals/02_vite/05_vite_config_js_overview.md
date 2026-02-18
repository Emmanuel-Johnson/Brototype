# ⚙️ What is `vite.config.js`?

It's the configuration file for **Vite**.

This file tells Vite:

-   How to build your app
-   Which plugins to use
-   Dev server settings
-   Path aliases
-   Proxy settings

Think of it as:

> **"Control center of your Vite project."**

------------------------------------------------------------------------

# 📁 Basic Example

When you create a React project, you'll see something like:

``` js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
})
```

Let's break this down.

------------------------------------------------------------------------

# 🔌 1️⃣ Plugins

``` js
plugins: [react()]
```

This enables React support.

It uses:

-   `@vitejs/plugin-react`
-   JSX transformation
-   Fast Refresh (HMR)

Without this → React won't work.

------------------------------------------------------------------------

# 🌐 2️⃣ Server Configuration

You can configure dev server like this:

``` js
server: {
  port: 3000,
  open: true
}
```

-   `port` → changes default 5173
-   `open` → auto opens browser

Useful for development.

------------------------------------------------------------------------

# 🔁 3️⃣ Proxy (Very Important for Django)

``` js
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true,
    }
  }
}
```

Now when you call:

``` js
fetch('/api/products')
```

Vite forwards it to Django.

No CORS headache 🔥

------------------------------------------------------------------------

# 🛤 4️⃣ Path Aliases (Cleaner Imports)

Instead of:

``` js
import Navbar from '../../../components/Navbar'
```

You can configure:

``` js
resolve: {
  alias: {
    '@': '/src',
  }
}
```

Then import like:

``` js
import Navbar from '@/components/Navbar'
```

Much cleaner.

------------------------------------------------------------------------

# 📦 5️⃣ Build Configuration

You can customize production build:

``` js
build: {
  outDir: 'build',
  sourcemap: true
}
```

Vite uses **Rollup** internally for production builds.

------------------------------------------------------------------------

# 🎯 Why `vite.config.js` Matters

For small demos → not important.

For real projects (like LMS + E-commerce):

-   Proxy setup for Django
-   Clean import paths
-   Custom build output
-   Environment control

This file becomes powerful.

------------------------------------------------------------------------

# 🧠 Interview One-Liner

> `vite.config.js` is the configuration file used to customize Vite's
> development server, plugins, build process, and module resolution.