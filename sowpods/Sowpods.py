"""
Hangman
https://www.practicepython.org/exercise/2017/01/10/32-hangman.html

"""

import random as ran

def get_word():
    file = "sowpods.txt"
    words = []
    with open(file,"r") as f:
        words = f.readlines()

    return ran.choice(words).strip()


def show(word,guess,inp):
    new_guess = ""
    for i in range(len(word)):
        if guess[i] != "-":
            new_guess += guess[i]
        elif word[i] == inp:
            new_guess += inp
        else:
            new_guess += "-"
    print(" ".join(new_guess))
    return new_guess


def play(word):
    chances = 6
    guess = "-"*len(word)
    while word != guess and chances:
        print(f"choices left: {chances}")
        inp = str(input("Make a new guess:")).strip()
        if inp in word and inp not in guess:
            guess = show(word,guess,inp)
        elif inp in guess :
            print("already guessed !!")
        else:
            print("Incorrect !!")
            chances -= 1
    return guess


if __name__ == "__main__":
    print("Welcome to Hangman!!")
    inp = input("Enter 's/e' to start/end:").strip()
    while inp == "s":
        word = get_word().lower()
        print(word)
        res = play(word)
        if res == word:
            print("Hurrrah, you won :)")
        else:
            print("Better luck next time.")
        inp = input("Enter 's/e' to start/end:").strip()
    print("Game Over")