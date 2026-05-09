import random
def main ():
    while True:
        low = 1
        high = 10
        level = input("Choose level (Easy/Medium/Hard): ")
        if level.lower() == "easy":
            high = 10
        elif level.lower() == "medium":
            high = 100
        elif level.lower() == "hard":
            high = 1000
        else:
            print("Invalid entry, auto set to easy")
        guesser = random.randint(low,high)
        bolean = True
        tries = 1
        while bolean == True:
            user_input = int(input(f"Guess a number between {low} to {high}: "))
            if guesser == user_input:
                print("CONGRATULATIONS! YOU WON!")
                print(f"You took {tries} attempts")
                bolean = False
            elif user_input < guesser:
                print("Too low... Aim a little higher")
                tries += 1
                bolean = True
            elif user_input > guesser:
                print("Too high... Aim a little lower")
                tries += 1
                bolean = True
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            print("Returning to main menu...")
            break