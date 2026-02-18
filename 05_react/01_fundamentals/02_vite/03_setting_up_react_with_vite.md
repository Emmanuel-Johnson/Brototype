# ⚡ Setting Up React with Vite

We'll go step-by-step.

------------------------------------------------------------------------

## ✅ 1️⃣ Make Sure Node.js Is Installed

Check version:

``` bash
node -v
```

If not installed → download from: 👉 https://nodejs.org

------------------------------------------------------------------------

## 🚀 2️⃣ Create a New React App Using Vite

Run this:

``` bash
npm create vite@latest
```

It will ask:

-   Project name → my-react-app
-   Framework → React
-   Variant → JavaScript (or TypeScript)

------------------------------------------------------------------------

## 📦 3️⃣ Go Inside Project Folder

``` bash
cd my-react-app
```

------------------------------------------------------------------------

## 📥 4️⃣ Install Dependencies

``` bash
npm install
```

This installs:

-   React
-   React DOM
-   Vite
-   Required packages

------------------------------------------------------------------------

## ▶️ 5️⃣ Start Development Server

``` bash
npm run dev
```

You'll see something like:

    Local: http://localhost:5173/

Open it in browser 🎉

Boom. React + Vite running.

------------------------------------------------------------------------

## 📁 Project Structure (Simple View)

    my-react-app/
     ├── index.html
     ├── src/
     │    ├── main.jsx
     │    └── App.jsx
     ├── vite.config.js
     └── package.json

### Important Files:

-   main.jsx → Entry point
-   App.jsx → Main component
-   vite.config.js → Vite configuration

------------------------------------------------------------------------

## 🏗 Production Build

When you're ready to deploy:

``` bash
npm run build
```

It creates a `dist/` folder with optimized files.

Vite uses Rollup internally for production optimization.

------------------------------------------------------------------------

## 🧠 Why This Is Better Than CRA

-   Instant dev server ⚡
-   Faster hot reload
-   Cleaner config
-   Modern setup

------------------------------------------------------------------------

## 🎯 Interview Answer (Short Version)

> To set up React with Vite, use `npm create vite@latest`, select React,
> install dependencies with `npm install`, and start the server using
> `npm run dev`.