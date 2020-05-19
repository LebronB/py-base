from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


# 9-14
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        rand_side = randint(1, self.sides)
        print("You have " + str(rand_side) + " points.")


die_six_sides = Die()
for i in range(10):
    die_six_sides.roll_die()

die_ten_sides = Die(10)
for i in range(10):
    die_ten_sides.roll_die()

die_twenty_sides = Die(20)
for i in range(10):
    die_twenty_sides.roll_die()


