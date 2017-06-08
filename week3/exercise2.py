"""Week 3, Exercise 2.

An example of how a guessing game might be written.
"""
from __future__ import division
from __future__ import print_function
import random


def exampleGuessingGame():
    """Play a game with the user.

    This is an example guessing game. It'll test as an example too.
    """
    print("\nwelcome to the guessing game!")
    print("A number between 0 and _ ?")
    upperBound = raw_input("Enter an upper bound: ")
    print("OK then, a number between 0 and {} ?".format(upperBound))
    upperBound = int(upperBound)

    actualNumber = random.randint(0, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(raw_input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again ")
        else:
            print("Too big, try again   ")
    return "You got it!"


if __name__ == "__main__":
    exampleGuessingGame()
