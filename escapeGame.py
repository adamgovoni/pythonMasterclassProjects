import random

available_exits = ["north", "south", "east", "west"]

random_exit = random.choice(available_exits)

print(random_exit)

guessed_exit = ""

# intro, instructions
print("Hello there!  This is a text based escape game.")
print("Only one direction is correct and it has been chosen at random.")
print("Your choices are simple.  North, south, east, west, or quit.")
print("Good luck adventurer...")

while guessed_exit != random_exit:
    guessed_exit = input("Please choose a direction: ")
    if guessed_exit.casefold() == "quit":
        print("Game over")
        break

else:
    print("aren't you glad you got out of there")