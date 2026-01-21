# Django Channels (WebSockets)

## 1. WHAT
Django Channels is an extension to Django used to handle real-time communication using WebSockets and other async protocols.  
It allows Django to go beyond HTTP and support bidirectional, long-lived connections.

## 2. WHY
Traditional Django with HTTP is request–response based and cannot push data to clients in real time.  
Without Channels, building chat, live notifications, or real-time updates becomes complex and inefficient.

## 3. WHERE
Django Channels sits alongside Django views and runs on an ASGI server.  
Flow is typically: Client → ASGI server → Channels consumer → channel layer → other consumers or clients.

## 4. HOW
The client opens a WebSocket connection to Django.  
Channels routes the connection to a consumer, which listens for and sends messages asynchronously.

## 5. WHEN
Use Django Channels for real-time features like chat, live dashboards, or notifications.  
Do not use it for normal CRUD APIs where standard HTTP requests are sufficient.

## 6. EXAMPLE
In a chat application, users send messages through WebSockets.  
Django Channels broadcasts the message instantly to all connected users in the room.

## 7. PROS & CONS
It enables real-time communication while staying within the Django ecosystem.  
However, it increases system complexity and requires ASGI servers and a channel layer like Redis.

## 8. COMMON MISTAKES
Using Channels when periodic polling or HTTP is enough.  
Blocking async consumers with long synchronous or database-heavy operations.