#testPlayers
#Dennis Gordick
#3/25/2015

#This is goint to be how player class gets all there information. YAY! We might be moving playerClass actualy into combat. But first, we need to test things
import testWeapon

class RandomPlayer(object):
    name = ""
    xp = 1
    melee = 1
    strength = 1
    dexterity = 1
    constitution = 1
    intelligence = 1
    wisdom = 1
    charisma = 1
    hp = 1

    def __init__(self, name, xp, melee, strength, dexterity, constitution, intelligence, wisdom, charisma, hp):
        self.name = name
        self.xp = xp
        self.melee = melee
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hp = hp

player_1 = RandomPlayer("Dave", 2003, testWeapon.dagger, 16, 15, 12, 13, 8, 10, 3)
player_2 = RandomPlayer("Raulph", 500, testWeapon.sword, 12, 12, 16, 11, 16, 12, 22)
player_3 = RandomPlayer("Hannah", 2001, testWeapon.bow, 13, 8, 14, 10, 17, 12, 10)
player_4 = RandomPlayer("Nick", 250, testWeapon.spear, 13, 17, 15, 15, 15, 17, 2)
