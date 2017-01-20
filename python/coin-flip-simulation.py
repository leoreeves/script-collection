import random

heads_count = 0
tails_count = 0

flips = int(input("How many times would you like to flip the coin?: "))

for x in range(flips):
    x = random.randint(0,1)
    if x == 0:
        #print('Heads') # Uncomment to print all Heads thrown
        heads_count += 1
    elif x == 1:
        #print('Tails') # Uncomment to print all Tails thrown
        tails_count += 1

print(str(heads_count) + ' Heads')
print(str(tails_count) + ' Tails')
