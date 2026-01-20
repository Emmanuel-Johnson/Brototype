# Django Signals -- Practical Use Cases & Patterns

This document shows **common Django signal patterns**, when to use them,
and when *not* to.

------------------------------------------------------------------------

## 1️⃣ `post_save` -- Create Related Object (Classic)

**Use case:** When a user is created → create a profile.

``` python
# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

### What's happening

-   **Signal:** `post_save`
-   **Sender:** `User`
-   Runs **only when a new user is created**

------------------------------------------------------------------------

## 2️⃣ `pre_save` -- Modify Data Before Saving

**Use case:** Auto-generate slug.

``` python
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Blog

@receiver(pre_save, sender=Blog)
def generate_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
```

✔ Runs **before** data hits the database.

------------------------------------------------------------------------

## 3️⃣ `post_delete` -- Cleanup Related Data / Files

**Use case:** Delete image file when object is deleted.

``` python
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Course

@receiver(post_delete, sender=Course)
def delete_course_image(sender, instance, **kwargs):
    if instance.thumbnail:
        instance.thumbnail.delete(save=False)
```

✔ Prevents orphaned files.

------------------------------------------------------------------------

## 4️⃣ Custom Signal -- Business Event (LMS Example)

### Define the signal

``` python
# courses/signals.py
from django.dispatch import Signal

course_completed = Signal()
```

### Send the signal

``` python
# courses/services.py
from .signals import course_completed

def complete_course(user, course):
    # business logic
    course_completed.send(
        sender=course.__class__,
        user=user,
        course=course
    )
```

### Receive the signal

``` python
# courses/receivers.py
from django.dispatch import receiver
from .signals import course_completed

@receiver(course_completed)
def award_certificate(sender, user, course, **kwargs):
    print("Certificate issued")
```

✔ Clean separation of business logic and side effects.

------------------------------------------------------------------------

## 5️⃣ Signal + Celery (Async Pattern)

**Use case:** Send email without blocking request.

``` python
@receiver(course_completed)
def send_completion_email(sender, user, course, **kwargs):
    send_course_email.delay(user.id, course.id)
```

-   Signal → **synchronous**
-   Celery task → **asynchronous**

------------------------------------------------------------------------

## 6️⃣ Many Receivers for One Signal

One signal → multiple actions.

``` python
@receiver(post_save, sender=Order)
def update_stock(sender, instance, **kwargs):
    ...

@receiver(post_save, sender=Order)
def send_order_email(sender, instance, **kwargs):
    ...
```

✔ Order saved → **both receivers run**

------------------------------------------------------------------------

## 7️⃣ Request Signal Example

``` python
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def log_request(sender, **kwargs):
    print("Request completed")
```

✔ Runs after **every HTTP request**.

------------------------------------------------------------------------

## 8️⃣ When NOT to Use Signals (Important)

❌ Validation logic\
❌ Core business rules\
❌ Performance-critical paths

### Use signals for

-   Side effects
-   Notifications
-   Cross-app communication

------------------------------------------------------------------------

## Interview One-Liner

> **"Django signals are best for decoupled side effects, not core
> logic."**