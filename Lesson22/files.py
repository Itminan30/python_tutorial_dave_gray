import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - Error if it doesn't exist
f = open("names.txt", "r")
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names_list.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    f.close()

# Append - creates the file if it doesn't exist
try:
    f = open("names.txt", 'a')
    f.write("\nSirat")
    f.close()
    f = open("names.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    f.close()

# Write (Overwrites)
try:
    f = open("context.txt", "w")
    f.write("I have deleted all the context")
    f.close()
    f = open("context.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it doesn't exist
try:
    f = open("names_list.txt", "w")
except FileNotFoundError:
    print("File not found")
finally:
    f.close()

# Creates the specified file but returns an error if the file exists
if not os.path.exists("newfile.txt"):
    f = open("newfile.txt", "x")
    f.close()

# Delete a file

# Avoid Error if the file doesn't exist
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("newfile.txt not found")

# More Operations
with open("more_names.txt", "r") as f:
    content = f.read()
with open("names.txt", "w") as f:
    f.write(content)
with open("names.txt", "r") as f:
    print(f.read())
