## 1. WHAT

A **CSRF Token** is a security token used to protect Django applications from **Cross-Site Request Forgery (CSRF)** attacks by verifying the authenticity of a request.

---

## 2. WHY

Without CSRF protection, attackers can trick authenticated users into performing unwanted actions.  
Manually securing every form would be repetitive and error-prone, so Django provides built-in CSRF protection.

---

## 3. WHERE

CSRF protection works at the **middleware** and **template** level in Django.  
The CSRF check happens during request processing **before the view logic executes**.

---

## 4. HOW

1. Django generates a unique CSRF token per user/session  
2. The token is sent to the client (usually via a cookie)  
3. The token is submitted with POST requests  
4. Django validates the token before processing the request  

---

## 5. WHEN

CSRF protection should be used for **state-changing requests** such as:

- POST  
- PUT  
- DELETE  

It is **not required** for safe GET requests or public read-only APIs.

---

## 6. EXAMPLE

```html
<form method="POST">
    {% csrf_token %}
    <input type="text" name="username">
    <input type="password" name="password">
    <button type="submit">Login</button>
</form>
```

Including `{% csrf_token %}` ensures that only valid form submissions are accepted.

---

## 7. PROS & CONS

### Pros
- Strong protection against CSRF attacks  
- Automatically managed by Django  
- Minimal developer effort  

### Cons
- Requires proper setup  
- Can block requests if misconfigured  

---

## 8. COMMON MISTAKES

- Forgetting to add `{% csrf_token %}` in POST forms  
- Disabling CSRF protection without understanding security risks  
- Using CSRF protection incorrectly for APIs