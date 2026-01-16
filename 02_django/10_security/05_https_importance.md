# HTTPS

## WHAT  
HTTPS is a secure communication protocol used to encrypt data between the client and a Django server. It protects data from being read or modified during transmission.

## WHY  
Without HTTPS, sensitive data like passwords and tokens can be intercepted. Manually securing each request is impractical and unsafe.

## WHERE  
HTTPS operates at the transport layer between the browser and the web server. Django runs behind it and relies on HTTPS for secure request handling.

## HOW  
The server presents an SSL/TLS certificate to the client. A secure encrypted connection is established. All HTTP data is then transmitted securely.

## WHEN  
HTTPS should be used for all production Django applications, especially those handling user data. It should not be skipped even for small or internal apps exposed to the internet.

## EXAMPLE  
A Django login form submits credentials over HTTPS so usernames and passwords are encrypted in transit.

## PROS & CONS  
HTTPS ensures confidentiality, integrity, and user trust. However, it requires certificate management and can add slight performance overhead.

## COMMON MISTAKES  
Serving login pages over HTTP is a major mistake. Not redirecting HTTP traffic to HTTPS can expose sensitive requests.

<br>
<br>
<br>

# HTTPS Importance

## What is HTTPS?

**HTTPS (HyperText Transfer Protocol Secure)** is the secure version of HTTP used to protect data exchanged between the browser and the server.  
It encrypts communication to prevent attackers from reading or modifying the data.

---

## Why HTTPS Is Important

### 1. Data Encryption

HTTPS encrypts data using **TLS**, so sensitive information such as passwords, tokens, and personal data cannot be read by attackers.

---

### 2. Data Integrity

HTTPS ensures that data is **not altered in transit**.  
Any tampering with the request or response is detected.

---

### 3. Authentication

HTTPS verifies that the client is communicating with the **correct server**, not a fake or malicious one.

---

### 4. Prevents Common Attacks

- Man-in-the-middle (MITM) attacks  
- Session hijacking  
- Cookie theft  

---

## HTTPS and Cookies (Very Important)

### Without HTTPS
- Cookies can be intercepted and stolen over the network  

### With HTTPS
- Cookies can be marked as **Secure**
- Session cookies are protected

```python
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## HTTPS in Django

Django provides security settings that work best with HTTPS:

```python
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
```

- Redirects all HTTP traffic to HTTPS  
- Enforces HTTPS using HSTS  

---

## SEO and Browser Trust

- Browsers mark HTTP sites as **Not Secure**
- HTTPS improves **SEO ranking**
- Required for modern browser features (payments, geolocation)

---

## Key Interview Points

- HTTPS encrypts data using **TLS**
- Prevents **MITM attacks**
- Mandatory for authentication systems
- Protects cookies and JWTs
- Required for **production applications**