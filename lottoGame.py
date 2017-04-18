# LOTTO game
#
# by mj.c

import random
decision = 'y'

print ("\tWelcome to LOTTO lottery!\n")
while (decision == 'y' or decision == 'Y'):
    counter = 1
    n = 0
    prize = 0

    # --- creating array of numbers and defining winning numbers
    numbers = list(range(1,50))
    print(numbers)
    random.shuffle(numbers)
    numbers = numbers[:6]
    print ("\nEnter 6 numbers between 1 and 49 and see if you win any cash!")

    # --- choice of gamer's numbers
    chosen_numbers = []
    print("")
    while counter <= 6:
        i = int(input("--$ "))
        while (i in chosen_numbers) or (i>49 or i<1):
            print("The number was chosen or not in range! Try again...")
            i = int(input("--$ "))
        chosen_numbers.append(i)
        counter += 1

    # --- comparison of gamer numbers with winning numbers (using counter)
    for i in chosen_numbers:
        if i in numbers:
            n += 1

    # --- the result displaying
    if n == 0 or n == 1 or n == 2:
        prize = 0
    elif n == 3:
        prize = random.uniform(23.32,258.25)
    elif n == 4:
        prize = random.uniform(782.95,2657.54)
    elif n == 5:
        prize = random.uniform(6152.24,46578.92)
    elif n == 6:
        prize = random.uniform(7000000,30000000)

    print ("\nYours numbers:\t\t", chosen_numbers)
    print("Winning numbers:\t",numbers)

    print("\nYou've guessed ",n," number(s)!\n\n\t\t\tYou won %.2f$!" % prize)
    decision = input("\nWanna try again? [y/n]: ")
    print("")
