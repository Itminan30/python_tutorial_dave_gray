nums = {1,2,3,4,5,6,7,8,9,10}
nums2 = set((19,42,32,12,5,6,7,8,9,10))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# 1 is Duplicate of True and 0 is Duplicate of False
nums3 = {1, True, 2, 0, 3, 4, False}
nums4 = {True, 1, False, 3, 4, 0}
print(nums3)
print(nums4)

# Check the existence of value in set
print(True in nums3)

# Can't refer to an element with index position or key

# Add element to set
nums.add(12)
print(nums)

# Add element from one set to another || update method can also take lists, tuples and dictionaries as well
monuments = {69, 400}
nums.update(monuments)
print(nums)

# Merge two sets
one = {3, 2, 1}
two = {3, 4, 5}
newset = one.union(two)
print(newset)

# Keep only the duplicates in set
duplicateset = one.intersection(two)
print(duplicateset)

# Keep everything except the duplicate
noduplicateset = one.symmetric_difference(two)
print(noduplicateset)
