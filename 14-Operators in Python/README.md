# Operators in Python

## Table of Contents

- Overview
- Arithmetic Operators
- Assignment Operators
- Unary vs Binary Operators
- Relational Operators
- Assignment vs Equality
- Logical Operators
- Truth Tables
- Quick Reference

---

## Overview

Python provides three primary operator categories:

- **Arithmetic** — perform numeric computation
- **Relational** — compare values and return Boolean results
- **Logical** — combine Boolean expressions

Understanding operator arity (unary vs binary) and the distinction between assignment and equality is essential for writing bug-free code.

---

## Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 3` | `13` |
| `-` | Subtraction | `10 - 3` | `7` |
| `*` | Multiplication | `10 * 3` | `30` |
| `/` | Division | `10 / 3` | `3.333...` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulo | `10 % 3` | `1` |
| `**` | Exponent | `10 ** 3` | `1000` |

```python
a = 10
b = 3
print(a + b)    # 13
print(a // b)   # 3
print(a % b)    # 1
print(a ** b)   # 1000
```

---

## Assignment Operators

Shorthand forms reduce redundancy:

| Operator | Equivalent |
|----------|------------|
| `a += 2` | `a = a + 2` |
| `a -= 2` | `a = a - 2` |
| `a *= 2` | `a = a * 2` |
| `a /= 2` | `a = a / 2` |
| `a //= 2` | `a = a // 2` |
| `a %= 2` | `a = a % 2` |
| `a **= 2` | `a = a ** 2` |

```python
a = 5
a += 2      # a = 7
a *= 3      # a = 21
```

> Note: `a++` and `a--` are **invalid** in Python.

---

## Unary vs Binary Operators

| Arity | Description | Example |
|-------|-------------|---------|
| Binary | Two operands | `a + b` |
| Unary | One operand | `-a`, `+a`, `not a` |

```python
a = 10
print(-a)       # unary minus → -10
print(a + 5)    # binary addition → 15
print(not True) # unary logical not → False
```

---

## Relational Operators

Always return `True` or `False`:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater or equal | `5 >= 5` | `True` |
| `<=` | Less or equal | `5 <= 3` | `False` |

```python
a = 10
b = 20
print(a < b)     # True
print(a == b)    # False
print(a != b)    # True
```

---

## Assignment vs Equality

| Operator | Purpose | Example |
|----------|---------|---------|
| `=` | Assigns a value | `a = 5` |
| `==` | Compares values | `a == 5` |

```python
a = 5           # assignment
print(a == 5)   # equality check → True
# print(a = 5)  # SyntaxError
```

> Confusing `=` with `==` is a common bug. Python prevents assignment inside expressions, reducing errors.

---

## Logical Operators

| Operator | Description | Returns True When |
|----------|-------------|-------------------|
| `and` | Logical AND | Both operands are True |
| `or` | Logical OR | At least one operand is True |
| `not` | Logical NOT | Operand is False |

```python
x = 10
y = 20

print(x > 5 and y > 15)    # True
print(x > 15 or y > 15)    # True
print(not (x > 5))         # False
```

---

## Truth Tables

### AND

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

### OR

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

### NOT

| A | not A |
|---|-------|
| True | False |
| False | True |

---

## Quick Reference

```python
# Arithmetic
a + b, a - b, a * b, a / b
a // b, a % b, a ** b

# Assignment
a += 2, a -= 2, a *= 2, a /= 2

# Relational (return bool)
a == b, a != b, a > b, a < b, a >= b, a <= b

# Logical
a and b, a or b, not a
```
