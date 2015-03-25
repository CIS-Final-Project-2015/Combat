#testWeapon.py
#Dennis Gordick
#3/25/2015

import dice


#This file is so we can givce the player a weapon and getr the damage corosponding with it


#V 0.0.1 Update: All weapons are equal but seem to work. In next update we are going to give the weapons there actual values with damage and stuff



class Weapon(object):
    damage = 1
    critRange = 1
    name = ""

    def __init__(self, name, damage, critRange):
        self.name = name
        self.damage = damage
        self.critRange = critRange

#Test weapons :)

dagger = Weapon("Dagger", dice.Dice(6).roll, 20)
sword = Weapon("Sword", dice.Dice(6).roll, 20)
bow = Weapon("Bow", dice.Dice(6).roll, 20)
staff = Weapon("Staff", dice.Dice(6).roll, 20)
