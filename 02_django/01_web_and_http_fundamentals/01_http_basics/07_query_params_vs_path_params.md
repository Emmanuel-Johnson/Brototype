> **“Query parameters and path parameters are two ways of sending data from the client to the server through the URL, but they serve very different purposes.”**

Understanding this difference shows **strong API design fundamentals**.

---

## 1️⃣ What Are Path Parameters?

> **“Path parameters are part of the URL path itself and are used to identify a specific resource.”**

### Example URL

```text
/users/42/
```

Here:
- `42` is a **path parameter**
- It identifies **which user** we want

### Key Characteristics

- **Mandatory**
- Used for **resource identification**
- Usually represent **IDs or unique values**
- Directly affect **URL routing**

### In Django

- Path parameters are captured in `urls.py`
- Passed directly to the **view function**

### Example Use Cases

- Get a user by ID  
- Get a product by ID  
- Get order details  

---

## 2️⃣ What Are Query Parameters?

> **“Query parameters are optional key–value pairs appended to the URL and are used to filter, sort, or modify the response.”**

### Example URL

```text
/products/?category=mobile&page=2
```

Here:
- `category` and `page` are **query parameters**
- They **refine the result**, not identify a single resource

### Key Characteristics

- **Optional**
- Used for filtering, searching, sorting, pagination
- Do **not** affect URL routing
- Easy to add or remove

### In Django

- Accessed using `request.GET`

### Example Use Cases

- Search  
- Pagination  
- Sorting  
- Filtering  

---

## 3️⃣ Core Difference (Interview Gold ⭐)

> **“Path parameters identify what resource you want, while query parameters control how you want it.”**

This sentence alone **scores points in interviews**.

---

## 4️⃣ Side-by-Side Comparison

| Feature | Path Parameters | Query Parameters |
|------|----------------|------------------|
| Location | URL path | After `?` in URL |
| Purpose | Identify resource | Modify / filter result |
| Mandatory | Yes | Usually optional |
| Routing | Affects routing | Does not affect routing |
| Example | `/users/10/` | `?page=2&sort=name` |

---

## 5️⃣ Django REST API Perspective

In **RESTful design**:

- **Path params** → nouns (resources)
- **Query params** → verbs or modifiers

### Good API Design

```http
GET /users/10/
GET /users/?is_active=true
```

### Bad API Design ❌

```http
GET /getUser?id=10
```

📌 Interviewers **love this REST clarity**.

---

## 6️⃣ Common Interview Trap (Say This!)

> **“Using query parameters to identify a resource instead of path parameters breaks REST conventions.”**

Example:

- ❌ `/users/?id=10`
- ✅ `/users/10/`

---

## 7️⃣ Real-World Analogy (Very Effective)

Think of a **library**:

- **Path parameter** → Book ID on the shelf  
- **Query parameter** → Filters like author, year, category  

You must identify the book first, then refine how you view results.

---

## 8️⃣ One-Line Interview Answer (Must Memorize)

> **“Path parameters identify a specific resource and are part of the URL path, while query parameters are optional and used for filtering, sorting, and pagination. Django handles path parameters in URL routing and query parameters via `request.GET`.”**

---

## 9️⃣ Final Wrap-Up (Strong Ending)

> **“In Django applications, path parameters define which resource is requested, while query parameters define how the response should be customized. Using them correctly leads to clean, RESTful APIs.”**