# Python Lists: Basics, Operations, and Functions

A complete beginner's guide to Python lists — covering creation, indexing, slicing, nested lists, list methods, mutability, deletion, and built-in functions.

---

##  Overview

A **list** in Python is an ordered collection of values enclosed in square brackets `[]`. Where a single variable holds one value, a list holds many — making it the fundamental data structure for managing collections of data. This guide covers everything from creation to manipulation.

---

##  Creating a List

```python
nums = [10, 20, 30, 40, 50]
names = ["Alice", "Bob", "Charlie"]
mixed = ["Naveen", 67, 6.5, True]   # heterogeneous
```

Lists can hold **any data type** — and even other lists.

---

##  Indexing

Lists use **zero-based indexing**. The first element is at index `0`:

```python
>>> nums = [10, 20, 30, 40, 50]
>>> nums[0]
10
>>> nums[2]
30
```

### Negative Indexing

Access elements from the end:

```python
>>> nums[-1]
50      # last element
>>> nums[-2]
40      # second to last
```

---

##  Slicing

Extract a **sub-list** using `[start:stop]` — start inclusive, **stop exclusive**:

```python
>>> nums = [10, 20, 30, 40, 50]
>>> nums[2:4]
[30, 40]      # indices 2 and 3
>>> nums[2:]
[30, 40, 50]  # to the end
>>> nums[:3]
[10, 20, 30]  # from the beginning
```

| Slice | Result |
|---|---|
| `[a:b]` | Elements from `a` up to `b-1` |
| `[:b]` | From start to `b-1` |
| `[a:]` | From `a` to end |

>  Same half-open rule as strings — consistent across Python sequences.

---

##  Heterogeneous Lists

Python lists allow **mixed data types** in one list — unlike strongly typed languages:

```python
mixed = ["Naveen", 67, 6.5]
```

This flexibility lets you model complex real-world data without rigid structuring.

---

##  Nested Lists

Lists inside lists model **multi-dimensional data**:

```python
nums = [10, 20, 30]
names = ["Alice", "Bob", "Charlie"]
combined = [nums, names]        # nested

>>> combined[0]
[10, 20, 30]
>>> combined[0][0]
10                              # double indexing
>>> combined[1][2]
'Charlie'
```

---

##  Combining Lists

| Method | Syntax | Result |
|---|---|---|
| **Nested** | `[nums, names]` | Two lists as elements |
| **Concatenation** | `nums + names` | One flat combined list |

```python
>>> nums + names
[10, 20, 30, 'Alice', 'Bob', 'Charlie']
```

---

##  List Methods

| Method | Description |
|---|---|
| `append(x)` | Adds `x` to the **end** |
| `insert(i, x)` | Inserts `x` at index `i`, shifting others |
| `remove(x)` | Removes **first occurrence** of value `x` |
| `pop([i])` | Removes and returns element at `i` (default: last) — LIFO |
| `extend(iterable)` | Adds multiple elements from another iterable |
| `clear()` | Removes all elements |
| `reverse()` | Reverses the list **in place** |
| `sort()` | Sorts ascending (numeric or lex order) |

### Examples

```python
>>> nums = [10, 20, 30]
>>> nums.append(40)
>>> nums
[10, 20, 30, 40]

>>> nums.insert(1, 15)
>>> nums
[10, 15, 20, 30, 40]

>>> nums.remove(20)
>>> nums
[10, 15, 30, 40]

>>> nums.pop()
40
>>> nums
[10, 15, 30]

>>> nums.extend([50, 60])
>>> nums
[10, 15, 30, 50, 60]

>>> nums.reverse()
>>> nums
[60, 50, 30, 15, 10]

>>> nums.sort()
>>> nums
[10, 15, 30, 50, 60]
```

>  **`append()` vs `insert()`:** `append()` adds at the end; `insert(i, x)` adds at a specific index.

---

##  Mutability: Lists vs. Strings

| Feature | Strings | Lists |
|---|---|---|
| **Mutable?** | ❌ Immutable | ✅ Mutable |
| **Change element?** | Not by index | Yes, by index or methods |

```python
>>> nums = [10, 20, 30]
>>> nums[0] = 99          # ✅ allowed
>>> nums
[99, 20, 30]
```

Lists can be changed after creation — strings cannot.

---

##  Deleting Elements

### Using `del` (by index/slice)

```python
>>> nums = [10, 20, 30, 40, 50]
>>> del nums[2:4]
>>> nums
[10, 20, 50]
```

### Using `remove()` (by value)

```python
>>> nums.remove(20)
>>> nums
[10, 50]
```

>  **Difference:** `del` deletes by **index/range**; `remove()` deletes by **value**.

---

##  Built-in Functions on Lists

| Function | Returns | Works On |
|---|---|---|
| `min(list)` | Smallest element | Numbers, strings (lex) |
| `max(list)` | Largest element | Numbers, strings (lex) |
| `sum(list)` | Total | Numeric lists only |

```python
>>> nums = [10, 20, 30]
>>> min(nums)
10
>>> max(nums)
30
>>> sum(nums)
60
```

>  `sum()` fails on non-numeric lists — know your data types first.

---

##  Practical Notes on Python IDLE

-  **Method autocompletion** — type `nums.` and press Tab to explore methods
-  **History navigation** — press **Alt + P** to recall previous commands
-  Great for **iterative testing** of list operations

---

*This guide provides a comprehensive introduction for beginners to get started with Python lists, their usage, and basic manipulation techniques — setting the foundation for future exploration of more complex data structures.*
