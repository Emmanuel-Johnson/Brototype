> **“HTTP methods define the type of action a client wants to perform on a resource.  
> They describe what to do, not how to do it.”**

In Django, HTTP methods are used to decide **how a request should be handled inside a view**.

---

## 1️⃣ Why HTTP Methods Exist

HTTP methods bring:

- **Clarity** → what action is intended  
- **RESTfulness** → clear API design  
- **Security** → safe vs unsafe operations  
- **Predictability** → same URL, different actions  

👉 Same URL + different method = **different behavior**

---

## 2️⃣ GET — Read Data

> **“GET is used to retrieve data from the server.”**

### Key Points

- Does **not** modify server data  
- Data sent via **query parameters**  
- Can be **cached**  
- Can be **bookmarked**  

### Example Use Cases

- Fetch user profile  
- List products  
- Load a webpage  

### In Django

- Access data using `request.GET`  
- GET requests should be **safe** and **idempotent**

---

## 3️⃣ POST — Create Data

> **“POST is used to send data to the server to create a new resource.”**

### Key Points

- **Modifies** server state  
- Data sent in **request body**  
- **Not cached**  
- Used for forms and API creation  

### Example Use Cases

- User registration  
- Login  
- Create a new order  

### In Django

- Access via `request.POST` or `request.body`  
- **CSRF protection applies** to POST requests  

---

## 4️⃣ PUT — Replace Data (Full Update)

> **“PUT is used to completely replace an existing resource.”**

### Key Points

- Client sends **full object**  
- Replaces entire resource  
- **Idempotent** (same request → same result)  

### Example

- Updating **all fields** of a user profile  

### In Django

- Commonly used in APIs  
- Usually handled via **Django REST Framework**

---

## 5️⃣ PATCH — Partial Update

> **“PATCH is used to update only specific fields of a resource.”**

### Key Points

- **Partial modification**  
- More efficient than PUT  
- Idempotent in practice  

### Example

- Updating only **email** or **phone number**  

### In Django

- Preferred for partial updates in REST APIs  
- Common in modern backend design  

---

## 6️⃣ DELETE — Remove Data

> **“DELETE is used to remove a resource from the server.”**

### Key Points

- Deletes server-side data  
- **Idempotent**  
- Usually no request body  

### Example

- Delete user account  
- Remove a product  

### In Django

- Often returns **204 No Content**

---

## 7️⃣ OPTIONS — Capability Discovery

> **“OPTIONS tells the client what methods are allowed on a resource.”**

### Key Points

- Does **not** modify data  
- Used heavily in **CORS**  
- Returns allowed HTTP methods  

### Example Use Cases

- Browser preflight request  
- API capability checking  

### In Django

- Often handled automatically  
- Important for frontend–backend communication  

---

## 8️⃣ HEAD — Headers Only

> **“HEAD is similar to GET, but it returns only headers, no response body.”**

### Key Points

- Used to check:
  - Resource existence  
  - Content size  
  - Cache validation  
- Very lightweight  

### Example

- Check if a file exists before downloading  

### In Django

- Often handled automatically  
- Useful for performance optimization  

---

## 9️⃣ Safe vs Unsafe Methods (Interview Favorite ⭐)

### Safe Methods (Do NOT change data)

- GET  
- HEAD  
- OPTIONS  

### Unsafe Methods (Change data)

- POST  
- PUT  
- PATCH  
- DELETE  

📌 This distinction matters for:

- Caching  
- Security  
- CSRF protection  

---

## 🔟 One-Line Interview Summary (Must Remember)

> **“HTTP methods define actions on resources. In Django, GET retrieves data, POST creates, PUT replaces, PATCH partially updates, DELETE removes, OPTIONS lists allowed methods, and HEAD returns headers only.”**

---

## 1️⃣1️⃣ Final Wrap-Up (Strong Ending)

> **“Django uses HTTP methods to separate concerns clearly and build RESTful, predictable applications. Choosing the correct method improves security, clarity, and API design.”**