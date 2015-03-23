




class Monster(object):
    health = 1
    name = " "
    initiative = 1
    damage = 1
    xp = 1

    def __init__(self, name, health, initiative, damage):
        self.name = name
        self.health = health
        self.initiative = initiative
        self.damage = damage


monster1 = Monster("goblin 1", 5, 1, 2)
monster2 = Monster("goblin 2", 5, 2, 2)
monster3 = Monster("goblin 3", 5, 3, 2)
monster4 = Monster("goblin 4", 5, 4, 2)

monsters= [monster1, monster2, monster3, monster4]

