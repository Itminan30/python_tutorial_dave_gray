# Closure is a function having access to the scope of its parent functions after the parent function has returned.
def parent_function(person, coins):
    # coins = 3

    def play_games():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_games


tommy = parent_function("tommy", 3)
tommy()
tommy()
jenny = parent_function("jenny", 5)
jenny()
