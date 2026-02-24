# 🚀 What is Dynamic Rendering?

In React, **dynamic rendering** means:

The UI changes automatically based on data or state.

Instead of hardcoding UI, you let data control what appears.

------------------------------------------------------------------------

## 🧱 Static vs Dynamic

### ❌ Static UI

``` jsx
<h1>Welcome Emmanuel</h1>
```

Always same output.

------------------------------------------------------------------------

### ✅ Dynamic UI

``` jsx
const user = "Emmanuel";

<h1>Welcome {user}</h1>
```

Now the UI depends on a variable.

Change `user` → UI changes.

------------------------------------------------------------------------

## 🧠 Where Dynamic Rendering Happens

### 1️⃣ Based on State

``` jsx
const [count, setCount] = useState(0);

<h1>{count}</h1>
<button onClick={() => setCount(count + 1)}>
  Increase
</button>
```

Click button → state updates → UI re-renders.

That's dynamic.

------------------------------------------------------------------------

### 2️⃣ Based on API Data

In your LMS:

``` jsx
{courses.map(course => (
  <CourseCard key={course.id} course={course} />
))}
```

If backend sends 3 courses → 3 cards
If backend sends 10 courses → 10 cards

UI adjusts automatically.

------------------------------------------------------------------------

### 3️⃣ Based on Conditions

``` jsx
{isLoggedIn ? <Dashboard /> : <Login />}
```

User logs in → different UI shows.

------------------------------------------------------------------------

### 4️⃣ Based on User Actions (eCommerce Example)

``` jsx
{cart.length === 0 ? (
  <p>Your cart is empty</p>
) : (
  <CartItems />
)}
```

Add item → UI changes
Remove item → UI changes

No page reload.

------------------------------------------------------------------------

## 🔥 Why React Feels "Magic"

When state changes:

-   React re-runs the component
-   Compares old UI vs new UI
-   Updates only what changed

That's why it feels instant.

------------------------------------------------------------------------

## 💡 Real Example (LMS)

Student enrolled → Show "Continue Course"
Not enrolled → Show "Buy Course"

``` jsx
{isEnrolled ? (
  <button>Continue</button>
) : (
  <button>Buy Now</button>
)}
```

That's dynamic rendering in real production apps.

------------------------------------------------------------------------

## 🧠 Simple Definition

Dynamic rendering =
👉 UI changes when data changes.