# React Router `useHistory` vs `useNavigate`

`useHistory` is a React Router hook used in **older versions (React
Router v5)** to control browser history and navigate between pages.

⚠️ In **React Router v6**, `useHistory` was **removed** and replaced
with **`useNavigate`**.

Most modern React projects use **React Router v6**, so you normally use
**`useNavigate`** instead.

------------------------------------------------------------------------

# 1️⃣ `useHistory` (React Router v5)

### Example

``` jsx
import { useHistory } from "react-router-dom";

function Home() {
  const history = useHistory();

  const goToAbout = () => {
    history.push("/about");
  };

  return (
    <button onClick={goToAbout}>
      Go to About
    </button>
  );
}
```

### Main Methods

  Method                        Meaning
  ----------------------------- -------------------------
  `history.push("/about")`      go to another page
  `history.replace("/about")`   replace current history
  `history.goBack()`            go back
  `history.goForward()`         go forward

------------------------------------------------------------------------

# 2️⃣ `useNavigate` (React Router v6)

Same concept, but **new syntax**.

### Example

``` jsx
import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <button onClick={() => navigate("/about")}>
      Go to About
    </button>
  );
}
```

------------------------------------------------------------------------

# 3️⃣ Simple Comparison

  -----------------------------------------------------------------------------
  React Router v5                     React Router v6
  ----------------------------------- -----------------------------------------
  `useHistory()`                      `useNavigate()`

  `history.push("/about")`            `navigate("/about")`

  `history.replace("/about")`         `navigate("/about", { replace: true })`

  `history.goBack()`                  `navigate(-1)`
  -----------------------------------------------------------------------------

------------------------------------------------------------------------

# 4️⃣ Easy Way to Remember

    Old React Router → useHistory
    New React Router → useNavigate

------------------------------------------------------------------------

Since you're working on **React for your Brototype projects**, you're
almost certainly using **React Router v6**, so focus on
**`useNavigate`**, not `useHistory`.