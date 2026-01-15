## WHAT

The `HttpRequest` object is a Django object that encapsulates **all data sent by the client** when making an HTTP request.

---

## WHY

Without `HttpRequest`, views would have no structured way to access:

- Form inputs  
- Query parameters  
- Headers  
- User authentication info  
- Uploaded files  

It is the **entry point** for all request data in Django.

---

## WHERE

`HttpRequest` is automatically created by Django and passed as the **first argument** to every view:

- Function-Based Views (FBV)  
- Class-Based Views (CBV)  
- Generic Views  

---

## Core Contents of HttpRequest (Must-Know)

### 1. `request.method`

```python
request.method   # 'GET', 'POST', etc.
```

- Tells what HTTP action the client is performing  

---

### 2. `request.GET`

```python
request.GET.get('page')
```

- Query parameters from the URL  
- Always a `QueryDict`  
- Used for filtering, pagination, searching  

---

### 3. `request.POST`

```python
request.POST.get('email')
```

- Form data sent via POST  
- Also a `QueryDict`  
- Only populated for POST requests  

---

### 4. `request.FILES`

```python
request.FILES['profile_pic']
```

- Uploaded files  
- Used with `enctype="multipart/form-data"`  

---

### 5. `request.user`

```python
request.user.is_authenticated
```

- Current logged-in user  
- `AnonymousUser` if not logged in  

---

### 6. `request.path`

```python
request.path   # '/contact/'
```

- Path portion of the URL  
- Useful for redirects and logging  

---

### 7. `request.headers`

```python
request.headers.get('User-Agent')
```

- All HTTP headers  
- Cleaner replacement for `request.META`  

---

### 8. `request.META`

```python
request.META['REMOTE_ADDR']
```

- Low-level server & HTTP details  
- Includes IP address, protocol, content type  

---

### 9. `request.COOKIES`

```python
request.COOKIES.get('sessionid')
```

- All cookies sent by the browser  

---

### 10. `request.session`

```python
request.session['cart_count'] = 3
```

- Per-user session storage  
- Backed by database or cache  

---

## Quick Mental Map (Interview Gold)

- **Request data** → `GET`, `POST`, `FILES`  
- **User info** → `user`, `session`, `cookies`  
- **Metadata** → `headers`, `META`, `path`, `method`