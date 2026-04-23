question = ("Who is India's Prime Minister",
            "Which is the largest country",
            "How many rings does Olympic Logo have",
            "Which is the largest ocean")
options = (("A. Narendra Modi","B. Rahul Gandhi"),
           ("A. Russia","B. USA"),
           ("A. Seven","B. Five"),
           ("A. Atlantic Ocean","B. Pacific Ocean"))
answers = ("A", "A", "B", "B")
ques_num = 0
score = 0
for ques in question:
    print("----------------------")
    print(ques)
    for option in options[ques_num]:
        print(option)
    guess = input("Enter your guess: ").upper()
    if guess == answers[ques_num]:
        print("The answer is correct!")
        score += 1
    else:
        print("The answer is incorrect!")
        print(f"{answers[ques_num]} is the correct answer!")
    ques_num += 1
print(f"Your score is {score*100/ques_num}%")
print("Congratulations!!")