## 1️⃣ Web & HTTP Fundamentals

### HTTP Basics
- What is HTTP & why it is stateless
- Structure of HTTP request & response
- HTTP headers (get/set)
- User-Agent
- HTTP methods  
  - GET, POST, PUT, PATCH, DELETE, OPTIONS
- PUT vs PATCH
- Query params vs Path params
- HTTP status codes  
  - 200, 201, 400, 401, 403, 500
- HTTP OPTIONS & Preflight request
- Content Negotiation

### Web Infrastructure
- Web server
- Webhook vs Webserver
- DNS
- HTTP vs HTTPS (ports)
- IPv4 vs IPv6
- Proxy vs Reverse Proxy
- Why HTTP is stateless

---

## 2️⃣ Django Fundamentals

- What is Django
- Advantages of Django
- Pros and Cons of Django
- Django vs other frameworks
- Project creation command
- App creation command
- Django project structure
- Django app file structure  
  - models.py  
  - views.py  
  - urls.py  
  - admin.py  
  - apps.py  

---

## 3️⃣ MVT Architecture

- MVT (Model–View–Template)
- Django View Engine
- Request–Response Cycle
- Role of Templates
- Context & context processors

---

## 4️⃣ Django Settings & Configuration

- settings.py overview
- SECRET_KEY  
  - Purpose  
  - Security implications
- INSTALLED_APPS
- Middleware settings
- Database configuration
- Static & Media settings

---

## 5️⃣ URL Routing

- URL routing concept
- URL patterns
- Path converters
- include()
- reverse() vs reverse_lazy()
- POST URL handling
- Reading query params & path params
- View function arguments

---

## 6️⃣ Django Views

### Types of Views
- Function-Based Views (FBV)
- Class-Based Views (CBV)
- Generic Views
- Mixins

### View Concepts
- Checking request method
- Returning HTTP status codes
- Changing response status code
- Redirects
- reverse() & reverse_lazy()
- HttpRequest object (contents)

---

## 7️⃣ Forms & Validation

- Forms vs ModelForms
- ModelForm
- Validators
- POST data validation
- CSRF Token (how it works)

---

## 8️⃣ Sessions, Cookies & Authentication

### Cookies & Sessions
- Session vs Cookies
- Cookie expiry
- Django session
- Django session management
- Session-based authentication

### Browser Storage
- Cookies
- localStorage
- sessionStorage

### Authentication & Authorization
- Authorization in Django
- JWT basics  
  - Parts of JWT  
  - JWT signature  
  - JWT verification
- CSRF Token vs CORS

---

## 9️⃣ Django Middleware

- What is middleware
- Request/Response middleware flow
- Default Django middleware
- Custom middleware
- Middleware vs signals

---

## 🔟 Django Security

- CSRF
- XSS
- CORS
- Rate limiting
- HTTPS importance

---

## 1️⃣1️⃣ Database & Migrations

- Database connection
- Models.py deep dive
- What are migrations
- Migration commands
- How migrations work
- Adding new column via migration
- Primary key vs Unique key
- Constraints
- unique_together

---

## 1️⃣2️⃣ Django ORM

### ORM Basics
- ORM concept
- ORM vs Raw SQL
- Advantages of ORM over SQL
- QuerySets
- Lazy evaluation
- Managers

### Retrieval Methods
- get()
- filter()
- exclude()
- values()
- values_list()
- contains / icontains

### Advanced ORM
- Q object
- F object
- Aggregation vs Annotation
- Aggregate functions
- annotate() vs aggregate()
- Raw queries vs cursor
- extra() (legacy)

### Date Lookups
- year
- month
- day
- weekday

---

## 1️⃣3️⃣ ORM Workouts (Practical)

Models: **Author, Book, Publisher**

- Find books of John or Sam
- Find total pages of Sam
- Find total number of books with author name
- Highest priced variant based on product
- Maximum workouts
- Join tables using FK & M2M

---

## 1️⃣4️⃣ ORM Optimization

- select_related
- prefetch_related
- Lazy loading
- When to use select_related vs prefetch_related

---

## 1️⃣5️⃣ Bulk Operations

- bulk_create
- bulk_update
- Bulk delete

---

## 1️⃣6️⃣ Model Relationships & Inheritance

- ForeignKey vs OneToOneField
- ManyToManyField
- related_name
- Model inheritance
  - Abstract base class
  - Multi-table inheritance
  - Proxy model (use cases)
- User model inheritance  
  - AbstractUser  
  - AbstractBaseUser

---

## 1️⃣7️⃣ Meta Options

- Meta class
- ordering
- verbose_name
- unique_together
- constraints

---

## 1️⃣8️⃣ Slug & SEO

- What is a slug
- SlugField use cases

---

## 1️⃣9️⃣ Static & Media Files

- Static files vs media files
- STATIC_ROOT vs MEDIA_ROOT
- How Django handles static files

---

## 2️⃣0️⃣ Signals

- What are signals
- Built-in signals
- Custom signals
- Signals sync vs async
- Signal examples
- When not to use signals

---

## 2️⃣1️⃣ WSGI & ASGI

- WSGI purpose
- ASGI purpose
- WSGI vs ASGI
- Django Channels
- Gunicorn

---

## 2️⃣2️⃣ Django REST Ecosystem

- Serializers
- Validators
- Generic API views
- Mixins
- Content negotiation
- Rate limiting

---

## 2️⃣3️⃣ Background Tasks & Realtime

- Celery
- Django Channels (WebSockets)

---

## 2️⃣4️⃣ Caching & Browser Behavior

- Browser cache
- Cache headers
- Django caching basics

---
