import random

words_set = ["cat", "dog", "fish", "cow", "bat", "rat", "ant", "bee", "pig", "hen", "zebra", "horse", "sheep", "snake", "goose", "camel", "panda", "tiger", "monkey", "rabbit", "alligator", "crocodile", "kangaroo", "dolphin", "elephant", "giraffe", "hippopotamus", "chameleon", "rhinoceros", "porcupine", "armadillo", "orangutan", "platypus", "axolotl", "komodo", "mongoose", "tarantula", "wolverine", "hedgehog", "jellyfish"]

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\")}

def display_man(wrong_guesses):
    print("**************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words_set)
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True
    total_guess = 0
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input!")
            continue
        
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if guess == answer[i]:
                    hint[i] = guess
        
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        total_guess += 1
        
        if wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lost!")
            is_running = False
                   
        elif "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"You took {total_guess} tries","\nCongratulations!!","\nYou Win!")
            is_running = False
        
if __name__ == "__main__":
    main()
