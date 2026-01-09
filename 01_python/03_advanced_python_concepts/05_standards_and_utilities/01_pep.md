A PEP ( Python Enhancement Proposal ) is an official design document that explains new features, process changes, or best practices for Python. In simple terms, PEPs define how Python evolves.

## Why PEPs exist
Python is an open-source language with contributors from all over the world. PEPs provide a standard way to propose, discuss, and document changes so everyone follows a clear and transparent process.

They answer questions like:
- Why is this feature needed?
- How should it work?
- Is it backward compatible?
- What are the alternatives?

## Types of PEPs

### 1. Standards Track PEPs
Describe new language features or behavior changes.

Examples:
- New syntax
- Changes to Python internals
- Library additions

Example:
```py
# PEP 484 — Type hints
def add(a: int, b: int) -> int:
    return a + b
```

### 2. Informational PEPs
Provide guidelines or explanations but don’t change Python itself.

Example:
- PEP 20 — The Zen of Python
> "Simple is better than complex."

### 3. Process PEPs
Describe how Python development works.

Example:
- PEP 1 — Explains how to write and submit a PEP.

## Most important PEP for interviews
**PEP 8 — Python Style Guide**

PEP 8 defines coding standards to keep Python code readable, consistent, and maintainable.

Key rules:
- Use `snake_case` for variables and functions
- Use `PascalCase` for classes
- Limit line length to 79 characters
- Use proper indentation (4 spaces)

Interviewers like to hear:
> "I follow PEP 8 for clean and readable code."

## PEP lifecycle (briefly)
A PEP typically goes through:
- Draft
- Discussion
- Accepted / Rejected
- Implemented
- Final

Only accepted PEPs become part of Python.

## One-line summary (Interview gold)
> PEPs are official documents that define Python’s features, coding standards, and development process. PEP 8 is the most important for writing clean Python code.
