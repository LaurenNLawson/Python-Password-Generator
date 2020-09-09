# Random password generator
# LL 09/09/2020

import random

chars = '0123456789abcdefghijklmnopqrstuvwxyz!@£$%^&*()?ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generatePassword():
    for userPass in range(1):
        password = ''
        for c in range(8):
            password += random.choice(chars)
    print('Your random password is ' + password)


def userInput():
    userAnswer = input('Would you like to generate a random password Y/N?')
    if userAnswer.upper() == "Y":
        generatePassword()
    elif userAnswer.upper() == "N":
        print('Program now exiting')
        exit()
    else:
        print('Try again with an appropriate input')
        userInput()


def main():
    userInput()


if __name__ == "__main__":
    main()
