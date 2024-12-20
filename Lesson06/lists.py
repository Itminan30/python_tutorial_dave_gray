users = ["Itminan", "Mafi", "Fuad", "Anik"]
data = ["Itminan", 105, True]

print("Itminan" in users)  # Find Element in List
print(users.index("Itminan"))  # Find Index of a Specific Element
print(users[0])  # First Element in List
print(users[-1])  # Last Element in List
print(users[1:])
print(users[1:-1])

print(len(users))  # Find the total number of Items in a List

# Add Items to List
users.append("Elaf")
print(users)

users += ["Sirat"]
print(users)

users.extend(["Hamid", "Ariyan"])
print(users)

# users.extend(data)
# print(users)

# users.append(data)
# print(users)

users.insert(1, "Hasan")
print(users)

users[3:3] = ["Sany", "Mridula"]
print(users)

# Splice in the List
users[3:5] = ["Rabeya", "Maliha"]
print(users)

# Remove Items from the List
users.remove("Rabeya")
print(users)

print(users.pop())
print(users)

del users[1]
print(users)

data.clear()
print(data)

# Sorting methods in List
users += ["jamil"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 48, 1, 6]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

# Copy List
numscopy = nums.copy()
mynums = list(nums)
ournums = nums[:]

print(type(numscopy))


