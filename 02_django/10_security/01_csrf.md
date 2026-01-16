# CSRF (Cross-Site Request Forgery)

## WHAT  
CSRF (Cross-Site Request Forgery) is a security mechanism used to protect Django applications from unauthorized actions performed on behalf of a logged-in user.

## WHY  
Without CSRF protection, attackers can trick users into submitting malicious requests unknowingly. Manually validating every request would be repetitive and error-prone.

## WHERE  
CSRF protection works at the middleware and template level in Django. It is checked during request processing before the view logic executes.

## HOW  
Django generates a unique CSRF token and sends it to the client. The token is included in unsafe requests like POST. Django validates the token before allowing the request.

## WHEN  
CSRF should be used for all state-changing requests made by authenticated users. It should not be enforced on trusted external APIs using token-based authentication.

## EXAMPLE  
A Django form includes `{% csrf_token %}` so only valid form submissions can create or update data.

## PROS & CONS  
CSRF protection is automatic, secure, and easy to use in Django. However, misconfiguration can block valid requests, especially in AJAX or API calls.

## COMMON MISTAKES  
Forgetting to include the CSRF token in forms or AJAX requests is common. Disabling CSRF globally instead of fixing configuration causes security risks.

<br>
<br>
<br>

# CSRF Attack – Simple Example

## What is a CSRF Attack?

A **CSRF (Cross-Site Request Forgery)** attack tricks an authenticated user into performing an unwanted action on a website where they are already logged in.

---

## Example Scenario

Imagine a user is logged into a **bank website** in one browser tab.  
The bank uses **cookies** to remember that the user is logged in.

Now, the same user opens a **malicious website** in another tab.  
That malicious site secretly sends a request like **“transfer money”** to the bank’s website.

Because the browser **automatically includes cookies**, the bank receives the request along with the user’s valid session cookie.

The bank believes the request came from the legitimate user and executes the transfer.

---

## Why This Attack Works

- The user never clicked **“transfer money”**
- The browser automatically sent the authenticated cookies
- Without CSRF protection, the server **cannot distinguish** between:
  - A real user-initiated request
  - A forged request from another site

---

## How Django Stops CSRF Attacks

Django protects against CSRF by using a **CSRF token**.

- Django generates a unique CSRF token for each session
- The token must be sent with every unsafe request (POST, PUT, DELETE)
- Only the real website can include this token
- A malicious site **cannot access or guess** the token

If the token is missing or invalid, Django **rejects the request**.