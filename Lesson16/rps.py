import sys
from random import choice
from enum import Enum

def rps(name="Playah"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins, python_wins, game_count, name

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(f"\n{name}, please enter...\n1 for Rock 🎱\n2 for Paper 📰 or\n3 for Scissors ✂\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please Enter 1, 2 or 3.")
            play_rps()

        player = int(playerchoice)
        computer = int(choice("123"))

        print(f"You chose {str(RPS(player)).replace('RPS.', '').title()} and computer chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")

        def decide_winner(playerparams, computerparams):
            nonlocal player_wins, python_wins, name

            if playerparams == 2 and computerparams == 1:
                player_wins += 1
                return f"🎉 {name}, You Win! 🎉"
            elif playerparams == 3 and computerparams == 2:
                player_wins += 1
                return f"🎉 {name}, You Win! 🎉"
            elif playerparams == 1 and computerparams == 3:
                player_wins += 1
                return f"🎉 {name}, You Win! 🎉"
            elif playerparams == computerparams:
                return "🎭 Tie Game! 🎭"
            else:
                python_wins += 1
                return "🐍 Python Wins! 🐍"

        print(decide_winner(player, computer))

        game_count += 1
        print(f"Game Count: {game_count}")
        print(f"{name}\'s Wins: {player_wins}")
        print(f"Python's Wins: {python_wins}")

        print(f"Play Again?")
        while True:
            playagain = input(f"{name}, would you like to play again? (y/n)\n")
            if playagain not in ["y", "n", "Y", "N"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            if __name__ == "__main__":
                print(f"🎉🎉🎉Thank {name} for playing!🎉🎉🎉")
                sys.exit(f"👋 Bye {name} 👋")
            else:
                return

    return play_rps

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized gaming experience for Rock Paper Scissors."
    )
    parser.add_argument("-n", "--name", metavar="name", default="Player", help="The name of the player.")
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()