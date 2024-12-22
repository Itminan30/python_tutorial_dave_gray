# Higher order function is a function that takes one or more functions as parameters or return a function as result
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = map(lambda x: x * x, numbers)
squared = list(squared)
print(squared)

odd_nums = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_nums)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = sum(numbers)
print(total)
total = reduce(lambda acc, curr: acc + curr, numbers, 0)
print(total)

factorial = reduce(lambda acc, curr: acc * curr, numbers, 1)
print(factorial)

names = ["Itminan", "Fuad", "Mafi", "Anik"]
char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(char_count)