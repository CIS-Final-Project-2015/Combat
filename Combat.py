#Combat
#Dennis Gordick
#3/13/15

import operator
import random
import playerClass
import monsterClass

#We need to get the damage done to the entity and distribute it to the correct target.

class Combat(object):
    combatOrder = {
        }
    
    players = playerClass.players
    monsters = monsterClass.monsters
    inCombat = players + monsters
    outOfCombat = []

    def SetCombatOrder(players, monsters):

        inCombat = {
            }

        #Sort the players into a dict and with there corisponding initiative
        x = 0
        for i in players:
            inCombat[i.name] = i.initiative
            x += 1
        x = 0
        for i in monsters:
            inCombat[i.name] = i.initiative
            x += 1
        
        #This puts the charachters in order from greatest to least. The sortedCombat.reverse() puts the list from largest to smallest.
        sortedCombat = sorted(inCombat, key=inCombat.get)
        sortedCombat.reverse()

        print(sortedCombat)

        return sortedCombat

    def lifeStatus(player, combatOrder, outOfCombat , players, monsters, inCombat):

        monName = []
        
        for i in monsters:
            monName.append(i.name)
        
        if player.name in monName:
            if player.health <= 0:
                monsters.remove(player)
                inCombat.remove(player)
        else:
            if player.name in combatOrder:
                if player.health <= 0:
                    outOfCombat.append(player.name)
                    combatOrder.remove(player.name)
                    print (outOfCombat)
                    print (combatOrder)
        
                elif player.health > 0:
                    print (combatOrder)
            elif player.name in outOfCombat:
                if player.health > 0:
                    combatOrder.append(player.name)
                    outOfCombat.remove(player.name)
                    print(combatOrder)
                else:
                    print(outOfCombat)

    def ApplyDamage(Amount,Target):
        #To calculate and distribute to the correct monster or player, the damage delt
        print("Test")

    combatOrder = SetCombatOrder(players,monsters)

    for i in inCombat:
        lifeStatus(i, combatOrder, outOfCombat, players, monsters, inCombat)

Combat()
