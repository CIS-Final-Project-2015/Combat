#dice
#Dennis Gordick
#3/20/2015
import random

class Dice(object):
    sides = 1

    def __init__(self, sides):
        self.side = sides
        self.roll = (random.randint(1, sides))

die_1d4 = Dice(4)
die_1d6 = Dice(6)
die_1d8 = Dice(8)
die_1d10 = Dice(10)
die_2d10 = Dice(100)
die_1d12 = Dice(12)
die_1d20 = Dice(20)

dice = [die_1d4, die_1d6, die_1d8, die_1d10, die_2d10, die_1d12, die_1d20]

