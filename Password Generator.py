import random
import time
import sys

print("Welcome!")
time.sleep(1)


def capture_password_length():
    passlen = int(input('Enter the length you wish your password to be: '))
    avail_char = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(avail_char, passlen))
    if passlen <= 18:
        time.sleep(.5)
        print(f"your password is: {password}")

    if passlen > 18:
        print("Error - character limit 18. Please try again. ")
        print(capture_password_length())

    else:
        print("Ok, thank you. Goodbye. ")
        sys.exit(0)


time.sleep(1)
repeat = input("Would you like another password? Yes/No ")
if repeat == "Yes" or "yes":
    print(capture_password_length())
else:
    print("Ok, thank you. Goodbye. ")
    sys.exit(0)
