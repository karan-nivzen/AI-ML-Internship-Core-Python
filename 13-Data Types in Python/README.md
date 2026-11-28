#  Python Data Types 

##  Numeric Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Whole numbers | `42` |
| `float` | Decimals | `3.14` |
| `complex` | Real + imaginary (`j`, not `i`) | `3+4j` |

---

##  Type Conversion

```python
int(3.14)      # 3    truncates (data loss)
float(5)       # 5.0
complex(2, 3)  # (2+3j)
```

---

##  Boolean

`True` = `1`, `False` = `0` (subclass of `int`)

```python
True + True        # 2
sum([True, False]) # 1
```

---

##  None

Represents "no value" (like `null`). Compare with `is None`, not `==`.

```python
x = None
x is None   # True
```

---

##  Sequence Types

| Type | Mutable | Ordered | Duplicates | Syntax |
|------|---------|---------|------------|--------|
| `list` | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| `tuple` | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| `set` | ✅ | ❌ | ❌ | `{1, 2, 3}` |
| `dict` | ✅ | ✅ | unique keys | `{"a": 1}` |

---

##  Range

`range(start=0, stop, step=1)` — **stop is exclusive**, memory-efficient.

```python
range(5)            # 0,1,2,3,4
range(0, 11, 2)     # 0,2,4,6,8,10
range(10, 0, -1)    # 10,9,...,1
```

---

##  Type Checking

```python
type(42)      # <class 'int'>
type(3.14)    # <class 'float'>
type(None)    # <class 'NoneType'>
```

> **Bottom line:** Master these types + conversions → robust, efficient Python. When in doubt, `type()` it out! 
