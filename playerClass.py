class Player(object):
    health = 1
    name = " "
    initiative = 1
    armorClass = 1
    
    def __init__(self, name, health, initiative, armorClass):
        self.health = health
        self.name = name
        self.initiative = initiative
        self.armorClass = armorClass



Dave = Player("Dave", 3, 8, 13)
Raulph = Player("Raulph", 22, 10, 15)
Hannah = Player("Hannah", 10, 6, 19)
Nick = Player("Nick", 0, 9, 11)



players = [Dave, Raulph, Hannah, Nick]

