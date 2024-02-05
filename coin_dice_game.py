import random

cointoss = ("Heads", "Tails")
coin_result = random.choice(cointoss)

print("Coin result:", coin_result)

if coin_result == "Heads":
    min_value = 1
    max_value = 6
    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("\nRolling the dice...")
        print("\nThe values are....")
        value1 = random.randint(min_value, max_value)
        value2 = random.randint(min_value, max_value)
        print(value1, value2)
        if value1==value2:
            print("\nCONGRATULATIONS!Your luck has just maxed out!")
        roll_again = input("\nPress 'y' or 'yes' to roll the dice again.\n\nPress 'n' or 'no' to quit the game.")
    times = 1
    while roll_again == "no" or roll_again == "n":
        while times==1:
            print("\nYou have quit the game. Thank you for playing!")
            times+=1

else:
    print("\nNo dice roll as the coin landed on Tails.")

