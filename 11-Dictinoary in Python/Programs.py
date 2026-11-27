'''
Program 1: Dictionary Creation & Unique Keys
Question:
Create a dictionary called student with the following key-value pairs:
"name" → "Naveen"
"age" → 21
"gpa" → 7.9
"name" → "Ravi" (intentionally duplicate the key)
Write a program that:
    Prints the dictionary 
    Prints the value of "name" using bracket notation
    Prints the type of the dictionary using type()
    Creates an empty dictionary empty_dict = {} and an empty set empty_set = set() — prints both and their types, with a comment explaining the difference
'''
student = {
    "name": "Naveen",
    "age": 21,
    "gpa": 7.9,
    "name": "Ravi"
}
print(student)
print(student["name"])
print(type(student))
empty_dict = {}
empty_set = set()
print(empty_dict)
print(type(empty_dict))
print(empty_set)
print(type(empty_set))

'''
Program 2: Safe Access with .get() vs. Bracket Notation
Question:
Create the dictionary phonebook = {"Naveen": "9876543210", "Ravi": "9123456789", "Kiran": "9000011111"}.
Write a program that:
Uses bracket notation to fetch "Ravi"'s number and prints it
Wraps a bracket-notation fetch of "Priya" in try/except to catch the KeyError and print a friendly message
Uses .get() to fetch "Priya" and prints the result (showing None)
Uses .get() with a custom default message for "Priya" and prints it
Uses .get() to fetch "Kiran" and prints the result
'''
phonebook = {
    "Naveen": "9876543210",
    "Ravi": "9123456789",
    "Kiran": "9000011111"
}
print(phonebook["Ravi"])
try:
    print(phonebook["Priya"])
except KeyError:
    print("Sorry, number is not available.")
print(phonebook.get("Priya"))
print(phonebook.get("Priyaa", "NUmber not found"))
print(phonebook.get("Kiran"))

'''
Program 3: Dynamic Dictionary Creation with zip()
Question:
Given:
keys = ["name", "age", "gpa", "subject"]
values = ["Naveen", 21, 7.9, "Computer Science"]
Write a program that:
Uses zip() and dict() to combine keys and values into a dictionary called student
Prints student
Creates another dictionary using set keys instead of list keys: set(keys) zipped with values
Prints the result and adds a comment explaining why the pairing may be unpredictable when keys come from a set
Converts the set-keys dictionary back to a list of its .items() and prints it
'''
keys = ["name", "age", "gpa", "subject"]
values = ["Naveen", 21, 7.9, "Computer Science"]
student = dict(zip(keys, values))
print(student)
set_keys_student = dict(zip(set(keys), values))
print(set_keys_student)
print(list(set_keys_student.items()))

'''
Program 4: Removing Items — pop() vs. del
Question:
Create the dictionary config = {"host": "localhost", "port": 8080, "debug": True, "timeout": 30}.
Write a program that:
Uses pop() to remove "debug" and prints the returned value
Prints the dictionary after the pop
Uses pop() with a default value to safely remove "ssl" (a key that doesn't exist) and prints the result
Uses del to remove "timeout" and prints the dictionary
Wraps a del config["ssl"] in try/except to catch the KeyError and prints a message
Prints the final dictionary
'''
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "timeout": 30
}
a = config.pop("debug")
print(a)
print(config)
b = config.pop("ssl", "Key not found")
print(b)
del config["timeout"]
print(config)
try:
    del config["ssl"]
except KeyError:
    print("Error: SSL key does not exist.")
print(config)

'''
Program 5: Nested Dictionaries & Combined Operations
Question:
Create the following nested dictionary:
languages = {
    "Python": "VS Code",
    "JavaScript": ["VS Code", "WebStorm"],
    "Java": {
        "IDE": "IntelliJ",
        "framework": "Spring"
    }
}
Write a program that:
Prints the value for "Python" (string value)
Prints the first IDE for "JavaScript" using list indexing
Prints the "IDE" value inside the nested "Java" dictionary using double indexing
Adds a new key "C++" with the value "CLion" and prints the updated dictionary
Uses .get() to safely check for "Rust" and prints the result
Uses pop() to remove "Python" and prints the returned value
Adds a comment summarizing all the dictionary concepts demonstrated in this program (creation, nesting, indexing, .get(), pop(), and unique keys)
'''
languages = {
    "Python": "VS Code",
    "JavaScript": ["VS Code", "WebStorm"],
    "Java": {
        "IDE": "IntelliJ",
        "framework": "Spring"
    }
}
print(languages["Python"])
print(languages['JavaScript'][0])
print(languages["Java"]["IDE"])
languages["C++"] = "CLion"
print(languages)
print(languages.get("Rust"))
a = languages.pop("Python")
print(a)
print(languages)
