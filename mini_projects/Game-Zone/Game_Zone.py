#Game-Zone, a collection of mini-games for entertainment.
import Hangman
import Number_guess
import Tic_Tac_Toe as Tic
def main_menu():
    print("Welcome to Game-Zone!")
    print("Which game would you like to play?")
    print("1. Hangman")
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
def main():
    while True:
        choice = main_menu()
        if choice == "1":
            hang()
        elif choice == "2":
            num_g()
        elif choice == "3":
            ttt()
        elif choice == "4":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()