# 🔁 What is Reusability in React?

Reusability means writing a component once and using it many times in
different places.

Instead of copying and pasting UI again and again...
You create one flexible component and reuse it.

That's clean architecture. That's professional code.

------------------------------------------------------------------------

## 🧱 Real Life Analogy

Think about a button.

Do you rewrite HTML every time you need a button?

No.

You create one `Button` component and reuse it everywhere.

------------------------------------------------------------------------

## 🧩 Basic Example

``` jsx
function Button({ text }) {
  return <button>{text}</button>;
}
```

Now you can reuse it like this:

``` jsx
<Button text="Login" />
<Button text="Register" />
<Button text="Buy Now" />
```

Same component.
Different data.

That's reusability.

------------------------------------------------------------------------

## 🔥 Real Example (Your E-commerce Project)

Instead of writing this 20 times:

``` jsx
<div>
  <h3>Product Name</h3>
  <p>₹999</p>
</div>
```

You create:

``` jsx
function ProductCard({ name, price }) {
  return (
    <div>
      <h3>{name}</h3>
      <p>₹{price}</p>
    </div>
  );
}
```

Now reuse:

``` jsx
<ProductCard name="iPhone" price={79999} />
<ProductCard name="Shoes" price={2999} />
<ProductCard name="Watch" price={1999} />
```

One component. Unlimited usage.

------------------------------------------------------------------------

## 🧠 Why Reusability is Powerful

Because it gives you:

-   ✅ Cleaner code
-   ✅ Less repetition
-   ✅ Easier maintenance
-   ✅ Faster development
-   ✅ Production-level architecture

If tomorrow you change styling in `ProductCard` →
All products update automatically.

That's professional thinking.