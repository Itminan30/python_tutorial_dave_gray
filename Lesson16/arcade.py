# 🤖 {name}, welcome to the Arcade 🤖
# Please, choose a game:
# 1 = Rock Paper Scissors
# 2 = Guess my number
# Or, press 'x' to exit the Arcade
# Play again, {name}?
# Press 'y' for Yes or 'q' to Quit
# 🎉🎊🎉 Thank you for playing 🎉🎊🎉
# {name}, Welcome back to arcade menu!!!
# Please, choose a game:
# 1 = Rock Paper Scissors
# 2 = Guess my number
# Or, press 'x' to exit the Arcade
# {name}, please enter 1, 2, or x
# See you next time!!!
# 👋👋👋 Bye {name} 👋👋👋

import sys
from rps import rps
from guess_number import guess_number

def arcade(name="playah"):
    welcome_back = False

    def play_arcade():
        nonlocal name, welcome_back

        if welcome_back:
            print("Welcome back, let's play again!")

        print(f"Please, choose a game:")
        print(f"1 = Rock Paper Scissors")
        print(f"2 = Guess my number")
        print(f"Or, press 'x' to exit the Arcade\n")

        while True:
            arcade_choice = input("")
            if arcade_choice not in ['1', '2', 'x']:
                print(f"{name}, please enter 1, 2, or x\n")
                continue
            else:
                break

        if arcade_choice == '1':
            play_rock_paper_scissors = rps(name)
            play_rock_paper_scissors()
        elif arcade_choice == '2':
            play_guess_number = guess_number(name)
            play_guess_number()
        else:
            print(f"See you next time!!!")
            sys.exit(f"👋👋👋 Bye {name} 👋👋👋")

        print(f"🎉🎊🎉 Thank you for playing 🎉🎊🎉")
        print(f"Play again, {name}?")
        print(f"Press 'y' for Yes or 'q' to Quit")

        while True:
            again_choice = input("")
            if again_choice not in ['y', 'Y', 'q', 'Q']:
                print(f"{name}, please enter 'y' or 'q'\n")
                continue
            else:
                break

        if again_choice == 'y':
            welcome_back = True
            play_arcade()
        else:
            print(f"See you next time!!!")
            sys.exit(f"👋👋👋 Bye {name} 👋👋👋")


    return play_arcade

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="A simple arcade game using Python"
    )
    parser.add_argument("-n", "--name", metavar="name", default="Player", help="The name of the player")
    args = parser.parse_args()

    arcade_game = arcade(args.name)
    print(f"🤖 {args.name}, welcome to the Arcade 🤖")
    arcade_game()











