
questions = ("Which of the followings is/are automatically added to every class, if we do not write our own.: ",
                       "What is the maximum length of a Python identifier?: ", 
                        "What will be the output of the following code snippet?  print(2**3 + (5 + 6)**(1 + 1)): ", 
                        "How is a code block indicated in Python?: ",
                        "What will be the output of the following code snippet?: ")

options = (("A.	Copy Constructor","B.Assignment Operator","c.A constructor without any parameter","D.All"),
                   ("A. 32", "B. 16", "C.182 ", "D. NONE"),
                   ("A. 12", "B. 8", "C. 18 ""D. none"),
                   ("A. brackets", "B. indentation", "C. key", "D. none"),
                   ("A. 15", "B. 0", "C. 2", "D. NONE"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("***********************")

print("       RESULTS        ")

print("***********************")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")