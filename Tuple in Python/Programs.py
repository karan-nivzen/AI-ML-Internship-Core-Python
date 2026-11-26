'''
Program 1: Tuple Creation & Indexing
Question:
Create a tuple called colors containing "red", "green", "blue", "yellow", and "purple" — once with parentheses and once without parentheses.
Write a program that:
Prints both tuples and confirms their type using type()
Prints the first color using positive indexing
Prints the last color using negative indexing
Prints the middle color (index 2)
Creates a single-element tuple containing just "black" and prints its type
'''
a = ("red", "green", "blue", "yellow", "purple")
b = "red", "green", "blue", "yellow", "purple"
print(a)
print(b)
print(type(a))
print(type(b))
print(a[0])
print(a[-1])
print(a[2])
b = ("black",)
print(b)
print(type(b))

'''
Program 2: Tuple Functions & Limited Methods
Question:
Create the tuple numbers = (45, 12, 78, 12, 90, 12, 33).
Write a program that prints:
The smallest value using min()
The largest value using max()
The total using sum()
The number of elements using len()
How many times 12 appears using count()
The index of the first occurrence of 78 using index()
'''
numbers = (45, 12, 78, 12, 90, 12, 33)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))
print(numbers.count(12))
print(numbers.index(78))
# numbers.append(100)
print(numbers)

'''
Program 3: Tuple Unpacking
Question:
Create the tuple student = (101, "Naveen", 7.9, "Computer Science").
Write a program that:
Unpacks the tuple into four variables: roll_no, name, gpa, and subject in a single statement
Prints each variable with a label
Unpacks only the first two elements into roll_no and name, and the remaining elements into a list called rest using the * operator
Prints rest and its type
'''
student = (101, "Naveen", 7.9, "Computer Science")
roll_no, name, gpa, subject = student
print("Roll No: ", roll_no)
print("Name: ", name)
print("GPA: ", gpa)
print("Subject: ", subject)

'''
Program 4: Nested Structures & Mutable Contents
Question:
Create the tuple record = (1, "Alice", [85, 90, 78]).
Write a program that:
Prints the tuple
Accesses and prints the list inside the tuple using indexing
Appends 95 to the list inside the tuple and prints the updated tuple
Changes the second element of the inner list to 100 and prints the updated tuple
'''
record = (1, "Alice", [85, 90, 78])
print(record)
print(record[2])
record[2].append(95)
print(record)
record[2][1] = 100
print(record)