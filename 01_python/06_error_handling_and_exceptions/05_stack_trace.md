A stack trace is a detailed report that shows the sequence of function calls that led to an exception. It helps developers understand where an error occurred, how the program reached that point, and what caused the failure.

## What "stack" means

Python uses a call stack to keep track of active function calls. Each time a function is called, a new frame is pushed onto the stack. When the function returns, its frame is removed.

When an exception occurs, Python prints the stack trace, showing all the frames still on the stack at the moment of failure.

## Simple example

```python
def c():
    return 10 / 0

def b():
    c()

def a():
    b()

a()
```

This code raises a `ZeroDivisionError`, and Python prints a stack trace.

## How to read a stack trace

A typical Python stack trace has three key parts:

- File name and line number
- Function call sequence
- Exception type and message

Python prints the trace from the most recent call backward: the last line is the actual error, and the lines above show how execution reached that point.

## Example stack trace output

```text
Traceback (most recent call last):
  File "example.py", line 10, in <module>
    a()
  File "example.py", line 7, in a
    b()
  File "example.py", line 4, in b
    c()
  File "example.py", line 1, in c
    return 10 / 0
ZeroDivisionError: division by zero
```

The bottom line tells us what failed, and the lines above tell us where it came from.

## Why stack traces are important

Stack traces are critical for:

- Debugging runtime errors
- Understanding program flow
- Identifying the root cause instead of symptoms
- Logging errors in production systems

## Stack trace vs exception handling

If an exception is caught using `try`/`except`, the stack trace is not shown by default:

```python
try:
    a()
except Exception:
    print("Error occurred")
```

To view the stack trace, log it explicitly.

## Printing stack traces manually

```python
import traceback

try:
    a()
except Exception:
    traceback.print_exc()
```

This is commonly used in logging systems.

## Best practices

- Always read the last line first
- Follow the call stack upward to find the root cause
- Log stack traces in production
- Don’t expose raw stack traces to end users

## Common interview mistakes

- ❌ Reading the trace top-down instead of bottom-up  
- ❌ Fixing symptoms instead of the root cause  
- ❌ Ignoring line numbers

✅ Strong interview closing line:  
So in Python, a stack trace shows the sequence of function calls that led to an exception, helping developers quickly locate and fix runtime errors.
