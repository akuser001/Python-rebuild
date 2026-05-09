#Game-Zone, a collection of mini-games for entertainment.
import Hangman
import Number_guess
import Tic_Tac_Toe as Tic
def main_menu():
    print("Welcome to Game-Zone!")
    print("1. Play Hangman")
    print("2. Number Guessing Game")
    print("3. tic-tac-toe")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice
def hang():
    Hangman.main()
def num_g():
    Number_guess.main()
def ttt():
    Tic.main()