'''
Program 1: Arithmetic Operators & Operator Arity
Question:
Write a program that:
Assigns a = 15 and b = 4
Prints the results of a + b, a - b, a * b, a / b
Prints the results of a // b, a % b, a ** b
Demonstrates a unary operator with -a and explains in a comment how it differs from binary a - b
Prints type() of the result of a / b and a // b to show they differ
'''
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
print(-a)
print(type(a / b))
print(type(a // b))

'''
Program 2: Assignment Operators & Shorthand Forms
Question:
Write a program that:
Starts with x = 10 and prints its value and id()
Applies x += 5, prints the new value, and adds a comment explaining it is equivalent to x = x + 5
Applies x -= 3, x *= 2, x /= 4, x //= 2, x %= 3, x **= 2 one at a time, printing after each
Compares the id() of x before and after x += 5 — adds a comment explaining whether a new object was created
Attempts to write x++ in a comment and notes that Python does not support it
'''
x = 10
print(x)
print(id(x))
old_id = id(x)
x += 5 
print(x)
print(id(x))
print(old_id)
x -= 3
print(x)
x *= 2
print(x)
x /= 4
print(x)
x //= 2
print(x)
x %= 3
print(x)
x **= 2
print(x)

'''
Program 3: Relational Operators & Assignment vs Equality
Question:
Write a program that:
Assigns p = 12 and q = 20
Prints results of p == q, p != q, p > q, p < q, p >= q, p <= q
Prints type() of each result and adds a comment confirming all are bool
Writes a line using = (assignment) and a line using == (equality) and explains the difference in comments
Uses a relational result in an if statement to show how Boolean output drives control flow
'''
p = 12
q = 20
print(p == q)
print(p != q)
print(p > q)
print(p < q)
print(p >= q)
print(p <= q)
print(type(p == q))
print(type(p != q))
print(type(p > q))
print(type(p < q))
print(type(p >= q))
print(type(p <= q))
x = 10
print(x)
print(x == 10)
if p < q:
    print("\np is less than q")
else:
    print("\np is greater than or equal to q")

'''
Program 4: Logical Operators & Truth Tables
Question:
Write a program that:
Assigns a = True and b = False
Prints results of a and b, a or b, not a, not b
Builds a truth table for and using nested loops over [True, False] and formatted string output
Builds truth tables for or and not the same way
Adds comments summarizing: and needs both true, or needs at least one true, not inverts
Uses logical operators in a real condition — for example, age > 18 and has_id — and prints the result with type()
'''
a = True
b = False
print(a and b)
print(a or b)
print(not a)
print(not b)
print("\nAND Truth Table:")
print("A       B       A and B")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7} {str(b):<7} {a and b}")
print("\nOR Truth Table:")
print("A       B       A or B")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<7} {str(b):<7} {a or b}")
print("\nNOT Truth Table:")
print("A       not A")
for a in [True, False]:
    print(f"{str(a):<7} {not a}")
age = 21
has_id = True
result = age > 18 and has_id
print(age)
print(has_id)
print(result)
print(type(result))

'''
Program 5: Putting It All Together — Operator Investigation
Question:
Write a program that investigates operator behavior across categories:
For arithmetic, prints results of +, -, *, /, //, %, ** on a = 17 and b = 5, with a comment for each explaining the operation
For assignment, starts total = 0 and uses += in a for loop over range(1, 6) — prints the final total and confirms it equals the sum of 1 to 5
For relational, compares two variables with all six operators and stores each result in a list — prints the list and confirms every element is bool
For logical, combines arithmetic and relational results, e.g., (a + b > 20) and (a % 2 == 1) — prints result and type()
'''
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print( a ** b)
total = 0
for num in range(1, 6):
    total += num
print(total)
print(sum(range(1, 6)))
print(total == sum(range(1, 6)))
x = 10
y = 20
results = [
    x == y,  
    x != y,  
    x > y,   
    x < y,   
    x >= y,  
    x <= y   
]
print(results)
print([type(value) for value in results])
print(all(type(value) == bool for value in results))
logical_result = (a + b > 20) and (a % 2 == 1)
print(logical_result)
print(type(logical_result))

