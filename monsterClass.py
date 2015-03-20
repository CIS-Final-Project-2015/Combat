import monsterClassV2
import modifier
import dice


goblin = monsterClassV2.goblin
gobMod = modifier.Modifier(goblin.strength, goblin.dexterity, goblin.constitution, goblin.intelligence, goblin.wisdom, goblin.charisma)


class Monster(object):
    health = 1
    name = " "
    initiative = 1
    damage = 1
    xp = 1

    def __init__(self, name, health, initiative, damage, xp):
        self.name = name
        self.health = health
        self.initiative = initiative
        self.damage = damage
        self.xp = xp


monster1 = Monster(goblin.name + " 1", goblin.hp, dice.Dice(6).roll + gobMod.dexMod, 2, goblin.xp)
monster2 = Monster(goblin.name + " 2", goblin.hp, dice.Dice(6).roll + gobMod.dexMod, 2, goblin.xp)
monster3 = Monster(goblin.name + " 3", goblin.hp, dice.Dice(6).roll + gobMod.dexMod, 2, goblin.xp)
monster4 = Monster(goblin.name + " 4", goblin.hp, dice.Dice(6).roll + gobMod.dexMod, 2, goblin.xp)

monsters= [monster1, monster2, monster3, monster4]

for i in monsters:
    print(i.xp)
