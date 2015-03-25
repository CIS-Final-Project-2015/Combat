#Combat
#Dennis Gordick
#3/13/15

import operator
import random
import playerClass
import testEncounter

#We need to get the damage done to the entity and distribute it to the correct target.

class Combat(object):
    combatOrder = {
        }
    
    players = playerClass.players
    monsters = testEncounter.monsters
    inCombat = players + monsters
    outOfCombat = []
        
    def setCombatOrder(players, monsters):
        

        #Sorts out the players and the monsters in the list via initiative. Works like a charm
        

        #This is so we can appand things to here. Only is needed in this function, otherwise it is not in use.
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

        #This checks to see if the players and monsters have enuff health to fight. We are going to be implomenting if they are paralized or asleep (and things of that nature) soon

        #This list is supper important. Without it, the whole thing would not work DO NOT REMOVE!!!!!
        monName = []

        #This lets us append the names of the monsters to the list above. The reasoning behind that is so we can use the name in if statments
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

        #This avoids any confussion and lets us see if the attacker is a monster or a player. It is needed or else none of this will work. Please DO NOT REMOVE THE LISTS BELOW HERE!
        monName = []
        plaName = []


        
        #Useing the lists from above, this for statments put the names of players and monsters in the corosponding lists
        for i in monsters:
            monName.append(i.name)
        for i in players:
            plaName.append(i.name)


        #This is where we use the updated list to compare the attackers name to the lists. If the attackers name is in monsters, it randomly attacks, else the player gets to choose who to attack
        if attacker.name in plaName:
            print (monName)
            targetName = input("Who does " + attacker.name + " want to attack?")
            valid = False

            #This is so the player can not just skip his own turn by miss spelling the monsters name. It would go on forever if the player never types in a monster who they can attack
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

        #Simply gets the damage done and sets it as a variable
        
        damageDone = attacker.damage
        return damageDone
        

    def applyDamage(target, monsters, players, damage):
        #To calculate and distribute to the correct monster or player, the damage delt
        target.health = target.health - damage
        print(damage)        


    combatOrder = setCombatOrder(players,monsters)

    for i in inCombat:
        lifeStatus(i, combatOrder, outOfCombat, players, monsters, inCombat)

    for i in inCombat:
        target = targeting(i, players, monsters, inCombat)
        damageDone = calcDamage(i)
        applyDamage(target, monsters, players, damageDone)
    
Combat()
