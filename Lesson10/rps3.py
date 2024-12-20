import sys
import random
from enum import Enum


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nEnter...\n1 for Rock 🎱\n2 for Paper 📰 or\n3 for Scissors ✂\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You Must Enter 1, 2 or 3.")
        play_rps()

    player = int(playerchoice)

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "").title() + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "").title() + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You Win! 🎉")
    elif player == 2 and computer == 1:
        print("🎉 You Win! 🎉")
    elif player == 3 and computer == 2:
        print("🎉 You Win! 🎉")
    elif player == computer:
        print("🎭 Tie Game! 🎭")
    else:
        print("🐍 Python Wins! 🐍")

    print("Play Again?\n")
    while True:
        playagain = input("\nWould you like to play again? (y/n)\n")
        if playagain not in ["y", "n"]:
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("🎉🎉🎉Thank you for playing!🎉🎉🎉")
        sys.exit("👋 Bye 👋")


play_rps()
