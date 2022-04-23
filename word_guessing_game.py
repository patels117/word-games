"""
PURPOSE: Create Word Guessing Game in which the
User has to form the hidden word by guessing the letters in order.
Played via the Terminal.
"""

import sys
import random


MISTAKES_ALLOWED = 7

WORDS = [
    "spoon",
    "sofa",
    "couch",
    "table",
    "fridge",
    "fork",
    "pillow",
    "sink",
    "lamp",
    "stove",
    "plant",
    "bowl",
    "dish",
    "oven",
    "chair",
    "phone",
    "candle",
    "laptop",
]


def play_game() -> None:

    start_game = input("Do you want to start game? (Y/N):").lower()

    # user input handling
    while (start_game != "y") & (start_game != "n"):
        print("Need to type Y or N plz.")
        start_game = input(
            "Do you want to actually start game? I don't have all day (Y/N):"
        )

    if start_game == "n":
        print("Game ended by user.")
        sys.exit()

    while True:
        try:
            max_letters = int(input("Type preferred max number of letters:"))
            break
        except ValueError:
            print("Need to type a number plz")
            max_letters = int(input("Type preferred max number of letters:"))

    # adjust list to only have words of max length specified by user
    new_list = []
    for _ in WORDS:
        if len(_) <= max_letters:
            new_list.append(_)

    # get random word from adjusted list
    random_word = random.choice(new_list)
    print(
        f"The word you have to guess has {len(random_word)}"
        + " letters in it. Good Luck."
    )
    guess_formed = ""

    mistakes = MISTAKES_ALLOWED

    # tracks progress of guessing
    for _ in random_word:
        while mistakes != 0:
            guess_letter = input("Guess a letter:")
            if guess_letter == _:
                guess_formed += _
                print(f"Guessed correctly! Word formed so far: {guess_formed}")
                break

            mistakes -= 1
            dif = abs(ord(_) - ord(guess_letter))
            print(
                f"Guessed incorrectly! {mistakes} tries left."
                + f" Word formed so far: {guess_formed}"
            )
            print(
                f"Your guess was {dif} letters away in the"
                + f" alphabet from the correct letter."
            )

    if guess_formed == random_word:
        print("You won!")
    else:
        print("You lost :(")

    sys.exit()


if __name__ == "__main__":
    play_game()
