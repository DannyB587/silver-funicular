# Generate 6 random numbers from 1 to 69 for the first to the fifth
# and 1 to 26 for red Powerball

import random


def powerball():
    a = str(random.randint(1, 69))
    b = str(random.randint(1, 69))
    c = str(random.randint(1, 69))
    d = str(random.randint(1, 69))
    e = str(random.randint(1, 69))
    f = str(random.randint(1, 26))
    print("Your numbers are: " + a + ", " + b + ", " + c + ", " + d + ", " + e)
    print("The Powerball is: " + f)


def megamil():
    b = str(random.randint(1, 70))
    a = str(random.randint(1, 70))
    c = str(random.randint(1, 70))
    d = str(random.randint(1, 70))
    e = str(random.randint(1, 70))
    f = str(random.randint(1, 25))
    print("Your numbers are: " + a + ", " + b + ", " + c + ", " + d + ", " + e)
    print("The Mega Ball is: " + f)


print("Welcome to the lottery number generator!")
print("Please select a game!")
print("1. Powerball")
print("2. Mega Millions")
opt = input("Selection: ")

if opt == str("1"):
    powerball()
elif opt == str("2"):
    megamil()
else:
    print("Invalid Selection, please run again.")
