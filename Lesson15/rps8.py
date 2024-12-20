import sys
import random
from enum import Enum

def rps(name="Player"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins, python_wins, name
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f"\n{name}, please enter...\n1 for Rock 🎱\n2 for Paper 📰 or\n3 for Scissors ✂\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please Enter 1, 2 or 3.")
            play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(playerparams, computerparams):
            nonlocal player_wins, python_wins, name
            if playerparams == 1 and computerparams == 3:
                player_wins += 1
                return f"🎉 {name}, You Win! 🎉"
            elif playerparams == 2 and computerparams == 1:
                player_wins += 1
                return f"🎉 {name}, You Win! 🎉"
            elif playerparams == 3 and computerparams == 2:
                player_wins += 1
                return f"🎉 {name}, You Win! 🎉"
            elif playerparams == computerparams:
                return "🎭 Tie Game! 🎭"
            else:
                python_wins += 1
                return "🐍 Python Wins! 🐍"
        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"Game Count: {game_count}")
        print(f"{name}\'s Wins: {player_wins}")
        print(f"Python's Wins: {python_wins}")

        print("Play Again?\n")
        while True:
            playagain = input(f"{name}, would you like to play again? (y/n)\n")
            if playagain not in ["y", "n"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print(f"🎉🎉🎉Thank {name} for playing!🎉🎉🎉")
            sys.exit(f"👋 Bye {name} 👋")


    return play_rps

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized gaming experience."
    )

    parser.add_argument("-n", "--name", metavar="name", help="Name of the person playing the game.")

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()