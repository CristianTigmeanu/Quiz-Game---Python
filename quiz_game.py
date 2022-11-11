print('Welcome to my quizz game! I hope you are going to have fun!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Pe cine iubeste cristi? ")
if answer.lower() == "cansu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("S-a suparat aseara pe el ca a stat sa scrie asta in loc sa se puna langa ea in pat? ")
if answer.lower() == "da":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("este cristi rau intentionat? ")
if answer.lower() == "nu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("face cristi asta pentru a realiza ceva cu viata lui? ")
if answer.lower() == "da":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct out of 5!")
