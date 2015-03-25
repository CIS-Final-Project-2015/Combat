#dice
#DennisGordick
#3/25/2015

import random

class Dice(object):
    sides = 1
    roll = 1


    def __init__(self, sides):
        self.sides = 1
        self.roll = random.randint(1, sides)
    
