import random

rollDice = input('How many times do you want to roll?')
diceSides = input('How many sides is your dice?')
print('Your roll(s) is:')
# 2) ask for the number of rolls and dice sides

rollDice = int(rollDice)
diceSides = int(diceSides)
# 1) rolls and dice numbers are integers

for rolls in range (rollDice):
    randomDice = random.randrange(diceSides)+1
    print(randomDice)
    if randomDice == 20 and diceSides==20:
        print('Critical Hit')
    if  randomDice == 1 and diceSides==20:
        print('Critical Miss!')
# 4) roll the dice
# 5) output the results to the screen
# 6) check for critical hits and misses

aNumber = 15
if aNumber == 20:
    print ('My result is 20')
elif aNumber == 1:
    print ('My result is 1')
else:
    print ('')


#w3c for help
