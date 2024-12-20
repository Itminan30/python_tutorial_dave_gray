band = {
    "vocal": "Plant",
    "guitar": "Page"
}
band2 = dict(vocal="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

# Access Items in Dictionary
print(band["vocal"])
print(band.get("guitar"))

# Get All keys in Dictionary
print(band.keys())

# Get All Values in Dictionary
print(band.values())

# Get All Items in Dictionary
print(band.items())

# Check for a key in Dictionary
print("guitar" in band)
print("triangle" in band)

# Change Values in Dictionary
band["guitar"] = "Coverdale"
band.update({"bass": "JPJ"}) # Added a New key value with update method
print(band)

# Remove Items from Dictionary
print(band.pop("bass")) # Returns value

band["drums"] = "Boham"
print(band.popitem()) # Returns Tuple

# Clear and Delete in Dictionary
band["drums"] = "Boham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2
# print(band2) # Gives Error

# Copy Dictionary
print("Band Copy")
band3 = band
band3["drums"] = "Itminan"
print(band3)
print(band)

print("Good Copy")
band3 = band.copy()
band3["dumb"] = "Itminan"
print(band3)
print(band)

print("Good Copy")
band3 = dict(band)
band3["smart"] = "Itminan"
print(band3)
print(band)

# Nested Dictionary
member1 = {
    "name": "Itminan",
    "instrument": "Laptop"
}
member2 = {
    "name": "Fuad",
    "instrument": "Desktop"
}
interns = {
    "member1": member1,
    "member2": member2
}
print(interns)
print(interns["member1"]["name"])