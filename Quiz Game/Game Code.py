# Quiz game
# This here is the cod which holds the question fields that the user will be asked to answer.
questions = ("Where was the first example of paper money used?: ",
                       "What Apollo mission successfully put a man on the moon for the first time? : ",
                       "What is the largest US state (By landmass)? : ",
                       "Which app has the most total users? : ",
                       "How long did dinosaurs live on earth for? : ")
# These are the possiable answers to said questions. They have a Letter assigned to them. This is how we'll get the correct answer.

options = (("A. Greece", "B. Mexico", "C. China", "D. Turkey"),
                   ("A. Apollo 12", "B. Apollo 14", "C. Apollo 9", "D. Apollo 11"),
                   ("A. Alaska", "B. Texas", "C. California", "D. Florida"),
                   ("A. Instagram", "B. Snapchat", "C. Vine", "D. TikiTok"),
                   ("A. 100-150 million years", "B. 150-200 million years", "C. 200-300 million years", "D. 300+ million years"))

# this are the correct answers
answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

# This is a for loop. Which will display all the questions then it will display all of the options for said question
for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
# this is what will ask the user to input a answer to the question. 
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    # This is what wiol tell if the user is correct. If the guess is the name as the value in "answers" the user will gain a point
    if guess == answers[question_num]:
        score += 1
        print("That's Correct")
    else:
        print("That's Incorrct")
# if the guess is wrong this will show what the correct answer is
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

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