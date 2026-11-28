'''
Program 1: Numeric Types & the Complex Suffix
Question:
Write a program that:
Assigns a = 42, b = 3.14, and c = 2 + 3j
Prints each value and its type()
Accesses and prints the real and imaginary parts of c using .real and .imag
Creates a purely imaginary number 5j and prints its type
'''
a = 42
b = 3.14
c = 2 + 3j
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(c.imag)
print(c.real)
imaginary = 5j
print(imaginary)
print(type(imaginary))

'''
Program 2: Type Conversion & Data Loss
Question:
Write a program that:
Converts 3.99 to int using int() — prints the result and adds a comment noting it truncates rather than rounds
Converts -2.7 to int — prints the result and adds a comment noting it truncates toward zero
Converts 7 to float using float() — prints the result
Converts 2 to complex using complex(2) — prints the result
Converts 2 and 3 to complex using complex(2, 3) — prints the result
Stores 3.14159 in a variable, converts it to int, and prints the difference to demonstrate data loss
'''
a = 3.99
result1 = int(a)
print(result1)
b = -2.7
result2 = int(b)
print(result2)
c = 7
result3 = float(c)
print(result3)
result4 = complex(2)
print(result4)
result5 = complex(2, 3)
print(result5)
number = 3.14159
converted_number = int(number)
print(number)
print(converted_number)
print(number - converted_number)

'''
Program 3: Boolean & None
Question:
Write a program that:
Prints True == 1 and False == 0 to show boolean-integer equivalence
Prints True + True and True * 5 to demonstrate boolean arithmetic
Uses sum([True, False, True, True]) and adds a comment noting it counts the True values
Prints type(True) and adds a comment noting bool is a subclass of int
Assigns x = None and prints its type
Checks x is None and x == None — adds a comment noting is None is the recommended form
'''
print(True == 1)
print(False == 0)
print(True + True)
print(True * 5)
print(sum([True, False, True, True]))
print(type(True))
x = None
print(x)
print(type(x))
print(x is None)
print(x == None)

'''
Program 4: Sequence Types
Question:
Write a program that:
Creates a list [1, 2, 3] and appends 4 to show mutability
Creates a tuple (1, 2, 3)
Creates a set {1, 2, 2, 3, 3, 3} and prints it to show duplicates are removed
Creates a dict {"name": "Alice", "age": 21} and prints a value by key
Prints type() of each of the four collections
Creates two empty lists [] and [] and prints whether they are the same object using is
'''
a = [1, 2, 3]
a.append(4)
print(a)
b = (1, 2, 3)
print(b)
c = {1, 2, 2, 3, 3, 3}
print(c)
d = {"name": "Alice", "age": 21}
print(d)
print(d["name"])
print(type(a))
print(type(b))
print(type(c))
print(type(d))

'''
Program 5: Putting It All Together — Range & Full Integration
Question:
Write a program that investigates range parameters and integrates all data type concepts:
Prints list(range(5)), list(range(2, 8)), list(range(0, 11, 2)), and list(range(10, 0, -1))
Adds comments noting the default start is 0 and default step is 1, and that stop is exclusive
Prints list(range(5, 5)) and adds a comment explaining why it is empty
Prints the size of range(1_000_000_000) using __sizeof__() and adds a comment noting range is memory-efficient
Uses a for loop over range(0, 11, 2) to print even numbers up to 10
Builds a summary dict combining all types: {"ints": [10, 20], "float": 3.14, "complex": 2+3j, "bool": True, "none": None, "list": [1, 2], "tuple": (1, 2), "set": {1, 2}}
Iterates over the summary dict and prints each key, value, and type(value)
'''
print(list(range(5)))
print(list(range(2, 8)))
print(list(range(0, 11, 2)))
print(list(range(10, 0, -1)))
print(list(range(5, 5)))
r = range(1_000_000_000)
print(r.__sizeof__())
print("Even numbers from 0 to 10:")
for num in range(0, 11, 2):
    print(num)
summary = {
    "ints": [10, 20],
    "float": 3.14,
    "complex": 2+3j,
    "bool": True,
    "none": None,
    "list": [1, 2],
    "tuple": (1, 2),
    "set": {1, 2}
}
print("\nSummary of Data Types:")
for key, value in summary.items():
    print("Key:", key, "| Value:", value, "| Type:", type(value))