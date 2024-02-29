import random

# Generating a random number for a dice

print("Welcome to the rolling the dice game! ")

print("The dice will roll until you get 6")

num = 0

# this will record the number of tries

tries = 0

# while loop will run until the number is 6

print("rolling.....")

while num != 6:
    tries = tries + 1

    num = random.randint(1, 6)

    print("You got ", num)

print("Congrats you got a 6 in", tries, "tries")
