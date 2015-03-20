# Combat

#Combat team repository


We have the combat order set and it send it out as the orderd list without the numbers.
We also have it pulling from an outside fource, witch lets us use any information sent from Entities.


The program can check to see if the player is able to fight or not, and weather a monster is alive or not.
If the monster is not alive it is removed from a list that we cheked.
We still need actual data from Entities and Encounters. Once we have that, we can check all of our code.

We have the damage done, and the target selected
We have it to where the players can select the target without problems
We need actual data so we can test evrything.

#Update 3/20/2015

We have made a test encounter, witch used to be know as monsterClass, and we changed it to where all the monsters data is in monsterClassV2

the dice.py is so you can get a random dice roll, and get the total. All you have to do to use it, is import it, then call it like so - dice.Dice(x).roll - x = the number of sides the die has, or the max number the roll can be

leveling.py just checks to see if a character can level up

modifier.py actualy checks the monster or characters ability scores, then puts out the correct modifier for it. To use it, summon it like this - modifier.Modifier(strength, dexterity, constitution, itelligence, wisdom, charisma).xMod -  x is the first 3 letters of the modifier you need... like Strength is str and Dexterity is dex

levelinfo.py sets the xp needed to lvl up based off the characters current lvl

we still need some actual data, but we created are own for testing purpeses. The most important thing is getting a test character to put thrue combat.
