#Game-Zone
import Hangman
def main_menu():
    print("Welcome to Game-Zone!")
    print("1. Play Hangman")
    print("2. Number Guessing Game")
    print("3. tic-tac-toe")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice
def hangman():
    Hangman.main()