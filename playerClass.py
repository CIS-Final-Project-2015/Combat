class Player(object):
    health = 1
    name = " "
    initiative = 1
    armorClass = 1
    damage = 1
    xp = 1
    lvl = 1
    
    def __init__(self, name, health, initiative, armorClass, damage, xp, lvl):
        self.health = health
        self.name = name
        self.initiative = initiative
        self.armorClass = armorClass
        self.damage = damage
        self.xp = xp
        self.lvl = lvl

Dave = Player("Dave", 3, 8, 13, 8, 2004, 1)
Raulph = Player("Raulph", 22, 10, 15, 3, 1900, 1)
Hannah = Player("Hannah", 10, 6, 19, 5, 2015, 2)
Nick = Player("Nick", 0, 9, 11, 1, 500, 1)



players = [Dave, Raulph, Hannah, Nick]

