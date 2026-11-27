'''
Program 1: Set Creation & Uniqueness
Question:
Create the following in a Python program:
A set called fruits containing "apple", "banana", "cherry", "apple", "banana", "date" — created using curly braces
A set called numbers created from the list [10, 20, 20, 30, 30, 30, 40] using the set() constructor
An empty set called empty — correctly created
An empty dictionary called empty_dict — and print its type to confirm it is not a set
Write a program that prints all four, along with their types using type(). 
'''
fruits = {"apple", "banana", "cherry", "apple", "banana", "date" }
numbers = [10, 20, 20, 30, 30, 30, 40] 
print(set(numbers))
empty = set()
empty_dict = {}
print(fruits)
print(type(fruits))

'''
Program 2: Membership Testing & Length
Question:
Create the set colors = {"red", "green", "blue", "yellow"}.
Write a program that:
Checks if "green" is in the set using in and prints the result
Checks if "purple" is in the set and prints the result
Checks if "Green" (capitalized) is in the set and prints the result
Prints the length of the set using len()
Prints the type of the set using type()
'''
colors = {"red", "green", "blue", "yellow"}
print("green" in colors)
print("purple" in colors)
print("Green" in colors)
print(len(colors))
print(type(colors))

'''
Program 3: Mathematical Set Operations
Question:
Create two sets:
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
Write a program that computes and prints:
Difference — elements in a but not in b (using -)
Union — elements in a or b (using |)
Intersection — elements in both a and b (using &)
Symmetric difference — elements in exactly one of the two sets (using ^)
The reverse difference — elements in b but not in a
'''
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)
print(b - a)

'''
Program 4: Duplicate Removal & Unordered Behavior
Question:
A teacher has a list of student names with duplicates:
python
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David", "Alice"]
Write a program that:
Converts the list to a set and prints the resulting set
Prints how many unique names there are using len()
Prints how many total names were in the original list
Prints the set three times and observes whether the order changes between runs
'''
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "David", "Alice"]
a = set(names)
print(a)
print(len(a))
print(len(names))
print(a)
print(a)
print(a)

'''
Program 5: Set Operations Challenge — Combining Concepts
Question:
Two classes have students who took different exams:
python
class_a = {"Naveen", "Ravi", "Kiran", "Priya", "Anu"}
class_b = {"Ravi", "Priya", "Deepa", "Arjun"}
Write a program that computes and prints:
Students who took both exams (intersection)
All students across both classes (union)
Students who took only the first exam (difference: class_a - class_b)
Students who took exactly one of the two exams (symmetric difference)
Whether "Naveen" is in class_b (membership test)
Whether "naveen" (lowercase) is in class_a — and explain the result in a comment
The total number of unique students across both classes using len()
'''
class_a = {"Naveen", "Ravi", "Kiran", "Priya", "Anu"}
class_b = {"Ravi", "Priya", "Deepa", "Arjun"}
print(class_a & class_b)
print(class_a | class_b)
print(class_a - class_b)
print(class_a ^ class_b)
print("Naveen" in class_b)
print("naveen" in class_a)
print(len(class_a | class_b))
