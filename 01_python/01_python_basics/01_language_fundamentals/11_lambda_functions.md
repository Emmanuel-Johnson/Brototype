In Python, a lambda function is simply a small, anonymous function—meaning it doesn’t require a name. Instead of using the def keyword to define a regular function, lambdas allow us to write short one-line functions, mainly used when the logic is simple and only needed temporarily.

A lambda function follows a fixed structure:

lambda arguments: expression

It can take multiple arguments, but it must contain only one expression, which is automatically returned. For example, lambda x: x * 2 returns a function that doubles its input. If I want to use it, I can say (lambda x: x * 2)(5) and get 10.

Lambdas are often used with Python’s functional programming tools like map, filter, and sorted. For example, if I want to square all numbers in a list using map, I can write:

map(lambda n: n*n, [1, 2, 3]).

Similarly, to filter even numbers, I can use:

filter(lambda n: n % 2 == 0, [1, 2, 3, 4]).

Another common use case is sorting. If I have a list of tuples like student records and I want to sort by marks, I can write:

sorted(students, key=lambda s: s[1]).

The lambda quickly tells Python which part of the data should be used as the sorting key.

In real-world development, lambdas make code shorter and more readable when used properly, especially for quick inline logic. But Python developers avoid making large complex logic inside lambdas because readability suffers. So, lambdas are best used when the function is very simple and only needed once.

To summarize: lambda functions are anonymous, single-expression functions used for short, temporary operations, especially in places where passing a quick function makes code cleaner. They improve code brevity but should be used carefully to keep readability.

Lambda without arguments

hello = lambda: "Hi there!"
print(hello())   # Output: Hi there!