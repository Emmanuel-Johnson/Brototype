# Django Signals: Synchronous vs "Asynchronous"

In Django, **signals are synchronous by default**.\
There is **no true async signal system** built into Django.

The confusion usually comes from **how the receiver behaves**, not the
signal itself.

Let's break it down cleanly.

------------------------------------------------------------------------

## 1️⃣ Synchronous Signals (Default Behavior)

When you send a signal, **all receivers run immediately**, one after
another, **in the same thread**.

``` python
post_save.send(sender=User, instance=user)
```

### What actually happens

1.  Signal is sent\
2.  Receiver A runs\
3.  Receiver B runs\
4.  Control returns to the original code

### Example

``` python
@receiver(post_save, sender=User)
def create_profile(sender, instance, **kwargs):
    Profile.objects.create(user=instance)
```

If this receiver takes **2 seconds**, your request waits **2 seconds**.

### Key points

-   Blocking
-   Predictable
-   Easy to debug
-   Slows requests if heavy work is inside receivers

------------------------------------------------------------------------

## 2️⃣ "Asynchronous" Signals (Not Real Async)

Django signals **cannot be async**.

What people usually mean by *async signals* is:

> "The signal is sent synchronously, but the work is done
> asynchronously."

### How is this achieved?

By delegating work to:

-   Celery
-   Django-Q
-   RQ
-   Threads (not recommended much)

------------------------------------------------------------------------

## 3️⃣ Signal + Background Task (Real-World Async Pattern)

``` python
@receiver(order_paid)
def handle_order_paid(sender, order, **kwargs):
    send_invoice_email.delay(order.id)  # Celery task
```

### Flow

1.  Signal is sent (sync)\
2.  Receiver is called (sync)\
3.  Task is queued (fast)\
4.  Actual work runs in the background

✔ The signal is still synchronous\
✔ The **effect** is asynchronous

------------------------------------------------------------------------

## 4️⃣ Async Views & Signals (Important Gotcha)

Even in **async Django views**, signals are still synchronous.

``` python
async def my_view(request):
    user.save()  # post_save signal runs synchronously
```

This can:

-   Block the event loop
-   Reduce async performance benefits

------------------------------------------------------------------------

## 5️⃣ What NOT to Do

❌ Heavy work inside signal receivers: - Sending emails - PDF
generation - External API calls

❌ Treating signals like task queues

------------------------------------------------------------------------

## 6️⃣ When to Use What

  Scenario                  Best Approach
  ------------------------- ----------------------
  Simple DB side-effects    Sync signal
  Email / notifications     Signal → Celery
  Critical business logic   Direct function call
  High-performance paths    Avoid signals

------------------------------------------------------------------------

## One-Line Summary

**Signals are always synchronous.**\
**"Async signals" means using signals to trigger async work.**