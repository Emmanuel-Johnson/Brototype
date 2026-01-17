## WHAT

A Manager is an interface through which Django models interact with the database. It provides methods to retrieve QuerySets.

## WHY

Managers centralize database query logic and make data access reusable, clean, and consistent across the application.

## WHERE

Managers are defined on Django models and accessed using the model class (for example, `Model.objects`).

## HOW

Django provides a default manager called `objects`. You can also create custom managers to add reusable query methods.

## Default Manager Example

```python
User.objects.all()
User.objects.filter(is_active=True)
```

## Custom Manager Example

```python
class ActiveUserManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

class User(models.Model):
    is_active = models.BooleanField(default=True)
    objects = models.Manager()
    active_users = ActiveUserManager()

User.active_users.active()
```

## Important Interview Points

* Every model has at least one manager
* Managers return QuerySets
* Managers work at the model level, not the instance level
* Custom managers help avoid repeating query logic

---

## Interview One-Liner

> "A Django manager is the entry point for database queries and returns QuerySets for a model."
