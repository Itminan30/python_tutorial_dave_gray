def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    return add_one(total)

answer = add_one(0)
print(answer)
