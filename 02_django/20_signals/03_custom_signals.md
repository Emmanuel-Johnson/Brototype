# Django Custom Signals

In Django, **custom signals** are signals you define yourself when
Django's built-in signals (like `post_save`, `request_started`, etc.)
aren't enough.

They're used to notify other parts of your app that **"something
happened"** without tightly coupling code.

------------------------------------------------------------------------

## Why Custom Signals?

To keep code **decoupled**.

### Example situations

-   User completed a course\
-   Order was paid successfully\
-   Profile verification finished

Instead of calling functions directly, you emit a signal and let any
listener react.

------------------------------------------------------------------------

## 1️⃣ Define a Custom Signal

Create a `signals.py` file.

``` python
# app/signals.py
from django.dispatch import Signal

course_completed = Signal()
```

With arguments (recommended):

``` python
course_completed = Signal()
```

> Modern Django ignores `providing_args` (it's deprecated).

------------------------------------------------------------------------

## 2️⃣ Send the Signal

You send (emit) the signal when the event happens.

``` python
from .signals import course_completed

course_completed.send(
    sender=Course,
    user=user,
    course=course
)
```

### Key points

-   **sender** → who is sending the signal (class or object)
-   **Extra keyword args** → data passed to receivers
-   **Sender does NOT have to be a model**, but usually is

------------------------------------------------------------------------

## 3️⃣ Receive the Signal

Create a receiver function.

``` python
from django.dispatch import receiver
from .signals import course_completed

@receiver(course_completed)
def award_certificate(sender, user, course, **kwargs):
    print(f"{user} completed {course}")
```

------------------------------------------------------------------------

## 4️⃣ Register Signals (IMPORTANT)

Django won't load signals automatically.

In `apps.py`:

``` python
# app/apps.py
from django.apps import AppConfig

class AppConfig(AppConfig):
    name = "app"

    def ready(self):
        import app.signals
```

And in `__init__.py`:

``` python
default_app_config = "app.apps.AppConfig"
```

------------------------------------------------------------------------

## Custom Signals vs Model Signals

  Feature        Model Signals           Custom Signals
  -------------- ----------------------- ------------------------------
  Triggered by   Django ORM              Your own logic
  Examples       post_save, pre_delete   order_paid, course_completed
  Sender         Model class             Anything
  Use case       DB lifecycle            Business logic events

------------------------------------------------------------------------

## Best Practices

-   Use custom signals for **business events**, not simple logic
-   Keep receivers **lightweight**
-   Don't hide critical logic inside signals (debugging becomes hard)
-   Avoid signals for simple function calls

------------------------------------------------------------------------

## Mental Model

**Signal = announcement**

> "Hey, this event just happened. Anyone interested can react."