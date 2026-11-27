'''
Program 1: Variables as References & id()
Question:
Write a program that:
Assigns a = 10 and b = 10
Prints the id() of both a and b
Prints whether a is b and adds a comment explaining why they share the same object
Reassigns a = 20 and prints the new id() of a
Compares the old and new id() of a — prints whether they differ and explains in a comment what happened to the old object
Prints id(b) again to confirm b still references the original object
'''
a = 10
b = 10
print(id(a))
print(id(b))
print(a is b)
old_id = id(a)
print(old_id)
a = 20
new_id = id(a)
print(new_id)
print(old_id != new_id)
print(id(b))

'''
Program 2: Small Number Caching
Question:
Write a program that tests Python's small-integer caching behavior:
Assigns x = 100 and y = 100 — prints x is y and their id()s
Assigns x = 1000 and y = 1000 — prints x is y and their id()s
Assigns x = -5 and y = -5 — prints x is y
Assigns x = -6 and y = -6 — prints x is y
Uses a loop to test caching for values 250 through 260 — prints value: cached/not cached for each
'''
print("=" * 25)
x = 100
y = 100
print(x is y)
print(id(x))
print(id(y))
print("=" * 25)
x = 1000
y = 1000
print(x is y)
print(id(x))
print(id(y))
print("=" * 25)
x = -5
y = -5
print(x is y)
print(id(x))
print(id(y))
print("=" * 25)
x = -6
y = -6
print(x is y)
print(id(x))
print(id(y))
for value in range(250, 261):
    x = value
    y = value

    if x is y:
        print(value, ": cached")
    else:
        print(value, ": not cached")

'''
Program 3: String Interning — Small vs. Long Strings
Question:
Write a program that demonstrates string interning:
Creates two variables with the same small string: a = "hello", b = "hello" — prints a is b and both id()s
Creates two variables with a long string containing spaces: c = "this is a long string with spaces", d = "this is a long string with spaces" — prints c is d and both id()s
Creates two variables with a single-word long string: e = "abcdefghijklmnop", f = "abcdefghijklmnop" — prints e is f and both id()s
'''
print("=" * 25)
a = "hello"
b = "hello"
print(a is b)
print(id(a))
print(id(b))
print("=" * 25)
c = "this is a long string with spaces"
d = "this is a long string with spaces"
print(c is d)
print(id(c))
print(id(d))
print("=" * 25)
e = "abcdefghijklmnop"
f = "abcdefghijklmnop"
print(e is f)
print(id(e))
print(id(f))

'''Program 4: Rebinding & Garbage Collection
Question:
Write a program that:
Creates a list data = [1, 2, 3, 4, 5] and prints its id()
Creates another reference to the same list: alias = data — prints whether alias is data and both id()s
Modifies the list through alias (e.g., alias.append(6)) and prints data — confirming both names see the change
Rebinds data = None and prints alias — showing the list still exists because alias references it
Rebinds alias = None — adds a comment explaining that the list now has no references and will be cleaned up by the garbage collector
Creates a new list, prints its id(), and compares it with the original list's id() — adds a comment explaining whether the memory addresses could be reused
'''
data = [1, 2, 3, 4, 5]
a = id(data)
print(data)
print(a)
alias = data
print(alias is data)
print(id(data))
print(id(alias))
alias.append(6)
print(data)
print(alias)
data = None
print(data)
print(alias)
alias = None
print(alias)
l = [10, 20, 30]
l_id = id(l)
print(l)
print(l_id)
print(a == l_id)

'''
Program 5: Putting It All Together — Identity Investigation
Question:
Write a program that investigates object identity across multiple data types:
For each of the following pairs, print the values, their id()s, and whether they are the same object (is):
Two small integers: 10 and 10
Two large integers: 10000 and 10000
Two small strings: "python" and "python"
Two long strings: "python programming language" and "python programming language"
Two empty lists: [] and []
Two tuples with the same values: (1, 2, 3) and (1, 2, 3)
'''
a = 10
b = 10
print(a, b)
print(id(a), id(b))
print(a is b)
c = 10000
d = 10000
print(c, d)
print(id(c), id(d))
print(c is d)
e = "python"
f = "python"
print(e, f)
print(id(e), id(f))
print(e is f)
g = "python programming language"
h = "python programming language"
print(g, h)
print(id(g), id(h))
print(g is h)
i = []
j = []
print(i, j)
print(id(i), id(j))
print(i is j)
k = (1, 2, 3)
l = (1, 2, 3)
print(k, l)
print(id(k), id(l))
print(k is l)

