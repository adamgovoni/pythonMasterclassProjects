import random

# list of possible exits
available_exits = ["north", "south", "east", "west"]

# one of the exits is chosen at random and saved here
random_exit = random.choice(available_exits)

# variable starts as am empty string to initiate the while loop
guessed_exit = ""

# intro, instructions
print("Hello there!  This is a text based escape game.")
print("Only one direction is correct and it has been chosen at random.")
print("Your choices are simple.  North, south, east, west, or quit.")
print("Good luck adventurer...")

#while loop continues until correct answer received or player enters quit
while guessed_exit.casefold() != random_exit:
    guessed_exit = input("Please choose a direction: ")
    if guessed_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("Congratulations you've escaped! Aren't you glad you got out of there?")

# need to add a counter for tracking incorrect guesses
# add random death/game over endings for too many wrong guesses
