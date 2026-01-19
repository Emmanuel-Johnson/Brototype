## 1. WHAT
`OneToOneField` is a Django model field used to create a **one-to-one relationship** between two models.  
It ensures that each record in one table is linked to **exactly one** record in another table.

---

## 2. WHY
It solves the problem of **splitting related data into separate tables** without duplication.  
Without it, you would need manual checks and joins to guarantee that only one related record exists.

---

## 3. WHERE
It belongs to the **model layer** in Django’s MVT architecture and is implemented at the database level as a **unique foreign key**.  
During request handling, the ORM uses it to fetch tightly coupled data efficiently.

---

## 4. HOW
1. Define a `OneToOneField` pointing to another model.  
2. Django enforces **uniqueness** at the database level.  
3. Access related data directly using simple attribute notation.

---

## 5. WHEN
Use it when two models have a **strict one-to-one relationship**, such as:
- User → Profile  

Do **not** use it when one record can be linked to multiple records; use `ForeignKey` instead.

---

## 6. EXAMPLE
In a user system, a `UserProfile` model can have a `OneToOneField` linked to Django’s `User` model to store additional user details.

---

## 7. PROS & CONS

### Pros
- Keeps models clean and well-structured  
- Enforces strong data integrity  
- Simplifies access to related data  

### Cons
- Adds an extra table join  
- Can be overkill if all data fits in a single model  

---

## 8. COMMON MISTAKES
- Using `OneToOneField` where a `ForeignKey` is required  
- Assuming the related object always exists without handling `DoesNotExist` errors  

<br>
<br>
<br>

## What is OneToOneField?

A **OneToOneField** creates a **one-to-one relationship** between two models.

👉 One object in Model A is linked to **exactly one** object in Model B  
👉 And Model B is linked to **exactly one** object in Model A  

---

## Real-life Examples

- **User ↔ Profile**
- **Person ↔ Passport**
- **Student ↔ ID Card**

Each side can have only **one matching record**.

---

## Basic Example  
### User Profile (Most Common Use Case)

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username
```

---

## What This Means

- Each **User** has only **one Profile**
- Each **Profile** belongs to only **one User**
- Django creates a **`user_id`** column in the `Profile` table

---

## Accessing Data

### From Profile → User

```python
profile = Profile.objects.get(id=1)
print(profile.user.username)
```

---

### From User → Profile (Reverse Relation)

```python
user = User.objects.get(id=1)
print(user.profile.phone)
```

⚠️ If the profile does **not exist**, Django raises  
`RelatedObjectDoesNotExist`

---

## Handling Missing OneToOne Object Safely

```python
profile = getattr(user, "profile", None)

if profile:
    print(profile.phone)
```

---

## `on_delete` Behavior

Same options as `ForeignKey`:

```python
models.CASCADE
models.PROTECT
models.SET_NULL    # requires null=True
models.SET_DEFAULT
models.DO_NOTHING
```

### Example

```python
user = models.OneToOneField(
    User,
    on_delete=models.CASCADE
)
```

---

## Custom Reverse Name (`related_name`)

```python
user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name="profile"
)
```

Then access using:

```python
user.profile
```

*(Without `related_name`, Django uses the model name by default)*

---

## OneToOneField vs ForeignKey

| Feature | OneToOneField | ForeignKey |
|------|--------------|-----------|
| Relation | One ↔ One | Many ↔ One |
| Unique | Yes | No |
| Example | User → Profile | Book → Publisher |

👉 **OneToOneField = ForeignKey + `unique=True`**

---

## Using `select_related()` with OneToOneField

Always use `select_related()` for performance:

```python
profiles = Profile.objects.select_related("user")

for profile in profiles:
    print(profile.user.username)
```

---

## When to Use OneToOneField

Use it when:

- You want to **extend an existing model**
- You don’t want to modify the original table
- You need a **strict one-to-one mapping**

### Examples

- Extending Django’s `User` model
- Splitting large models into smaller logical parts

---

## Database-Level View

- Django creates a **UNIQUE constraint** on the foreign key column
- Ensures the **one-to-one relationship** at the database level