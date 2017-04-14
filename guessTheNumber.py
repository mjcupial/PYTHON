# PC, just guess the number!
#
# The gamer chosses the number in previously defined range.
# The PC must guess what is the number!
# by mj.c

import random
decision = 'y'

while (decision == 'y' or decision == 'Y'):
    print("Hi! I would like to guess your number! I would like to try...")
    print("but first please define the range as: from x to y")
    x = int(input("\nx: "))
    y = int(input("y: "))

    # check logic condition of range
    while (y <= x):
        print("WRONG! Give correct values!")
        x = int(input("\nx: "))
        y = int(input("y: "))

    PC_number = random.randint(x,y)
    tries=1
    the_number = int(input("\n### Gamer! Give the number: "))

    # check the_number value
    while (the_number > y or the_number < x):
        print("Wow! It doesn't make sense! Try again...")
        the_number = int(input("\n### Gamer! Give the number: "))

    # guess loop
    while PC_number != the_number:
        if PC_number > the_number:
            print("too high...")
            PC_number = random.randint(x,PC_number)
        else:
            print("too low...")
            PC_number = random.randint(PC_number,y)
        tries += 1

    print("You've got it! The unknow number is: ", the_number)
    print("To guess it, the PC needed only", tries, "probes!\n")

    decision=input("\n\nWould you like to try again? [y/n]: ")
input("\n\nPress ENTER to continue...")
