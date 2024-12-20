import math
# Data types

# Literal Assignment
# first = "Itminan"
# last = "Chowdhury"
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor Function
# pizza = str("Chicken")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
# fullname = first + " " + last
# print(fullname)

# Casting a number to string
# decade = str(1980)
# print(type(decade))
# print(decade)
# statement = "I like the music from the " + decade + "s."
# print(statement)

# Multiple Lines
# multiline = '''
# Hey, How are you??

#     I was just checking in..                All good??
#                     Are you allright???!!!
# '''
# print(multiline)

# Escaping Special Characters
# sentence = 'I\'m Itminan.\t I\'m an undergrad student.\n \nI study at BUP.'
# print(sentence)

# String Methods
# print(sentence)
# print(sentence.lower())
# print(sentence.upper())

# print(multiline.title())
# print(multiline.replace("good", "ok"))

# print(len(multiline))
# multiline += "                                   "
# multiline = "                  " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# Build a Menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cake".ljust(16, ".") + "$4".rjust(4))
print("=".center(20, "="))
print("")

# String Index Values
# print(title[1])
# print(title[-1]) # Returns the last letter
# print(title[0:3])
# print(title[0:])

# Some method return boolean data
# print(title.startswith("M"));
# print(title.endswith("M"));

# Boolean Data Type
# myvalue = True
# x = bool(True)
# print(type(myvalue))
# print(isinstance(x, bool));
# print(type(myvalue) == bool);

# Numaric Data Types
# Integer Type
# price = 100
# best_price = int(80)
# print(type(price))
# print(isinstance(best_price, int));
# print(type(price) == int);
# Float Type
gpa = 3.81
# y = float(3.99)
# print(type(gpa))
# print(isinstance(y, float));
# print(type(gpa) == float);
# Complex Type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Buildin functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(5))
print(math.ceil(gpa))
print(math.floor(gpa))

# Cast a string to number
zipcode = "10001"
zipcode = int(zipcode)
print(type(zipcode))