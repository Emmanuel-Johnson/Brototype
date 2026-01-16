# Browser Storage

Browser storage refers to mechanisms provided by the browser to store data on the **client side** so it can be reused across page loads or requests.

---

## 1. Cookies

Cookies are small **key–value pairs** stored in the browser and automatically sent to the server with every HTTP request.

### Key Points

- Stored in the browser  
- Sent with every request  
- Size limit ≈ **4KB**  
- Can have expiry and security flags  

### Example (Django Sets Cookie)

```python
response.set_cookie('theme', 'dark', max_age=3600)
```

### Use Cases

- Session ID  
- Authentication state  
- User preferences  

---

## 2. localStorage

`localStorage` stores data in the browser with **no expiry**.  
Data persists even after the browser is closed and reopened.

### Key Points

- Client-side only  
- Not sent to server automatically  
- Size ≈ **5–10MB**  
- Persists until manually cleared  

### Example (JavaScript)

```javascript
localStorage.setItem('theme', 'dark');
const theme = localStorage.getItem('theme');
```

### Use Cases

- Theme (dark/light)  
- User settings  
- Cached UI data  

---

## 3. sessionStorage

`sessionStorage` stores data for the **current browser tab/session only**.  
Data is cleared when the tab is closed.

### Key Points

- Client-side only  
- Tab-specific  
- Not shared across tabs  
- Cleared on tab close  

### Example (JavaScript)

```javascript
sessionStorage.setItem('step', '2');
const step = sessionStorage.getItem('step');
```

### Use Cases

- Multi-step forms  
- Temporary UI state  
- One-time flags  

---

## Quick Comparison (Interview Favorite)

| Feature | Cookies | localStorage | sessionStorage |
|-------|--------|--------------|----------------|
| Stored in | Browser | Browser | Browser |
| Sent to server | Yes | No | No |
| Expiry | Yes | No | On tab close |
| Storage size | ~4KB | ~5–10MB | ~5MB |
| Security | Medium | Low | Low |

---

## One-Line Takeaway

- **Cookies** → server communication  
- **localStorage** → persistent client data  
- **sessionStorage** → temporary tab-level data  