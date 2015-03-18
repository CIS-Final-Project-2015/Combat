class Player(object):
    health = 1
    name = " "
    initiative = 1
    armorClass = 1
    damage = 1
    
    def __init__(self, name, health, initiative, armorClass, damage):
        self.health = health
        self.name = name
        self.initiative = initiative
        self.armorClass = armorClass
        self.damage = damage


Dave = Player("Dave", 3, 8, 13, 8)
Raulph = Player("Raulph", 22, 10, 15, 3)
Hannah = Player("Hannah", 10, 6, 19, 5)
Nick = Player("Nick", 0, 9, 11, 1)



players = [Dave, Raulph, Hannah, Nick]

