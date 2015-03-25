import dice
import modifier
import testWeapon
import testPlayers

#This is a test set of players. We tesrt to see if these players can go thrugh the combat system, and also get hit, deal damage, and get initiative.

#V 0.0.3 Update: We are useing the weapons from testWeapons.py, and they work perfectly so far. We need to get initiative like the mosnters, and we need to get moddifiers

class Player(object):
    health = 1
    name = " "
    initiative = 1
    weapon = 1
    

    
    def __init__(self, name, health, initiative, weapon):
        self.health = health
        self.name = name
        self.initiative = initiative
        self.weapon = weapon


        #This is all for damage and critical damage. It works fine now :)
        
        hit = dice.Dice(20).roll
        crit = weapon.critRange

        ifCrit = False

        if crit <= hit:
            ifCrit = True

        if ifCrit == True:
            damage = weapon.damage + weapon.damage
        elif ifCrit == False:
            damage = weapon.damage
        self.damage = damage

character_1 = Player(testPlayers.player_1.name, testPlayers.player_1.hp, 8, testPlayers.player_1.melee)
character_2= Player(testPlayers.player_2.name, testPlayers.player_2.hp, 10, testPlayers.player_2.melee)
character_3 = Player(testPlayers.player_3.name, testPlayers.player_3.hp, 6, testPlayers.player_3.melee)
character_4 = Player(testPlayers.player_4.name, testPlayers.player_4.hp, 9, testPlayers.player_4.melee)



players = [character_1, character_2, character_3, character_4]

