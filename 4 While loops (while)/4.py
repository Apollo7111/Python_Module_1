import random
numberToGuess = random.randint(1,10)
guess = int(input("Take a guess! "))
while (guess != numberToGuess):
    print('You guessed wrong! Try again!')
    if(guess > numberToGuess):
        print('Tip: Too High')
    if (guess < numberToGuess):
         print('Tip: Too Low')
    guess = int(input("Take a guess! "))
if(guess == numberToGuess):
        print("Correct!")