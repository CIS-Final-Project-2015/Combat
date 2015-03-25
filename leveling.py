#leveling
#Dennis Gordick
#3/19/2015

import levelInfo
import playerClass

class Leveling(object):

    lvlup = False
    players = playerClass.players
    lvlinfo = levelInfo.lvls
    xpNeeded = 0
    
    def setXp(player, lvlinfo):

        #Sets the base xp needed to lvl up based off the charachters lvl, using an outside document for the infomation
        
        for i in lvlinfo:
            if player.lvl == i.lvl:
                xpNeed = i.xpRequired
                return xpNeed


    def xpCheck(player, xpNeeded):

        #Checks to see if the player has enuf xp to lvl up, then does so.

        if player.xp >= xpNeeded:
            lvlup = True

        else:
            lvlup = False

        return lvlup
        
    for i in players:
        xpNeeded = setXp(i, lvlinfo)
        lvlup = xpCheck(i, xpNeeded)
Leveling()
