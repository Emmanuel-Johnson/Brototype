In Python, objects are classified as mutable or immutable based on whether their internal state can be changed after creation.

Mutable objects are objects whose values can be modified in place without creating a new object. Common mutable types include lists, dictionaries, and sets. For example, if I have a list and I append a new element, the list itself changes, and its memory identity remains the same. This means multiple variables pointing to the same mutable object will see the change, which is powerful but can also lead to unexpected side effects if not handled carefully.

On the other hand, immutable objects cannot be changed after they are created. Instead, any operation that appears to modify them actually creates a new object. Common immutable types include integers, floats, strings, tuples, and frozensets. For example, if I add to an integer or modify a string, Python creates a new object rather than altering the original one. This makes immutable objects safer to share across different parts of a program.

A key concept here is object identity. Mutable objects keep the same identity when changed, while immutable objects get a new identity when modified. This difference explains why doing list.append() works, but trying to modify a string character raises an error.

Immutability also brings predictability and safety. Because immutable objects cannot change, they are hashable, which allows them to be used as dictionary keys or set elements. Mutable objects are not hashable because changing them would break hash consistency.

In function calls, mutable objects can be modified inside a function, affecting the caller, whereas immutable objects cannot be changed directly, only reassigned locally. This is a common interview trap and an important design consideration.

To summarize:

Mutable objects can be changed in place and may cause side effects

Immutable objects cannot be changed and promote safer, more predictable code

Understanding this distinction helps you write bug-free code, avoid hidden side effects, and design better APIs—which is exactly why interviewers care about it.