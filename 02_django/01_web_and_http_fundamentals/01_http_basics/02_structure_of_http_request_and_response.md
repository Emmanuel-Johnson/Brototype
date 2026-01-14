> **“HTTP communication is based on a request–response model.  
> Every interaction between a client and a Django server happens through an HTTP request and an HTTP response.”**

Let’s break down the structure of both, step by step.

---

## 1️⃣ Structure of an HTTP Request

An HTTP request is sent by the **client** (browser, mobile app, or frontend like React) to the **Django server**.

It has **four main parts**:

---

### 🔹 1. Request Line

This is the **first line** of the request.

It contains:

- **HTTP Method**
- **URL / Path**
- **HTTP Version**

#### Example

```http
GET /api/users/ HTTP/1.1
```

#### Meaning

- `GET` → fetch data  
- `/api/users/` → resource  
- `HTTP/1.1` → protocol version  

**In Django:**  
👉 This determines **which view function is called**

---

### 🔹 2. Headers

Headers are **key–value pairs** that send metadata about the request.

#### Common Headers

- Host
- User-Agent
- Content-Type
- Authorization
- Cookie

#### Example

```http
Content-Type: application/json
Authorization: Bearer <token>
```

**In Django:**

- Accessible via `request.headers`
- Authentication and content negotiation depend on headers

---

### 🔹 3. Request Body (Optional)

The body contains **actual data** sent to the server.

Used mainly with:

- POST
- PUT
- PATCH

#### Example JSON Body

```json
{
  "username": "john",
  "password": "secret"
}
```

**In Django:**

- `request.POST` → form data
- `request.body` → raw data
- `request.data` → Django REST Framework

---

### 🔹 4. Query Parameters (Optional)

Appended to the URL.

#### Example

```text
/products/?category=mobile&page=2
```

**In Django:**

- Accessed via `request.GET`

---

## 2️⃣ Structure of an HTTP Response

The response is sent back by the **Django server** to the **client**.

It has **three main parts**:

---

### 🔹 1. Status Line

The first line of the response.

Contains:

- HTTP version
- Status code
- Reason phrase

#### Example

```http
HTTP/1.1 200 OK
```

#### Common Status Codes

- 200 → Success
- 201 → Created
- 400 → Bad Request
- 401 → Unauthorized
- 404 → Not Found
- 500 → Server Error

**In Django:**

- Returned using `HttpResponse`, `JsonResponse`, or DRF `Response`

---

### 🔹 2. Response Headers

Headers provide metadata about the response.

#### Common Headers

- Content-Type
- Content-Length
- Set-Cookie
- Cache-Control

#### Example

```http
Content-Type: application/json
Set-Cookie: sessionid=abc123
```

**In Django:**

- Cookies and caching are handled here

---

### 🔹 3. Response Body

The **actual data** returned to the client.

Can be:

- HTML (traditional Django)
- JSON (APIs)
- Files (images, PDFs)

#### Example JSON

```json
{
  "message": "Login successful"
}
```

👉 This is what the **frontend consumes**.

---

## 3️⃣ Django Request–Response Flow (One-Liner)

> **“A Django server receives an HTTP request, processes it through middleware and views, and sends back an HTTP response containing a status code, headers, and body.”**

---

## 4️⃣ Real-World Analogy (Interview-Friendly)

Think of HTTP like **ordering food at a restaurant**:

- Request → Order details  
- Headers → Preferences (spicy, takeaway)  
- Body → What you ordered  
- Response → Prepared food  
- Status code → Order success or failure  

---

## 5️⃣ Final Interview Summary (Very Strong)

> **“An HTTP request consists of a request line, headers, optional body, and query parameters. An HTTP response consists of a status line, headers, and a response body. Django processes the request through views and middleware and returns a structured response to the client.”**