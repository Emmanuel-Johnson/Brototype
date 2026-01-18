## 1. WHAT
Lazy loading is a Django ORM behavior used to delay database queries until the data is actually needed.

## 2. WHY
It avoids unnecessary database hits when data may not be used. Without lazy loading, Django would fetch data eagerly, causing wasted queries and slower response times.

## 3. WHERE
It exists at the ORM and QuerySet level and is triggered during view execution, template rendering, or serialization when the data is accessed in the request–response flow.

## 4. HOW
Django first builds a QuerySet without hitting the database. The query executes only when the QuerySet is evaluated. Accessing fields or iterating triggers the actual database call.

## 5. WHEN
Use it when working with QuerySets where data might not always be required. Do not rely on it inside loops where repeated access can cause N+1 query problems.

## 6. EXAMPLE
In a user list view,  
`users = User.objects.filter(is_active=True)`  
hits the database only when the users are iterated over in the template.

## 7. PROS & CONS
It improves performance by avoiding unnecessary queries and enables flexible query composition while keeping code clean. However, it can hide database hits and cause unexpected performance issues.

## 8. COMMON MISTAKES
Assuming a QuerySet has already hit the database is a common mistake. Another is accessing related objects repeatedly without using `select_related` or `prefetch_related`.
