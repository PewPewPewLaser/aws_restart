import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        

#psuedocode for the above:

#import the random module
#print the 'welcome' text
# generate a random number and set 'guess' var to false

#loop:
    #ask for a guess
    #if the user guesses right, then congratulate them, and set the guess var to true so the loop will end.
    #if the user guesses wrong then print a "nope wrong" text and continue looping.
    
    