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

    def setCombatOrder(players, monsters):

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
            elif player.name in outOfCombat:
                if player.health > 0:
                    combatOrder.append(player.name)
                    outOfCombat.remove(player.name)

    def targeting(attacker, players, monsters, inCombat):
        #To tell the monsters who to attack.
        monName = []
        plaName = []
        for i in monsters:
            monName.append(i.name)

        for i in players:
            plaName.append(i.name)
            
        if attacker.name in plaName:
            print (monName)
            targetName = input("Who does " + attacker.name + " want to attack?")
            valid = False
            while valid == False:
                time = 0
                for i in monsters:
                    if i.name == targetName:
                        target = i
                        valid = True
                    else:
                        time +=1
                if time == 4:
                    print("You spelled the name wrong, try again")
                    targetName = input("Who does " + attacker.name + " want to attack?")
                    time = 0
                
            print(target.name)
        elif attacker.name in monName:
            target = random.randrange(0, len(players))
            target = players[target]
            print(target.name)
        return target

    def calcDamage(attacker):
        damageDone = attacker.damage
        return damageDone
        

    def applyDamage(target, monsters, players, damage):
        #To calculate and distribute to the correct monster or player, the damage delt
        target.health = target.health - damage
        print(target.health)
        


    combatOrder = setCombatOrder(players,monsters)

    for i in inCombat:
        lifeStatus(i, combatOrder, outOfCombat, players, monsters, inCombat)

    for i in inCombat:
        target = targeting(i, players, monsters, inCombat)
        damageDone = calcDamage(i)
        applyDamage(target, monsters, players, damageDone)
    
Combat()
