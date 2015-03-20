#modifier
#Dennis Gordick
#3/20/2015

import monsterClassV2

def getMod(abbil):
        mod = 0
        if abbil == 1:
            mod = -5
        elif abbil <= 3:
            mod = -4
        elif abbil <= 5:
            mod = -3
        elif abbil <= 7:
            mod = -2
        elif abbil <= 9:
            mod = -1
        elif abbil <= 11:
            mod = 0
        elif abbil <= 13:
            mod = 1
        elif abbil <= 15:
            mod = 2
        elif abbil <= 17:
            mod = 3
        elif abbil <= 19:
            mod = 4
        elif abbil <= 21:
            mod = 5
        elif abbil <= 23:
            mod = 6
        elif abbil <= 25:
            mod = 7
        elif abbil <= 27:
            mod = 8
        elif abbil <= 29:
            mod = 9
        elif abbil <= 31:
            mod = 10
        elif abbil <= 33:
            mod = 11
        return mod


class Modifier(object):
    strength = 1
    dexterity = 1
    constitution = 1
    intelligence = 1
    wisdom = 1
    charisma = 1

    
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

        self.strMod = getMod(strength)
        self.dexMod = getMod(dexterity)
        self.conMod = getMod(constitution)
        self.intMod = getMod(intelligence)
        self.wisMod = getMod(wisdom)
        self.chaMod = getMod(charisma)



