class Monster(object):
    health = 1
    name = " "
    initiative = 1
    armorClass = 1

    def __init__(self, name, health, initiative, armorClass):
        self.name = name
        self.health = health
        self.initiative = initiative
        self.armorClass = armorClass


Goblin1 = Monster("Goblin 1", 10, 4, 5)
Goblin2 = Monster("Goblin 2", 10, 2, 5)
Goblin3 = Monster("Goblin 3", 10, 7, 5)
Goblin4 = Monster("Goblin 4", 10, 1, 5)

monsters= [Goblin1, Goblin2, Goblin3, Goblin4]
