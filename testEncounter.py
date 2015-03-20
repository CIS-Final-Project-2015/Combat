import monsterClassV2
import modifier
import dice


monster = monsterClassV2.goblin
monMod = modifier.Modifier(monster.strength, monster.dexterity, monster.constitution, monster.intelligence, monster.wisdom, monster.charisma)


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


monster1 = Monster(monster.name + " 1", monster.hp, dice.Dice(6).roll + monMod.dexMod, 2, monster.xp)
monster2 = Monster(monster.name + " 2", monster.hp, dice.Dice(6).roll + monMod.dexMod, 2, monster.xp)
monster3 = Monster(monster.name + " 3", monster.hp, dice.Dice(6).roll + monMod.dexMod, 2, monster.xp)
monster4 = Monster(monster.name + " 4", monster.hp, dice.Dice(6).roll + monMod.dexMod, 2, monster.xp)

monsters= [monster1, monster2, monster3, monster4]

for i in monsters:
    print(i.initiative)
