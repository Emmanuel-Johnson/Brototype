# XSS (Cross-Site Scripting)

## WHAT  
XSS (Cross-Site Scripting) is a security protection used to prevent malicious scripts from being executed in users’ browsers. It protects users from injected client-side code.

## WHY  
Without XSS protection, attackers can steal session data, cookies, or perform actions as the user. Manually sanitizing every output would be repetitive and unreliable.

## WHERE  
XSS protection works mainly at the template rendering layer in Django. It affects how user input is displayed in HTML responses sent to the browser.

## HOW  
Django automatically escapes unsafe characters when rendering templates. User input is treated as plain text by default. Only explicitly marked safe content is rendered as HTML.

## WHEN  
XSS protection should always be enabled when rendering user-generated content. It should not be bypassed unless the data source is fully trusted and sanitized.

## EXAMPLE  
A comment posted by a user is displayed safely on a page without executing embedded JavaScript because Django auto-escapes the content.

## PROS & CONS  
Django’s XSS protection is automatic, effective, and easy to use. However, marking content as safe incorrectly can reintroduce vulnerabilities.

## COMMON MISTAKES  
Using the `|safe` filter on untrusted data is a common mistake. Trusting raw user input without validation can lead to XSS attacks.

<br>
<br>
<br>

# XSS (Cross-Site Scripting) – Simple Example

## What is XSS?

**XSS (Cross-Site Scripting)** is an attack where an attacker injects malicious JavaScript into a trusted website, causing the script to run in other users’ browsers.

---

## Simple Example Scenario

Imagine a **comment box** on a website that does not validate or escape user input.

An attacker posts a comment containing malicious JavaScript code.

When another user opens the page, the injected script **runs automatically in their browser**.

---

## What the Attacker Gains

Because the script runs inside a trusted website, the browser allows it to:

- Steal cookies or session data  
- Read or modify page content  
- Perform actions as the logged-in user  

---

## Key Difference from CSRF

- **CSRF** → tricks the browser into sending a **fake request**  
- **XSS** → injects **malicious JavaScript** that runs in the browser  

---

## How Django Prevents XSS

Django protects against XSS mainly through **automatic template escaping**.

- Template variables are auto-escaped by default  
- Injected scripts are displayed as **plain text**, not executed  
- XSS usually occurs only when developers disable escaping (e.g., using `|safe` incorrectly)