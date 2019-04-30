import random
import sys

min = 1
max = int(input("How many sides of your dice? "))
accepted = ['yes', 'y', 'Yes', 'Y']


def roll_dice():
    print("Rolling the dice... ")
    print("The values are... ")
    print(random.randint(min, max))
    print(random.randint(min, max))

    roll_more = input("Roll the dice again? ")
    if roll_more in accepted:
        roll_dice()
    else:
        print('OK, thanks for playing!')
        sys.exit(0)


roll_dice()
