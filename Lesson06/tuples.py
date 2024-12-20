mytuple = tuple(("Itminan", 105, True))
anothertuple = (1, 3, 2, 9, 3, 4, 5, 3, 8)

print(mytuple)
print(type(mytuple))

newlist = list(mytuple)
newlist.append("BUP_CDI")
newtuple = tuple(newlist)
print(newtuple)

# Unpack a Tuple
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(3))  # Number of occurrences of 3 in the tuple
