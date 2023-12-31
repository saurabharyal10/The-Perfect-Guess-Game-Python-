import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses +=1
    if(userGuess == randNumber):
        print("You guessed it right.")
    else:
        if(userGuess>randNumber):
            print("You guessed it wrong! Enter a smaller number")
        else:
           print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")

# open("The Perfect Guess Game/hiscore.txt", "w").close()

with open("The Perfect Guess Game/hiscore.txt", "r") as f:
    highScore = int(f.read())

if(guesses<highScore):
    print("You just broke the high Score!")
    with open("The Perfect Guess Game/hiscore.txt", "w") as f:
        f.write(str(guesses))
