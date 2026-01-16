## What is JWT?

**JWT (JSON Web Token)** is a compact, URL-safe token used to securely transmit user identity and claims between a client and a server.  
It is commonly used for **stateless authentication**, especially in APIs.

---

## Parts of a JWT

A JWT has **three parts**, separated by dots (`.`):

```
header.payload.signature
```

---

## 1. Header

Contains metadata about the token.

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- `alg` → signing algorithm  
- `typ` → token type  

---

## 2. Payload

Contains **claims** (user data and token info).

```json
{
  "user_id": 5,
  "username": "emmanuel",
  "exp": 1700000000
}
```

- Can contain public or private claims  
- **Not encrypted**, only Base64-encoded  
- Anyone can read the payload  

---

## 3. Signature

Used to ensure **integrity** and prevent tampering.

```text
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret_key
)
```

---

## JWT Signature – Purpose

The signature is created using:

- Header + payload  
- Secret key (or private key)  
- Hashing algorithm (HS256, RS256)  

### Why Signature Matters

- Detects token tampering  
- Confirms token was issued by a trusted server  
- If payload is changed, the signature becomes invalid  

---

## JWT Verification

JWT verification happens on **every request**.

### Verification Steps

1. Split token into header, payload, signature  
2. Recreate signature using secret key  
3. Compare recreated signature with received one  
4. Check token expiry (`exp`)  

If valid → user is authenticated.

### Example (Conceptual)

```python
jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
```

---

## How JWT is Sent

Tokens are usually sent in the HTTP header:

```
Authorization: Bearer <token>
```

---

## Key Interview Points

- JWT is **stateless**
- Payload is **readable but not modifiable**
- Signature ensures **integrity**, not secrecy
- No server-side session storage
- Common in **REST APIs**, not traditional server-rendered apps