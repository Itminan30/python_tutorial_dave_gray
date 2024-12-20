import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)

print("")
playerchoice = input("Enter...\n1 for Rock 🎱\n2 for Paper 📰 or\n3 for Scissors ✂\n\n")
player = float(playerchoice)
playerint = int(player)
choices = ["", "🎱", "📰", "✂"]

if player < 1 or player > 3 or player != playerint:
    sys.exit("You Must Enter 1, 2 or 3.")

computerChoice = random.choice("123")
computer = int(computerChoice)

# print("")
# print("You chose " + choices[playerint] + ".")
# print("Python chose " + choices[computer] + ".")
# print("")
print("")
print("You chose " + str(RPS(playerint)).replace("RPS.", "").title() + ".")
print("Python chose " + str(RPS(computer)).replace("RPS.", "").title() + ".")
print("")

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