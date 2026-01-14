**MVT** is the architectural pattern used by Django.  
It’s Django’s version of **MVC**, just with slightly different names.

👉 Think of it as: **Data → Logic → UI**

---

## 1️⃣ Model (Data Layer)

### What it is:
The **Model** defines your database structure and business rules.

### Responsibilities:
- Database tables  
- Fields & relationships  
- Data validation  
- Queries (ORM)  

### Example:
```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
```

🧠 **Model = “How data is stored & managed”**

---

## 2️⃣ View (Logic Layer)

### What it is:
The **View** handles the request and decides what data to send and which template to use.

### Responsibilities:
- Handle HTTP requests  
- Fetch data from models  
- Apply business logic  
- Return HTTP responses  

### Example:
```python
def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
```

🧠 **View = “Brain of the app”**

---

## 3️⃣ Template (Presentation Layer)

### What it is:
The **Template** defines how the data looks (HTML).

### Responsibilities:
- UI / layout  
- Display data  
- No business logic  

### Example:
```html
{% for product in products %}
  <p>{{ product.name }} - {{ product.price }}</p>
{% endfor %}
```

🧠 **Template = “Face of the app”**

---

## 🔁 How MVT Works (Request–Response Flow)

```
Browser → URL → View → Model → View → Template → Browser
```

### Step by step:
1. User sends request (URL)  
2. Django routes it to a **View**  
3. View talks to **Model**  
4. View sends data to **Template**  
5. Template returns HTML response  

---

## 🆚 MVT vs MVC (Quick Mapping)

| MVC | Django MVT |
|----|-----------|
| Model | Model |
| View | Template |
| Controller | View |

👉 Django’s **View** acts like the **Controller**.

---

## ✅ Why Django Uses MVT

- Clean separation of concerns  
- Secure by default  
- Faster development  
- Easy to scale  
- Beginner-friendly  

---

## 🎯 One-Line Interview Answer

> **“MVT is Django’s architecture where Model handles data, View handles logic, and Template handles presentation.”**