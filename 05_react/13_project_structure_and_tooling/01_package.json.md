# package.json

`package.json` is a configuration file for **Node.js projects** (like
React, Express, etc.).
It tells **npm (Node Package Manager)** about your project.

Think of it like the **identity card of your project 📦**.

It contains:

-   Project name
-   Version
-   Dependencies (libraries your app uses)
-   Scripts (commands to run your project)
-   Author
-   License
-   Other metadata

------------------------------------------------------------------------

# Example of a package.json

``` json
{
  "name": "my-react-app",
  "version": "1.0.0",
  "description": "My first React project",
  "main": "index.js",
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "author": "Emmanuel",
  "license": "ISC"
}
```

------------------------------------------------------------------------

# Important Parts

## 1️⃣ name

Project name.

``` json
"name": "my-react-app"
```

------------------------------------------------------------------------

## 2️⃣ version

Version of your project.

``` json
"version": "1.0.0"
```

------------------------------------------------------------------------

## 3️⃣ scripts

Commands you can run with **npm**.

Example:

``` json
"scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build"
}
```

Run them like:

``` bash
npm start
npm run build
```

------------------------------------------------------------------------

## 4️⃣ dependencies

Libraries your project needs.

``` json
"dependencies": {
  "react": "^18.2.0",
  "axios": "^1.6.0"
}
```

Install them with:

``` bash
npm install
```

------------------------------------------------------------------------

## 5️⃣ devDependencies

Packages needed **only for development**.

Example:

``` json
"devDependencies": {
  "nodemon": "^3.0.0"
}
```

------------------------------------------------------------------------

# How package.json is created

Run:

``` bash
npm init
```

or quickly:

``` bash
npm init -y
```

------------------------------------------------------------------------

# Simple Understanding

    package.json
         ↓
    List of everything your project needs
         ↓
    npm reads it
         ↓
    Installs dependencies
         ↓
    Runs scripts

------------------------------------------------------------------------

Since you are learning **React and Django**, you'll see `package.json`
in **every React project**.

Example commands you probably use:

``` bash
npm install
npm start
npm run build
```

All of these come from **package.json**.