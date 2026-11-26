'''
Program 1: Quote Handling (Single vs. Double)
Question:
Create a Python program that stores the sentence It's a beautiful day in a variable and prints it. Then store the sentence She said "Hello" in another variable and print it. Use both single and double quotes appropriately to avoid syntax errors.
'''
a = "It's a beautiful day"
print(a)
b = 'She said "Hello"'
print(b)

'''
Program 2: Escape Characters
Question:
Write a program that prints the sentence He said, "Python's fun!" using escape characters — not by switching quote types. Your string must be enclosed in single quotes.
'''
a = "He said, \"Python\'s fun!\""
print(a)

'''
Program 3: String Multiplication
Question:
Write a program that prints a decorative separator line using string multiplication. The program should:
Print = repeated 40 times
Print the word WELCOME in the middle
Print = repeated 40 times again
Print - repeated 20 times
'''
print("=" * 40)
print("WELCOME")
print("=" * 40)
print("-" * 20)

'''
Program 4: The Backslash Trap (File Paths)
Question:
A student writes the following code intending to print a Windows file path, but the output is wrong:
path = "C:\new_folder\test"
print(path)
Write the corrected version that prints the path exactly as intended: C:\new_folder\test
'''
#Method-1
path = r"C:\new_folder\test"
print(path)
path = "C:\new_folder\test"
print(path)
path = "C:\\new_folder\\test"
print(path)

'''
Program 5: Combined Challenge (Quotes + Escape + Multiplication)
Question:
Write a program that prints the following output exactly, using a single print() statement with escape characters and string multiplication:
*** "Python" is 'fun' ***
'''
a = "*" * 3 + ' \"Python\" is \'fun\' ' + "*" * 3
print(a)
