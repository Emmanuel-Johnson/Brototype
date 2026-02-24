# 📦 Lists in JSX

In React, we render lists using JavaScript's `.map()`.

Why?

Because `.map()` returns a new array --- and JSX can render arrays of
elements.

------------------------------------------------------------------------

## ✅ Basic Example

``` jsx
const numbers = [1, 2, 3];

<ul>
  {numbers.map(num => (
    <li key={num}>{num}</li>
  ))}
</ul>
```

### What happens:

-   `.map()` loops through each number
-   Returns `<li>` elements
-   React renders them

**Output:**

    1
    2
    3

------------------------------------------------------------------------

## 🗝️ What Are Keys?

Keys are special props that help React identify which item changed,
added, or removed.

Think of keys like:

> "ID card for each element in the list"

Without keys, React gets confused when updating the UI.

------------------------------------------------------------------------

## 🚫 Without Key (Bad)

``` jsx
{numbers.map(num => (
  <li>{num}</li>
))}
```

React will show warning:

⚠ "Each child in a list should have a unique key prop."

------------------------------------------------------------------------

## ✅ With Key (Correct)

``` jsx
{numbers.map(num => (
  <li key={num}>{num}</li>
))}
```

------------------------------------------------------------------------

## 🧠 Why Keys Are Important

Imagine your eCommerce cart:

``` jsx
const cart = [
  { id: 1, name: "Laptop" },
  { id: 2, name: "Phone" }
];

{cart.map(item => (
  <div key={item.id}>
    {item.name}
  </div>
))}
```

If user removes "Laptop":

React uses the key to know exactly which item disappeared.

Without key → React may re-render incorrectly.

------------------------------------------------------------------------

## ❌ Don't Use Index as Key (Usually)

``` jsx
{items.map((item, index) => (
  <li key={index}>{item.name}</li>
))}
```

This can cause bugs when:

-   Items are reordered
-   Items are deleted
-   Items are inserted

For your LMS project, always use:

``` jsx
key={item.id}
```

Real database ID is best.

------------------------------------------------------------------------

## 💡 Real LMS Example

``` jsx
{courses.map(course => (
  <CourseCard key={course.id} course={course} />
))}
```

Clean. Professional. Scalable.

------------------------------------------------------------------------

## 🔥 Mental Model

-   `.map()` → Converts array → JSX elements
-   `key` → Unique identifier for each element
-   Use stable unique IDs
-   Never random values