> **“HTTP status codes are three-digit numbers returned by the server to indicate the result of an HTTP request.”**

They tell the client **what happened** — whether the request succeeded, failed, or needs action.

In Django, **every response includes a status code**, even if we don’t explicitly set it.

---

## 1️⃣ Why HTTP Status Codes Matter

Status codes are important because they:

- Standardize communication between client and server  
- Help frontend handle responses correctly  
- Improve debugging and API clarity  
- Are essential for RESTful design  

👉 A correct status code is just as important as the response data.

---

## 2️⃣ 200 — OK (Successful Request)

> **“200 OK means the request was successful.”**

### Used When

- Data is fetched successfully  
- Operation completes without errors  

### Examples

- Fetch user profile  
- List products  
- Successful GET request  

### In Django

- Default status for successful responses  
- Commonly used with **GET**

---

## 3️⃣ 201 — Created (Resource Created)

> **“201 Created means a new resource was successfully created.”**

### Used When

- POST request creates a new object  
- Server confirms creation  

### Examples

- User registration  
- Create order  
- Add new product  

### In Django

- Often returned after **POST**
- Usually includes the created resource or its location  

🎯 **Interview Tip:**  
POST → **201**, not 200

---

## 4️⃣ 400 — Bad Request (Client Error)

> **“400 Bad Request means the server cannot process the request due to invalid input.”**

### Used When

- Missing required fields  
- Invalid data format  
- Validation errors  

### Examples

- Invalid email format  
- Required field missing  

### In Django

- Form validation failures  
- Serializer validation errors  

📌 Important:  
👉 Request is syntactically correct, but **logically invalid**

---

## 5️⃣ 401 — Unauthorized (Not Authenticated)

> **“401 Unauthorized means authentication is required or has failed.”**

### Used When

- User is not logged in  
- Invalid or missing token  

### Examples

- Accessing protected API without login  
- Invalid JWT token  

### In Django

- Authentication failure  
- Login required  

⚠️ **Interview Trap:**  
401 = **not logged in**

---

## 6️⃣ 403 — Forbidden (Not Allowed)

> **“403 Forbidden means the user is authenticated but does not have permission.”**

### Used When

- User lacks required role  
- Permission denied  

### Examples

- Normal user accessing admin panel  
- Read-only user trying to delete data  

### In Django

- Permission checks  
- Authorization failures  

💡 **Interview Gold:**  
- 401 → *Who are you?*  
- 403 → *I know you, but you can’t do that*

---

## 7️⃣ 500 — Internal Server Error (Server Failure)

> **“500 Internal Server Error means something went wrong on the server.”**

### Used When

- Unhandled exceptions  
- Bugs in code  
- Database or server failure  

### Examples

- Null reference  
- Crashed service  

### In Django

- Usually indicates a backend bug  
- Should not expose internal details  

📌 Important:  
👉 **500 errors are never the client’s fault**

---

## 8️⃣ Quick Comparison Table (Interview Friendly ⭐)

| Code | Meaning | Responsibility |
|----|--------|---------------|
| 200 | OK | Server success |
| 201 | Created | Server success |
| 400 | Bad Request | Client mistake |
| 401 | Unauthorized | Authentication missing |
| 403 | Forbidden | Permission denied |
| 500 | Internal Error | Server bug |

---

## 9️⃣ One-Line Interview Answer (Must Memorize)

> **“HTTP status codes indicate the outcome of a request. In Django, 200 and 201 represent success, 400 indicates client-side validation errors, 401 and 403 handle authentication and authorization, and 500 indicates server-side failures.”**

---

## 🔟 Final Wrap-Up (Strong Ending)

> **“Using correct HTTP status codes in Django improves API clarity, error handling, and frontend–backend communication, making applications more reliable and REST-compliant.”**