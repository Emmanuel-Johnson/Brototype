A **proxy** is a middleman between two parties.

Instead of talking directly, one side sends requests to the proxy, and the proxy passes them on and brings the response back.

👉 The main idea is: **“someone else is talking on your behalf.”**

---

## Forward Proxy

A **forward proxy** sits in front of **clients**.

### How it works:
```
Client → Forward Proxy → Internet Server
```

### Key points:
- Client sends the request to the proxy
- Proxy forwards it to the internet server
- The server does **not** know the real client
- The server only sees the proxy’s IP address

### Example:
In a college or office:
- Students access blocked websites using a proxy server
- Websites see only the **proxy IP**, not the student’s IP

---

## Reverse Proxy

A **reverse proxy** sits in front of **servers**.

### How it works:
```
Client → Reverse Proxy → Backend Server (Django)
```

### Key points:
- Client thinks it is talking to one server
- Reverse proxy forwards requests to backend servers
- Client does **not** know which backend server handled the request

### Example:
A Django app in production:
- All requests go to a reverse proxy
- Reverse proxy passes requests to Django
- Users only see the proxy, not the Django server

---

## One-Line Memory Trick 🧠

> **Forward proxy → hides the client**  
> **Reverse proxy → hides the server**

---

<br>

# Proxy (Why Use It?)

A **proxy** is a middleman between two parties.

Instead of talking directly, one side sends requests to the proxy, and the proxy passes them on and brings the response back.

👉 The main idea is: **“someone else is talking on your behalf.”**

---

## Why Use a Proxy?

- To hide identity (client or server)  
- To control access (block or allow traffic)  
- To improve security  
- To log, monitor, or filter requests  

---

## Forward Proxy

A **forward proxy** sits in front of **clients**.

### How it works:
```
Client → Forward Proxy → Internet Server
```

### Why Use a Forward Proxy?
- To hide the client’s IP address  
- To bypass restrictions (firewalls, geo-blocks)  
- To control what users can access  
- To cache responses and save bandwidth  

### Key Points:
- Client sends the request to the proxy  
- Proxy forwards it to the internet server  
- The server does **not** know the real client  
- The server only sees the proxy’s IP address  

### Example:
In a college or office:
- Students access blocked websites using a proxy server  
- Websites see only the **proxy IP**, not the student’s IP  

---

## Reverse Proxy

A **reverse proxy** sits in front of **servers**.

### How it works:
```
Client → Reverse Proxy → Backend Server (Django)
```

### Why Use a Reverse Proxy?
- To hide backend servers from the public  
- To add security (TLS, rate limiting, DDoS protection)  
- To distribute load across multiple servers  
- To improve performance (caching, compression)  

### Key Points:
- Client thinks it is talking to one server  
- Reverse proxy forwards requests to backend servers  
- Client does **not** know which backend server handled the request  

### Example:
A Django app in production:
- All requests go to a reverse proxy  
- Reverse proxy passes requests to Django  
- Users only see the proxy, not the Django server  

---

## One-Line Memory Trick 🧠

> **Forward proxy → hides the client (WHY: privacy & access control)**  
> **Reverse proxy → hides the server (WHY: security & scalability)**