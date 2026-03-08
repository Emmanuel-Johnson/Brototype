# Dependency Management

Dependency management means handling the **external libraries/packages
your project needs to run**. 📦

In modern JavaScript projects (like React), we rarely write everything
from scratch.
We use libraries like **React, Axios, Lodash**, etc. Managing them
properly is called **dependency management**.

------------------------------------------------------------------------

# 1️⃣ What is a Dependency?

A **dependency** is a package your project depends on.

Example:

    React app
       ↓
    react
    react-dom
    axios

Your project needs these packages to work, so they are called
**dependencies**.

Example in `package.json`:

``` json
"dependencies": {
  "react": "^18.2.0",
  "axios": "^1.6.0"
}
```

------------------------------------------------------------------------

# 2️⃣ Why Dependency Management is Important

Without dependency management:

-   Developer A → installs version 1
-   Developer B → installs version 2
-   Production → installs version 3

The app may break or behave differently.

Dependency management ensures:

-   Same versions for everyone
-   Easy installation
-   Organized project
-   Avoid conflicts

------------------------------------------------------------------------

# 3️⃣ Tools Used for Dependency Management

In Node.js projects we use:

-   npm
-   yarn
-   pnpm

In most React projects you will commonly use:

    npm

Example:

``` bash
npm install axios
```

------------------------------------------------------------------------

# 4️⃣ Files Used in Dependency Management

## package.json

Lists required packages.

Example:

``` json
"dependencies": {
  "react": "^18.2.0"
}
```

## package-lock.json

Locks the **exact versions**.

Example:

    react → 18.2.0

## node_modules

Folder that contains **all installed packages**.

Example:

    node_modules/
       react/
       axios/
       lodash/

------------------------------------------------------------------------

# 5️⃣ Installing Dependencies

Install all dependencies:

``` bash
npm install
```

Install a single package:

``` bash
npm install axios
```

Install a dev dependency:

``` bash
npm install nodemon --save-dev
```

------------------------------------------------------------------------

# 6️⃣ Dependency vs DevDependency

## Dependencies

Needed to **run the app**.

Examples:

-   react
-   axios
-   express

## DevDependencies

Needed **only during development**.

Examples:

-   eslint
-   nodemon
-   webpack

------------------------------------------------------------------------

# ✅ Simple Summary

Dependency management =
Managing libraries your project uses.

Using:

-   `package.json`
-   `package-lock.json`
-   `node_modules`
-   `npm`