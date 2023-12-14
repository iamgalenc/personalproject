print("Welcome to iamgalenc's quizz :)")

name = input("Enter your name: ")
print("Hello, " + name + "!")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Let's Go!")
score = 0

answer = input("What is GPU stand for?, ")
if answer.lower() == "graphical processing unit":
    print("Correct!" + name + "!")
    score += 1
else:
    print("Incorrect")

answer = input("What is ECC RAM? ")
if answer.lower() == "error correction code memory":
    print("Awesome!")
    score += 1
else:
    print("Incorrect")

answer = input("What is CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Good Job!")
    score += 1
else:
    print("Incorrect")

print("You got " + str(score) + "question correct! ," + name)
print("You got " + str((score / 3) * 100) + "%")