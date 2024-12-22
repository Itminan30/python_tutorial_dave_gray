# nums = [1, 2, 3]
# result = [num * num for num in nums] # List comprehension

squared = lambda x: x * x
print(squared(3))

add = lambda x, y: x + y
print(add(2, 3))

def function_builder(x):
    return lambda num : num + x

add_ten = function_builder(10)
add_twenty = function_builder(20)

print(add_ten(10))
print(add_twenty(20))