In Python, a float is an immutable data type.

This means that once a float object is created, its value cannot be changed in place. Any operation that appears to modify a float actually creates a new float object and rebinds the variable name to that new object.

For example, if I assign a float value to a variable and then add something to it, Python does not update the original float. Instead, it creates a new float with the updated value and assigns it back to the variable. The original float object remains unchanged in memory.

This behavior exists because floats represent numeric values, and Python treats all built-in numeric types—such as integers, floats, and complex numbers—as immutable. Immutability ensures predictable behavior, simplifies memory management, and makes these objects safe to share across different parts of a program.

Immutability also affects function behavior. When a float is passed to a function, the function cannot modify the original float value. If the function assigns a new value, it only changes the local reference, not the caller’s variable. This eliminates side effects that are common with mutable objects like lists or dictionaries.

Another important implication is hashability. Since floats are immutable, they are hashable and can be used as dictionary keys or set elements. This would not be possible if floats were mutable, because changing their value would break hash consistency.

To summarize:

float objects in Python are immutable

Any “modification” creates a new float object

Passing floats to functions does not cause side effects

Floats are hashable and safe to use as dictionary keys

So in interviews, the direct and correct answer is: No, floats are not mutable in Python—they are immutable numeric objects.