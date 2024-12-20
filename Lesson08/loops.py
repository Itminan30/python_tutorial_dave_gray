# # While Loop
# value = 1
# while value < 10:
#     if value == 5:
#         break
#     print(value)
#     value += 1
# else:
#     print("done") # It will not print

# value = 0
# while value <= 10:
#     value = value + 1
#     if value == 5:
#         continue
#     print(value)
# else: # Else will not work if break is used
#     print("done")

# # For Loop
# names = ["Itminan", "Mafi", "Fuad", "Anik"]
# for name in names:
#     print(name)
#
# for al in "mississippi":
#     print(al)

# for x in range(3, 9):
#     print(x)

# for x in range(5, 101, 5):
#     print(x)
# else:
#     print('That\'s done!!!')

names = ["Itminan", "Sany", "Fuad"]
actions = ["codes", "cries", "sleeps"]
for name in names:
    for action in actions:
        print(name + " " + action + ".")