import sys
import random
from enum import Enum

game_count = 0

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

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 You Win! 🎉"
        elif player == 2 and computer == 1:
            return "🎉 You Win! 🎉"
        elif player == 3 and computer == 2:
            return "🎉 You Win! 🎉"
        elif player == computer:
            return "🎭 Tie Game! 🎭"
        else:
            print("🐍 Python Wins! 🐍")
    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1
    print("Game Count: " + str(game_count))

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
