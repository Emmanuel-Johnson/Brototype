In Python, debugging tools help developers identify, analyze, and fix
errors in code. Python provides several built-in and external tools that
allow us to inspect program flow, variable values, and runtime behavior.

------------------------------------------------------------------------

## 🔹 1. Print Debugging

The simplest debugging tool is using `print()` statements.

``` python
print("Value of x:", x)
```

This helps trace program flow and check variable values, but it doesn't
scale well for large applications.

------------------------------------------------------------------------

## 🔹 2. Python Debugger -- `pdb`

Python includes a built-in interactive debugger called `pdb`.

``` python
import pdb
pdb.set_trace()
```

When execution reaches this line, the program pauses, allowing us to:

-   Step through code line by line\
-   Inspect variables\
-   Evaluate expressions\
-   Control execution flow

**Common `pdb` commands:**

-   `n` → next\
-   `s` → step into\
-   `l` → list code\
-   `c` → continue

------------------------------------------------------------------------

## 🔹 3. Using IDE Debuggers

Most IDEs like **VS Code** and **PyCharm** provide graphical debuggers.

These allow us to:

-   Set breakpoints visually\
-   Step into and over functions\
-   Watch variables in real time\
-   Inspect the call stack

IDE debuggers are more efficient and beginner-friendly than manual
debugging.

------------------------------------------------------------------------

## 🔹 4. Stack Traces

When an error occurs, Python automatically prints a stack trace.

This shows:

-   The sequence of function calls\
-   File names and line numbers\
-   The exact exception raised

Reading stack traces correctly is one of the most important debugging
skills.

------------------------------------------------------------------------

## 🔹 5. Logging

For real-world applications, we use the `logging` module instead of
`print()`.

``` python
import logging
logging.error("Something went wrong")
```

Logging allows different log levels like:

-   `DEBUG`
-   `INFO`
-   `WARNING`
-   `ERROR`
-   `CRITICAL`

It is essential for debugging production systems.

------------------------------------------------------------------------

## 🔹 6. Exception Handling

Using `try-except` blocks helps capture and analyze errors without
crashing the application.

``` python
try:
    risky_operation()
except Exception as e:
    print(e)
```

This allows controlled debugging and graceful failure.

------------------------------------------------------------------------

## 🔹 7. Profilers (Advanced)

For performance-related bugs, Python provides profiling tools like
`cProfile`.

These help identify:

-   Slow functions\
-   Performance bottlenecks

------------------------------------------------------------------------

## 🔹 Best Practices

-   Read stack traces from **bottom to top**
-   Use `pdb` for complex logic issues
-   Use **logging** instead of `print()` in production
-   Reproduce bugs consistently before fixing them

------------------------------------------------------------------------

## 🔹 Common Interview Traps

❌ Relying only on print statements\
❌ Ignoring stack traces\
❌ Debugging without reproducing the bug

------------------------------------------------------------------------

## ✅ Strong Interview Closing Line

> *"Python offers multiple debugging tools --- from print statements and
> stack traces to pdb, IDE debuggers, and logging --- allowing
> developers to efficiently identify and fix issues in both development
> and production environments."*