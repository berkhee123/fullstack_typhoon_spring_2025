# random number buyu duriin utga 

import random

roll_dice = random.randint(1, 6)
print(roll_dice)

is_heads = random.choice([True, False])
print("You flipped heads: " + str(is_heads))

# 4 shirheg hoolnii tsugluulga list uusgeed tuuniigee randomoor
# xevlej xaruulna uu 


foods = ['tsuivan', 'buuz', 'huushuur']
is_food = random.choice(foods)
print('Your food is ' + is_food)