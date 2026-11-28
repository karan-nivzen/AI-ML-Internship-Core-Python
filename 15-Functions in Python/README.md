# Introduction to Functions in Python

## Table of Contents

- Overview
- Why Functions Matter
- Defining a Function
- Parameters and Arguments
- Return vs Print
- Comments and Docstrings
- Calling Functions
- IDE Usage
- Quick Reference
- Key Takeaways

---

## Overview

Functions are reusable blocks of code that encapsulate logic, accept input via parameters, and optionally return a result. Python defines functions with the `def` keyword, uses indentation for the function body, and relies on `return` to send values back to the caller. Moving from the interactive prompt to an IDE like VS Code or PyCharm improves project organization, editing, and debugging.

---

## Why Functions Matter

- Eliminate repetition (DRY principle — Don't Repeat Yourself)
- Centralize logic so changes happen in one place
- Improve readability and maintainability in large projects
- Allow the same logic to be called many times, from many places

Without functions, repetitive code becomes error-prone and hard to maintain as projects grow.

---

## Defining a Function

Syntax rules:

- Start with `def`
- Function name followed by parentheses `()`
- End the line with a colon `:`
- Indent the body (no braces `{}` in Python)
- Use consistent indentation (spaces or tabs, not mixed)

```python
def greet():
    print("Hello, world!")
```

Call it with `greet()`.

---

## Parameters and Arguments

Parameters make functions dynamic instead of hardcoded.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

- `a` and `b` are **parameters** (in the definition)
- `3` and `5` are **arguments** (at call time)
- The same function works with any input

---

## Return vs Print

| Behavior | Effect |
|----------|--------|
| `print()` inside function | Sends output directly to console |
| `return` inside function | Sends value back to caller |

```python
def add_print(a, b):
    print(a + b)        # prints, returns None

def add_return(a, b):
    return a + b        # returns value

add_print(2, 3)         # 5
x = add_return(2, 3)    # x = 5
print(x * 10)           # 50
```

> Returning gives the caller control — to print, store, pass along, or process further. Printing ends the conversation inside the function.

---

## Comments and Docstrings

**Comments** — notes for humans, ignored by Python:

```python
# This function adds two numbers
def add(a, b):
    return a + b
```

**Docstrings** — triple-quoted descriptions placed right after the function signature:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

- Accessible via `help(add)` or IDE hover
- Critical for collaboration and long-term maintenance

---

## Calling Functions

Once defined, a function can be called repeatedly:

```python
def square(n):
    return n * n

print(square(4))    # 16
print(square(7))    # 49
print(square(10))   # 100
```

Functions defined in one file can be imported into another, enabling reuse across a project.

---

## IDE Usage

Moving from the interactive prompt to an IDE improves workflow:

| Feature | Benefit |
|---------|---------|
| Project folders | Organize related files |
| Multi-line editor | Write and edit scripts easily |
| Run/debug tools | Execute and inspect code |
| Docstring hover | See function descriptions inline |

Common choices: **VS Code**, **PyCharm**.

Basic workflow:
1. Open a folder as a project
2. Create a `.py` file
3. Write the function
4. Run the script from the IDE terminal

---

## Quick Reference

```python
# Define
def name(param1, param2):
    """Docstring."""
    # body
    return value

# Call
name(arg1, arg2)

# Comment
# single-line note

# Docstring
"""multi-line description"""
```
