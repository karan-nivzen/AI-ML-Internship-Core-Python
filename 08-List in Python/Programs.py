'''
Program 1: List Basics & Indexing
Question:
Create a list called fruits containing "apple", "banana", "cherry", "date", and "elderberry".
Write a program that prints:
The first fruit using positive indexing
The last fruit using negative indexing
The third fruit using positive indexing
The second-to-last fruit using negative indexing
'''
a = ["apple", "banana", "cherry", "date", "elderberry"]
print(a[0])
print(a[-1])
print(a[2])
print(a[-2])

'''
Program 2: Slicing & Heterogeneous Lists
Question:
Create a heterogeneous list called mixed containing: "Naveen", 67, 6.5, "Python", 100, "Data".
Write a program that prints:
The first three elements using slicing
Elements from index 2 to the end
Elements from index 1 up to (but not including) index 4
The entire list using slicing
The last two elements using negative slicing
'''
a = ["Naveen", 67, 6.5, "Python", 100, "Data"]
print(a[0:3])
print(a[2:])
print(a[1:4])
print(a[:])
print(a[-2:])

'''
Program 3: Nested Lists & Concatenation
Question:
Create two lists:
nums = [10, 20, 30]
names = ["Alice", "Bob", "Charlie"]
Write a program that:
Creates a nested list from nums and names and prints it
Prints the first element of nums using double indexing on the nested list
Prints the last element of names using double indexing on the nested list
Creates a concatenated list using the + operator and prints it
Prints the length of the concatenated list
'''
nums = [10, 20, 30]
names = ["Alice", "Bob", "Charlie"]
a = [nums, names]
print(a)
print(a[0][0])
print(a[1][-1])
b = nums + names
print(b)
print(len(b))


''''
Program 4: List Methods Challenge
Question:
Start with the list numbers = [30, 10, 40, 20, 50].
Perform the following operations in order, printing the list after each step:
append(60) — add to the end
insert(2, 25) — insert at index 2
remove(40) — remove by value
pop() — remove and print the last element
extend([70, 80]) — add multiple elements
reverse() — reverse in place
sort() — sort in ascending order
clear() — remove all elements
'''
numbers = [30, 10, 40, 20, 50]
print(numbers.append(60))
print(numbers.insert(2,25))
print(numbers.remove(40))
print(numbers.pop())
print(numbers.extend([70, 80]))
print(numbers.reverse())
print(numbers.sort())
print(numbers.clear())

'''
Program 5: Mutability & del Keyword
Question:
Create the list data = [5, 10, 15, 20, 25, 30, 35, 40].
Write a program that:
Changes the element at index 0 to 100 (demonstrating mutability) and prints the list
Uses the del keyword to delete elements from index 2 to 4 (i.e., del data[2:4]) and prints the list
Uses del to delete a single element at index 1 and prints the list
Uses remove() to delete the value 30 and prints the list
Prints the final min(), max(), and sum() of the list
Bonus: Explain in a comment why del data[2:4] removes two elements but del data[1] removes only one.
'''
data = [5, 10, 15, 20, 25, 30, 35, 40]
data[0] = 100
print(data)
del data[2:4]
print(data)
del data[1]
print(data)
print(data.remove(30))
print(min(data))
print(max(data))
print(sum(data))
