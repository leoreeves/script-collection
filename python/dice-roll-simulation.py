import random

def dice_roll():
    return "You roll a " + str(random.randint(1,6)) # Amend end integer to increase the size of the dice rolled

print(dice_roll())

while True:
    roll_again = input("Roll again? [y/n] ").lower()
    if roll_again == 'y':
        print(dice_roll())
        continue
    elif roll_again == 'n':
        break
