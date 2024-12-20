name = "Cipher"
coins = 5

normaltext = "\n" + name + " has " + str(coins) + " coins."
print(normaltext)

fstringtext = "\n%s has %s coins." % (name, coins)
print(fstringtext)

formattext = "\n{} has {} coins.".format(name, coins)
print(formattext)

formatText = "\n{1} has {0} coins.".format(coins, name)
print(formatText)

formatText = "\n{name} has {coin} coins.".format(coin=coins, name=name)
print(formatText)

person = {'name': "Itminan", 'coins': 69}
print("\n{name} has {coins} coins.".format(**person))

# fstring starts here
message = f"\n{name} has {coins} coins."
print(message)

message = f"\n{name} has {2 * 4} coins."
print(message)

message = f"\n{name.lower()} has {coins} coins."
print(message)

message = f"\n{person['name']} has {person['coins']} coins."
print(message)

# Passing formatting options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

for num in range(1, 6):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 6):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}")
