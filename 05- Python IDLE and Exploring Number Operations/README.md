# Introduction to Python Basics Using Command Line and Python IDLE

A hands-on introduction to running Python in the interactive shell — covering basic arithmetic, operator precedence, division types, and variables, all from the command line.

---

##  Overview

This guide walks beginners through using Python's **interactive shell (REPL)** on Windows — no IDE required. It contrasts the **Command Prompt** and **PowerShell**, then demonstrates core programming fundamentals directly in the Python prompt: arithmetic, precedence rules, division operators, and variables.

---

##  Command Prompt vs. PowerShell

Before jumping into Python, it helps to understand the two Windows shell environments:

| Shell | Capabilities |
|---|---|
| **Command Prompt** | Basic command execution |
| **PowerShell** | Adds scripting abilities and Unix-like commands (e.g., `ls`, `clear`) |

PowerShell bridges Unix-style shell functionality with Windows, making it easier for users familiar with Unix to adapt — and improving automation on Windows.

---

##  The Python REPL: Your Learning Playground

The Python interactive shell — known as the **REPL** (**R**ead, **E**valuate, **P**rint **L**oop) — lets you type commands and see results instantly. It's ideal for:

-  Experimenting with syntax quickly
-  Seeing immediate effects of commands
-  Building intuition for language grammar and evaluation flow

---

##  Arithmetic Operations & Operator Precedence

Python supports standard arithmetic: addition, subtraction, multiplication, and division.

**Operator precedence follows mathematical rules** (BODMAS/BIDMAS):

```python
>>> 2 + 3 * 4
14          # multiplication happens before addition
```

**Parentheses override default precedence:**

```python
>>> (2 + 3) * 4
20
```

---

##  Exponentiation: Use `**`, Not `^`

This is a common beginner trap:

| Symbol | Meaning in Python |
|---|---|
| `**` | Exponentiation (power) ✅ |
| `^` | Bitwise XOR ❌ (not power) |

```python
>>> 2 ** 3
8
```

In some languages and spreadsheets, `^` means power — but in Python, it doesn't. Always use `**`.

---

##  The Three Division Operators

Python offers distinct division operators, each serving a different purpose:

| Operator | Name | Result | Example |
|---|---|---|---|
| `/` | Floating-point division | Decimal result | `7 / 2` → `3.5` |
| `//` | Integer (floor) division | Quotient only | `7 // 2` → `3` |
| `%` | Modulus | Remainder | `7 % 2` → `1` |

- `/` gives **real division** with decimals
- `//` discards the remainder — useful for whole-number quotients
- `%` is essential for **modular arithmetic** and divisibility/periodicity algorithms

---

##  Syntax Compliance Matters

Python is strict about syntax. Invalid input results in errors — which is actually helpful for learning:

```python
>>> 2 + * 3
SyntaxError: invalid syntax
```

Errors teach you the rules quickly and build good habits early.

---

##  Variables: Named Containers for Values

Variables store values under meaningful names, improving **reusability** and **readability**:

```python
>>> num_one = 10
>>> num_two = 5
>>> result = num_one + num_two
>>> result
15
```

Variables abstract raw data and let you compute incrementally — no retyping numbers.

---

##  The Underscore `_` Shortcut

In the Python REPL, `_` holds the **result of the last executed expression**:

```python
>>> 5 + 3
8
>>> _ * 2
16
```

This streamlines calculations that depend on previous results and reduces copy errors.
