# Built-in Signals in Django

Django provides **predefined signals** that fire automatically when common events happen in the framework.

---

## 1️⃣ Model Signals (Most Used)

These signals are triggered during **model lifecycle events**.

---

### `pre_save`

- Fired **before** `model.save()`
- Used for validation or modification

```python
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Book)
def before_save(sender, instance, **kwargs):
    instance.title = instance.title.strip()
```

---

### `post_save`

- Fired **after** `model.save()`
- Commonly used for side effects

```python
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def after_user_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

---

### `pre_delete`

- Fired **before** `model.delete()`

```python
from django.db.models.signals import pre_delete

@receiver(pre_delete, sender=Product)
def before_delete(sender, instance, **kwargs):
    print("About to delete product")
```

---

### `post_delete`

- Fired **after** `model.delete()`

```python
from django.db.models.signals import post_delete

@receiver(post_delete, sender=Product)
def after_delete(sender, instance, **kwargs):
    instance.image.delete(save=False)
```

---

### `m2m_changed`

- Fired when a **ManyToManyField** changes

```python
from django.db.models.signals import m2m_changed

@receiver(m2m_changed, sender=Book.authors.through)
def authors_changed(sender, instance, action, **kwargs):
    if action == "post_add":
        print("Author added")
```

---

## 2️⃣ Request / Response Signals

Triggered during the **HTTP request lifecycle**.

| Signal | When it fires |
|------|---------------|
| `request_started` | Request begins |
| `request_finished` | Request ends |
| `got_request_exception` | Exception raised |

---

### Example

```python
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def request_done(sender, **kwargs):
    print("Request completed")
```

---

## 3️⃣ Authentication Signals

Triggered during **authentication events**.

- `user_logged_in`
- `user_logged_out`
- `user_login_failed`

```python
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def on_login(sender, user, request, **kwargs):
    print("User logged in:", user.username)
```

---

## 4️⃣ Migration Signals (Less Common)

| Signal | Purpose |
|------|--------|
| `pre_migrate` | Before migrations |
| `post_migrate` | After migrations |

```python
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_data(sender, **kwargs):
    print("Migrations finished")
```

---

## 5️⃣ Important Things to Remember

- Built-in signals are **synchronous**
- They run inside the **same transaction**
- Exceptions can **break the request**
- Signals can fire **multiple times**

---

## Common Mistakes

❌ Putting heavy logic in signals  
❌ Assuming async behavior  
❌ Forgetting to register signals  
❌ Using signals for core business logic  

---

## Interview One-Liners

- `post_save` → after model saved  
- `pre_delete` → before deletion  
- `m2m_changed` → many-to-many updates  
- Signals are synchronous  

---

## Quick Summary

- Django provides many built-in signals
- Model signals are the most commonly used
- Signals react automatically to events
- Powerful but must be used carefully