# ❌ When You Should NOT Use Django Signals

Django signals are powerful, but **misusing them leads to hidden bugs,
poor performance, and unreadable code**.

Below are clear cases where signals are the *wrong* tool.

------------------------------------------------------------------------

## 1️⃣ Core Business Logic

If the app **cannot work correctly without this logic**, don't hide it
in a signal.

### ❌ Bad

``` python
@receiver(post_save, sender=Order)
def charge_payment(sender, instance, **kwargs):
    charge_card(instance)
```

### Why this is bad

-   Hard to trace
-   Logic runs "magically"
-   Debugging becomes painful

### ✅ Better

``` python
def place_order(order):
    charge_card(order)
    order.save()
```

✔ Business flow is explicit and readable.

------------------------------------------------------------------------

## 2️⃣ Validation Rules

Signals are **not** for enforcing rules.

### ❌ Bad

``` python
@receiver(pre_save, sender=User)
def validate_age(sender, instance, **kwargs):
    if instance.age < 18:
        raise ValueError("Too young")
```

### Why this is bad

-   Unclear errors
-   Breaks admin, serializers, and forms
-   Validation happens in unexpected places

### ✅ Better

Use one of these instead: - `Model.clean()` - Form validation -
Serializer validation - Database constraints

------------------------------------------------------------------------

## 3️⃣ Performance-Critical Paths

Signals run **synchronously** and block requests.

### ❌ Bad

``` python
@receiver(post_save, sender=Order)
def generate_invoice(sender, instance, **kwargs):
    create_pdf(instance)  # slow
```

### Why this is bad

-   Slows every save
-   Causes unexpected latency

### ✅ Better

``` python
@receiver(post_save, sender=Order)
def trigger_task(sender, instance, **kwargs):
    generate_invoice.delay(instance.id)
```

✔ Signal triggers async work, not heavy logic.

------------------------------------------------------------------------

## 4️⃣ Code That Must Be Obvious & Traceable

If a new developer should **instantly understand what happens**, avoid
signals.

### ❌ Problem

``` python
order.save()
```

Hidden behavior happens somewhere else.

### ✅ Better

``` python
order.save()
send_email(order)
update_stock(order)
```

✔ Nothing is hidden.

------------------------------------------------------------------------

## 5️⃣ Tight Coupling Disguised as "Decoupling"

Using signals inside the **same app** for simple flows is
overengineering.

### ❌ Bad

``` python
order_created.send(sender=Order, order=order)
```

### When this is wrong

-   Only one receiver exists
-   Same app owns everything

### ✅ Better

Just call the function directly.

------------------------------------------------------------------------

## 6️⃣ Complex Transactional Logic

Signals don't respect business transaction boundaries well.

### ❌ Risk

-   Signal fires
-   Transaction rolls back
-   Side effects already happened (emails sent)

### ✅ Better

-   Use `transaction.on_commit()`
-   Or explicit service-layer functions

------------------------------------------------------------------------

## ✅ When Signals ARE a Good Fit

✔ Side effects\
✔ Cross-app notifications\
✔ Logging / analytics\
✔ Cache invalidation\
✔ Triggering background tasks

------------------------------------------------------------------------

## 🧠 Simple Rule to Remember

> **If the system breaks without it → don't use a signal.**\
> **If it's an optional reaction → signals are fine.**

------------------------------------------------------------------------

## 🎤 Interview-Ready Answer

> **"Signals should not be used for core business logic, validation, or
> performance-critical paths because they hide behavior and run
> synchronously. They're best for decoupled side effects."**