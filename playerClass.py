import dice
import modifier
import testWeapon

#This is a test set of players. We tesrt to see if these players can go thrugh the combat system, and also get hit, deal damage, and get initiative.

#V 0.0.3 Update: We are useing the weapons from testWeapons.py, and they work perfectly so far. We need to get initiative like the mosnters, and we need to get moddifiers

class Player(object):
    health = 1
    name = " "
    initiative = 1
    armorClass = 1
    weapon = 1
    

    
    def __init__(self, name, health, initiative, armorClass, weapon):
        self.health = health
        self.name = name
        self.initiative = initiative
        self.armorClass = armorClass
        self.weapon = weapon

        self.damage = 1

        #This is all for damage and critical damage. It works fine now :)
        
        hit = dice.Dice(20).roll
        crit = weapon.critRange

        ifCrit = False
        if crit == hit:
            ifCrit = True

        if ifCrit == True:
            damage = weapon.damage + weapon.damage
            print(damage)
        elif ifCrit == False:
            damage = weapon.damage
            print(damage)

Dave = Player("Dave", 3, 8, 13, testWeapon.dagger)
Raulph = Player("Raulph", 22, 10, 15, testWeapon.sword)
Hannah = Player("Hannah", 10, 6, 19, testWeapon.bow)
Nick = Player("Nick", 2, 9, 11, testWeapon.staff)



players = [Dave, Raulph, Hannah, Nick]


