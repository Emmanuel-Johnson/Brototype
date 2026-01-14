# HTTP Headers (Django Perspective)

> **“HTTP headers are key–value pairs that carry metadata between a client and a server during an HTTP request and response.”**

They don’t contain the actual data itself, but they describe **how the data should be handled**.

---

## 1️⃣ What Are HTTP Headers?

HTTP headers are sent:

- **From client to server** → Request headers  
- **From server to client** → Response headers  

### What Headers Tell Us

- Data format (`Content-Type`)
- Authentication info (`Authorization`)
- Caching rules (`Cache-Control`)
- Cookies (`Cookie`, `Set-Cookie`)

👉 Headers are part of **every HTTP request and response**.

---

## 2️⃣ Request Headers (Getting Headers in Django)

Request headers are sent by the **client**.

### Common Request Headers

- Host  
- User-Agent  
- Accept  
- Content-Type  
- Authorization  
- Cookie  

### 📌 How Django Gets Request Headers

In Django, headers are accessed using the **request object**.

You can get headers using:

- `request.headers` → **recommended**
- `request.META` → low-level (WSGI)

### Conceptual Flow

- Django reads headers sent by the browser  
- Headers are available inside the view  
- Used for authentication, content negotiation, etc.

### Examples

- `Authorization` header → used for JWT or token authentication  
- `Content-Type` → tells Django how to parse the request body  

---

## 3️⃣ Response Headers (Setting Headers in Django)

Response headers are sent by the **server** back to the **client**.

### Common Response Headers

- Content-Type  
- Set-Cookie  
- Cache-Control  
- Content-Length  
- Location  

### 📌 How Django Sets Response Headers

Conceptually:

- View creates a response  
- Headers are attached to the response object  
- Django sends them to the client  

### Examples of What Django Sets

- `Content-Type` → JSON or HTML  
- `Set-Cookie` → session management  
- `Cache-Control` → caching rules  

---

## 4️⃣ Cookies Are Header-Based (Important Point)

Cookies work **entirely using headers**:

- Client → sends cookies using the `Cookie` header  
- Server → sets cookies using the `Set-Cookie` header  

### In Django

- Sessions rely on cookies  
- Authentication depends on cookies or authorization headers  

👉 Cookies are **not magic** — they are just HTTP headers.

---

## 5️⃣ Headers in Django REST APIs

In REST APIs:

- Headers carry authentication tokens  
- Headers specify request and response formats  

### Examples

```http
Authorization: Bearer <token>
Accept: application/json
```

### Django REST Framework Uses Headers For

- Authentication  
- Throttling  
- Versioning  
- Content negotiation  

---

## 6️⃣ Why Headers Matter in Interviews

Headers are critical because they:

- Support stateless HTTP  
- Enable security  
- Allow API communication  
- Control caching and performance  

Without headers:

- ❌ No authentication  
- ❌ No sessions  
- ❌ No REST APIs  

---

## 7️⃣ One-Line Interview Answer (Must Remember)

> **“HTTP headers are metadata sent with requests and responses. In Django, request headers are accessed using the request object, and response headers are set on the response object to control authentication, content type, cookies, and caching.”**

---

## 8️⃣ Ultra-Short Django-Specific Summary (Bonus)

> **“In Django, request headers are accessed using `request.headers` to read metadata like authorization, content type, and cookies. Response headers are set on the response object to control content type, caching, cookies, and authentication. Cookies and sessions work entirely through HTTP headers.”**

---

## 9️⃣ Real-World Analogy (Optional)

Think of headers like **instructions written on a courier package**:

- Sender details  
- Handling instructions  
- Destination rules  

The package (body) is handled based on those instructions.

---

## 🔚 Final Wrap-Up

> **“In Django, HTTP headers play a key role in handling authentication, sessions, content negotiation, and caching. They allow the server and client to exchange control information while keeping HTTP stateless.”**

---
<br>
<br>


# HTTP Headers in Django REST Framework (DRF)

<br>

## 1️⃣ Reading Request Headers in DRF

### Example: Read `Authorization` and `Content-Type`

```python
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response

class HeaderReadAPIView(APIView):
    def post(self, request):
        auth_header = request.headers.get('Authorization')
        content_type = request.headers.get('Content-Type')

        return Response({
            "authorization": auth_header,
            "content_type": content_type
        })
```

### Client Sends Request

```http
POST /api/headers/
Authorization: Bearer abc123
Content-Type: application/json
```

### Response

```json
{
  "authorization": "Bearer abc123",
  "content_type": "application/json"
}
```

### 📌 Key Points

- `request.headers` is a **clean, case-insensitive dictionary**
- DRF automatically parses headers for you
- ✅ Prefer `request.headers` over `request.META`

---

## 2️⃣ Accessing Custom Headers

### Client Sends

```http
X-Client-Version: 1.2.0
```

### DRF Code

```python
client_version = request.headers.get('X-Client-Version')
```

✅ Works directly — **no `HTTP_` prefix needed** in DRF

---

## 3️⃣ Setting Response Headers in DRF

### Example: Set Content-Type, Custom Header, Caching

```python
from rest_framework.views import APIView
from rest_framework.response import Response

class HeaderSetAPIView(APIView):
    def get(self, request):
        response = Response(
            {"message": "Headers set successfully"}
        )

        response['Content-Type'] = 'application/json'
        response['X-App-Name'] = 'MyDRFApp'
        response['Cache-Control'] = 'no-cache'

        return response
```

### Response Headers

```http
Content-Type: application/json
X-App-Name: MyDRFApp
Cache-Control: no-cache
```

---

## 4️⃣ Setting Cookies Using Response Headers

```python
class CookieAPIView(APIView):
    def get(self, request):
        response = Response({"message": "Cookie set"})
        response.set_cookie(
            key='session_id',
            value='abc123',
            httponly=True,
            secure=True
        )
        return response
```

📌 Cookies are headers under the hood (`Set-Cookie`)

---

## 5️⃣ Authentication Header Example (JWT Style)

### Reading Token

```python
token = request.headers.get('Authorization')
```

### Client Sends

```http
Authorization: Bearer eyJhbGciOiJIUzI1...
```

📌 DRF authentication classes (JWT, TokenAuthentication) automatically read this header.

---

## 6️⃣ 🎯 Interview-Ready Summary

> **“HTTP headers carry metadata.  
> In DRF, request headers are accessed via `request.headers`, and response headers are set directly on the `Response` object.  
> Headers are commonly used for authentication (`Authorization`), content negotiation (`Content-Type`), cookies (`Set-Cookie`), and caching (`Cache-Control`).”**