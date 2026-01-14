In Django, **Templates are responsible for presentation** —  
👉 how data is displayed to the user, **not** how it’s processed.

Think of templates as the **UI layer** in Django’s **MVT architecture**.

---

## What Is a Template?

A **Template** is usually an HTML file with special Django template syntax that:

- Displays data sent from Views  
- Controls layout and structure  
- Keeps UI separate from business logic  

📄 Example: `home.html`

---

## Core Role of Templates

### 1️⃣ Presentation (UI)

Templates define:

- HTML structure  
- CSS & JS integration  
- Page layout  

```html
<h1>Welcome</h1>
```

🧠 **Templates decide how things look.**

---

### 2️⃣ Display Dynamic Data

Templates receive context data from Views and render it.

```html
<p>Hello {{ user.username }}</p>
```

🧠 Templates **show data**, they don’t fetch it.

---

### 3️⃣ Separation of Concerns

Templates must **not** contain:

❌ Database queries  
❌ Business logic  
❌ Complex calculations  

This keeps responsibilities clear:

- **Views** → logic  
- **Models** → data  
- **Templates** → display  

---

### 4️⃣ Reusability with Template Inheritance

Templates allow reuse using:

- `base.html`  
- `{% extends %}`  
- `{% block %}`  

```html
{% extends "base.html" %}
{% block content %}
  <h2>Products</h2>
{% endblock %}
```

🧠 **Write once, reuse everywhere.**

---

### 5️⃣ Control Flow (Limited Logic)

Templates support **safe, simple logic only**:

- Loops  
- Conditions  

```html
{% if products %}
  {% for product in products %}
    {{ product.name }}
  {% endfor %}
{% endif %}
```

🚫 Heavy logic stays in **Views**, not Templates.

---

### 6️⃣ Security Benefits

Templates automatically protect against:

- XSS (Cross-Site Scripting)  
- Unsafe HTML rendering  

```html
{{ user_input }}
```

🛡 Escaped by default.

---

## Template’s Place in Request–Response Cycle

```
Request
   ↓
View (logic)
   ↓
Template (render UI)
   ↓
Response (HTML)
```

---

## Template vs View (Quick Comparison)

| View | Template |
|----|---------|
| Handles logic | Handles display |
| Talks to Models | Receives data only |
| Python code | HTML + template syntax |

---

## Real-World Example

**E-commerce site:**

- **View** → gets product list  
- **Template** → shows product cards  
- **Model** → stores product data  

---

## 🎯 One-Line Interview Answer

> **“Templates in Django handle the presentation layer by rendering dynamic data into HTML while keeping UI separate from business logic.”**