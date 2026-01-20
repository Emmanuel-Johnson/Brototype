## What Are Signals?

**Signals** are a way for different parts of a Django application to **communicate automatically** when a specific event happens.

In simple terms:

> **“When X happens, do Y — without tightly coupling the code.”**

---

## Core Idea

- An **event occurs** → a signal is sent  
- A **receiver function listens** → runs automatically  

This enables **decoupled logic**.

---

## Real-Life Examples

- User is created → create profile  
- Order is placed → send confirmation email  
- Model is deleted → clean up related files  

You don’t put all this logic in one place.

---

## Basic Signal Structure

A signal has **three parts**:

1. **Signal** – the event (e.g. `post_save`)
2. **Sender** – who sends the signal (e.g. `User`)
3. **Receiver** – function that handles the event

---

## Simple Example

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        print("User created!")
```

---

## What Happens Here?

1. `User.save()` is called  
2. `post_save` signal fires  
3. `user_created()` runs automatically  

---

## Why Signals Exist

Signals help you:

- Keep code **loosely coupled**
- Avoid duplicating logic
- Add side effects without modifying core code

---

## Important Characteristics

- Signals are **synchronous** (blocking)
- They run in the **same process**
- Overuse can make code **hard to trace**

---

## One-Line Interview Answer

**Signals allow Django apps to react to events in a decoupled way when something happens.**

---

## When Signals Are Typically Used

- Notifications
- Audit logs
- Auto-creating related objects
- Cleanup tasks

---

## When NOT to Use Signals

- Core business logic
- Critical workflows
- When execution order matters

---

## Quick Summary

- Signals = event-driven hooks
- Promote loose coupling
- Powerful but easy to misuse
- Use sparingly and intentionally