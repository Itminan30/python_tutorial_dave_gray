import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins, python_wins
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

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(playerparams, computerparams):
            nonlocal player_wins, python_wins
            if playerparams == 1 and computerparams == 3:
                player_wins += 1
                return "🎉 You Win! 🎉"
            elif playerparams == 2 and computerparams == 1:
                player_wins += 1
                return "🎉 You Win! 🎉"
            elif playerparams == 3 and computerparams == 2:
                player_wins += 1
                return "🎉 You Win! 🎉"
            elif playerparams == computerparams:
                return "🎭 Tie Game! 🎭"
            else:
                python_wins += 1
                print("🐍 Python Wins! 🐍")
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"Game Count: {str(game_count)}")
        print(f"Player Wins: {str(player_wins)}")
        print(f"Python Wins: {str(python_wins)}")

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


    return play_rps

game = rps()
game()