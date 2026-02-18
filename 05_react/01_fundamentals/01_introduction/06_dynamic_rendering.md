# 🌐 What is Dynamic Rendering?

## Definition

Dynamic Rendering = Serving different versions of a page depending on
who is requesting it.

Usually:

-   👤 Normal users → CSR version (JavaScript app)
-   🤖 Search engine bots → SSR pre-rendered HTML

So the server checks:

"Is this a real user or a search engine crawler?"

And then responds differently.

------------------------------------------------------------------------

## 🧠 Why Was It Created?

### The Problem

SPAs (like normal React apps) use CSR.

Search engines sometimes struggle with:

-   JavaScript-heavy content
-   Delayed rendering
-   Empty initial HTML

So developers created dynamic rendering as a workaround.

------------------------------------------------------------------------

## 🔧 How It Works (Step-by-Step)

1.  Request comes in
2.  Server detects user-agent
3.  If Google bot → send pre-rendered HTML
4.  If real user → send normal React app

### Tools Used

-   Next.js
-   Prerender.io

------------------------------------------------------------------------

## 🎯 Simple Example

Imagine your e-commerce site:

👤 Real user:

-   Gets React SPA experience (smooth navigation)

🤖 Google bot:

-   Gets fully rendered HTML for indexing

Same URL. Different output.

------------------------------------------------------------------------

## ⚖️ Why It's Not Always Recommended Now

Google officially recommends:

👉 Use proper SSR or Static Generation instead.

Dynamic rendering is considered:

-   A workaround
-   Not the cleanest long-term solution

Modern frameworks like:

-   SSR
-   SSG (Static Site Generation)
-   Hybrid rendering

solve this properly.

So dynamic rendering is less popular now.

------------------------------------------------------------------------

## 🔥 When Would You Use It?

-   Large legacy SPA
-   SEO problems
-   Cannot rewrite entire app
-   Need quick SEO fix

------------------------------------------------------------------------

## 🧠 Interview One-Line Answer

> Dynamic rendering is a technique where the server sends pre-rendered
> HTML to search engine bots and a client-side rendered app to regular
> users to improve SEO.