from random import randint

n = randint(1, 10)
userGuess = 0

while userGuess != n:
    userGuess = int(input("Guess a number: "))
    if userGuess < n:
        print("guess higher")

    elif userGuess > n:
        print("guess lower")

    else:
        print("Correct Guess")
