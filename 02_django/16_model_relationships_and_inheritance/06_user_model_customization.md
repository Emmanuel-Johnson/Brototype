# User Model Customization in Django

Django provides **two official ways** to customize the User model:

1. **AbstractUser** (easy & recommended)  
2. **AbstractBaseUser** (advanced & full control)

---

## 1️⃣ AbstractUser

### What is AbstractUser?

`AbstractUser` is Django’s **default User model**, but extensible.

It already includes:

- `username`
- `email`
- `password`
- `is_staff`, `is_active`, `is_superuser`
- `groups` & `permissions`

You only **add extra fields**.

---

### Example

```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
```

### settings.py

```python
AUTH_USER_MODEL = "accounts.User"
```

⚠️ Must be set **before the first migration**.

---

### Usage

```python
user = User.objects.create_user(
    username="emmanuel",
    password="test123"
)

user.phone = "9876543210"
user.save()
```

---

### When to Use AbstractUser

✅ 90% of projects  
✅ When you need **extra fields only**  
✅ Minimal complexity  
✅ Django admin & auth work out of the box  

---

## 2️⃣ AbstractBaseUser

### What is AbstractBaseUser?

`AbstractBaseUser` is the **bare minimum** user model.

It only provides:

- Password hashing
- `last_login`

You must define:

- Username / Email field
- Authentication logic
- Permissions
- Admin configuration

👉 **Full control, more responsibility**

---

### Example (Email as Login)

```python
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
```

---

### Custom User Manager (Required)

```python
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user
```

Attach it:

```python
objects = UserManager()
```

---

### settings.py

```python
AUTH_USER_MODEL = "accounts.User"
```

---

### When to Use AbstractBaseUser

✅ Need **email instead of username**  
✅ Completely custom authentication logic  
✅ No username field  
✅ Enterprise / large systems  

---

## AbstractUser vs AbstractBaseUser

| Feature | AbstractUser | AbstractBaseUser |
|------|--------------|------------------|
| Ease of use | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| Built-in fields | Yes | No |
| Admin ready | Yes | No (manual) |
| Custom login field | Limited | Full control |
| Recommended | Yes (most cases) | Only if needed |

---

## Strong Recommendation

👉 **Use AbstractUser unless you have a very strong reason not to.**

Even Django’s official documentation recommends this.

---

## Common Mistakes

❌ Switching user model after migrations  
❌ Using AbstractBaseUser for simple projects  
❌ Forgetting custom user manager  
❌ Breaking Django admin  

---

## Interview One-Liners

- **AbstractUser** → “Extend Django’s default user safely”  
- **AbstractBaseUser** → “Build a user model from scratch”