In Python, unpacking is the process of assigning elements from an iterable to multiple variables in a single statement. Instead of accessing elements one by one, Python allows us to extract values directly based on position, which makes code cleaner, more readable, and more Pythonic.

The most common example is sequence unpacking, where values from a sequence are assigned to variables. For instance, when a sequence has the same number of elements as the variables on the left side, Python automatically maps each value to its corresponding variable.

Python supports unpacking in many contexts, not just assignments. It is widely used in loops, function returns, and function arguments.

Now, coming to what can be unpacked.

In Python, any iterable can be unpacked. This includes:

Lists

Tuples

Strings

Sets

Dictionaries

Ranges

Custom objects that implement the iterator protocol

For strings, unpacking extracts individual characters. For sets, unpacking works but the order is not guaranteed, because sets are unordered. For dictionaries, unpacking extracts keys by default, not values.

Python also supports extended unpacking using the * operator. This allows one variable to collect multiple remaining values into a list. Extended unpacking is especially useful when the number of elements is not fixed or when we care only about specific positions.

Another important use case is unpacking function return values. Python functions can return multiple values as a tuple, and unpacking lets us assign them directly to variables, which improves clarity and avoids indexing.

Unpacking is also commonly used in loops, such as iterating over pairs of values, making code more expressive and reducing boilerplate.

From an interview perspective, a key rule is that the number of variables must match the number of values, unless extended unpacking is used. Otherwise, Python raises an error.

To summarize:

Unpacking extracts elements from an iterable into variables

Any iterable can be unpacked

Extended unpacking with * allows flexible assignments

It improves readability, expressiveness, and code quality

In short, unpacking is a core Python feature that simplifies data handling and is heavily used in real-world Python code, which is why interviewers expect you to understand it clearly.