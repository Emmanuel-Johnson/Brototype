# unique_together

## What is unique_together?

`unique_together` is a Django model option used to enforce **uniqueness across multiple fields combined**.  
It ensures that the **same combination of values cannot be repeated** in the database.

**In simple terms:**  
One field can repeat, but the **combination cannot**.

---

## Why unique_together is Needed

### Example Problem

- A student can enroll in many courses  
- A course can have many students  
- But the **same student cannot enroll in the same course twice**

---

## Example Using unique_together

```python
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('student', 'course')
```

This prevents duplicate **(student, course)** entries in the database.

---

## How It Works Internally

- Django creates a **database-level unique constraint**
- Enforced by the **database**, not just Django
- A migration is automatically generated
- Duplicate combinations raise an error at insert/update time

---

## Interview-Friendly Points

- `unique_together` enforces **composite uniqueness**
- Works at the **database level**
- Prevents duplicate field combinations
- Implemented via **migrations**
- Common in **many-to-many / junction tables**

---

## Important Note (Modern Django)

`unique_together` is **deprecated** in favor of `UniqueConstraint`.

### Preferred Way

```python
from django.db.models import UniqueConstraint

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['student', 'course'],
                name='unique_student_course'
            )
        ]
```

---

## One-Line Interview Answer

`unique_together` ensures that a **combination of fields remains unique** in the database.