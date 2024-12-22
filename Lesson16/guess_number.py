########################################################################################################################
# {name}, guess which number I'm thinking of ... 1, 2 or 3.
# {name}, you chose {number}.
# I was thinking about number {number}
# 🎉 {name}, you win! 🎉 || 😔 Sorry, {name}. Better luck next time. 😔
# Game count: {number of total games}
# {name}'s wins: {number of wins by the player}
# Your winning percentage: {wining percentage}%
# Play again, {name}?
# Y for Yes or Q for Quit
# {name}, please enter 1, 2 or 3.
# 🎊🎊 Thank you for playing 🎊🎊
# 👋👋 Bye, {name} 👋👋
########################################################################################################################

import sys
from random import choice

def guess_number(name="Player"):
    game_count = 0
    player_wins = 0

    def guess_number_game():
        nonlocal game_count, player_wins, name

        player_choice = input(f"{name}, guess which number I\'m thinking of... 1, 2 or 3\n")
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please choose from 1, 2, or 3")
            guess_number_game()
        player = int(player_choice)
        computer = int(choice("123"))

        print(f"{name}, you chose {player}.")
        print(f"I was thinking about number {computer}")

        if player == computer:
            print(f"🎉 {name}, you win! 🎉")
            player_wins += 1
            game_count += 1
        else:
            print(f"😔 Sorry, {name}. Better luck next time. 😔")
            game_count += 1

        print(f"Game count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Your winning percentage: {(player_wins / game_count):.2%}")

        print(f"Play again, {name}?")
        while True:
            again_choice = input(f"Y for Yes or N for No\n")
            if again_choice not in ["y", "Y", 'n', 'N']:
                print(f"{name}, please choose from 'y' or 'n'")
                continue
            else:
                break
        if again_choice.lower() == "y":
            guess_number_game()
        else:
            if __name__ == "__main__":
                print(f"🎊🎊 Thank you for playing 🎊🎊")
                print(f"👋👋 Bye, {name} 👋👋")
                sys.exit()
            else:
                return

    return guess_number_game

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Game to guess which number Python is thinking of."
    )
    parser.add_argument("-n", "--name", metavar="name", default="Player", help="Name of the Player")
    args = parser.parse_args()


    guessing_game = guess_number(args.name)
    guessing_game()








