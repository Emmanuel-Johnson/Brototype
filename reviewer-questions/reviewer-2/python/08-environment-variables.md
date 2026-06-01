- Environment variables are system values used to store configuration data like API keys, database URLs, or port numbers.
- They help keep sensitive or changeable information separate from the code.
- This makes applications more secure and easier to manage across different environments.


Environment variables are read using the os module in Python.

```python
import os

name = os.getenv("USERNAME")

print(name)
```

- os.getenv("VARIABLE_NAME") reads the environment variable
- It returns None if the variable is not found
- Commonly used for passwords, API keys, and configuration settings