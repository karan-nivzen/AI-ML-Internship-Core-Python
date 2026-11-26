'''
Program 1: Concatenation (Implicit vs. Explicit)
Question:
Create three string variables: first = "Python", second = "Programming", and space = " ". Using these variables, produce the output Python Programming in two ways:
Using implicit concatenation (literals only)
Using explicit concatenation with the + operator
Then explain why implicit concatenation doesn't work with variables.
'''
first = "Python"
second = "Programming"
space = " "

a = "Python" " " "Programming"
print(a)
b = first + space + second
print(b)

'''
Program 2: Positive and Negative Indexing
Question:
Given the string word = "Programming", write a program that prints:
The first character using positive indexing 
The last character using negative indexing
The third character using positive indexing
The second-to-last character using negative indexing
'''
word = "Programming"
a = word[0]
b = word[-1]
c = word[2]
d = word[-2]
print(a, b, c, d)

'''
Program 3: String Slicing (Half-Open Interval)
Question:
Given text = "HelloWorld", write a program that prints:
The first 5 characters (HellW)
Characters from index 5 to the end (World)
Characters from index 2 up to (but not including) index 7 (lloWo)
The entire string using slicing
The last 3 characters using negative slicing
'''
text = "HelloWorld"
a = text[0:6]
b = text[5:]
c = text[2:7]
d = text[:]
e = text[-3:]
print(a, b, c, d, e)

'''
Program 4: Immutability Demonstration
Question:
A student tries to change the first character of the string "Python" to "J" using indexing:
word = "Python"
word[0] = "J"
print(word)
Write the correct way to produce the output Jython.
'''
word = "Python"
a = "J" + word[1:]
print(a)

'''
Program 5: len() and Multi-Line Strings
Question:
Write a program that:
Stores the text "Learning Python" in a variable and prints its length using len().
Prints a multi-line string using the \n escape sequence.
Prints the same multi-line string using triple quotes instead.
'''
a = "Learning Python"
print(len(a))
print("Hii \n My Name is Karan")
print("""Hii
My Name is Karan""")
