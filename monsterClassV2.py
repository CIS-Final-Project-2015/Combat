#monsterClassV2.0
#Dennis Gordick
#3/19/2015

import dice

class Monster(object):
    name = ""
    xp = 1
    ranged = 1
    melee = 1
    strength = 1
    dexterity = 1
    constitution = 1
    intelligence = 1
    wisdom = 1
    charisma = 1
    size = ""
    CMB = 1
    CMD = 1
    AC = 1
    fortitude = 1
    reflex = 1
    will = 1
    speed = 1
    hp = 1
    cr = 1

    def __init__(self, name, xp, ranged, melee, strength, dexterity, constitution, intelligence, wisdom, charisma, size, CMB, CMD, AC, fortitude, reflex, will, speed, hp, cr):
        self.name = name
        self.xp = xp
        self.ranged = ranged
        self.melee = melee
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.size = size
        self.CMB = CMB
        self.CMD = CMD
        self.AC = AC
        self.fortitude = fortitude
        self.reflex = reflex
        self.will = will
        self.speed = speed
        self.hp = hp
        self.cr = cr

dire_bat = Monster("Dire Bat", 600, "-", "Bite = 5 (1d8 + 4)", 17, 15, 13, 2, 14, 6, -1, 7, 19, 14, 5, 6, 3, 20, 22, 2)
doppelganger = Monster("Doppelganger" , 800, "-", "2 claws + 8 (1d8+4)", 18, 13, 12, 13, 14, 13, 0, 8, 20, 16, 4, 5, 6, 30, 26, 3)
ghoul = Monster("Ghoul", 400, "-", "bite + 3 (1d6 + 1 + disease, paralysis); 2 claws + 3 (1d6 + 1 + paralysis)", 13, 15, 0, 13, 14, 14, 0, 8, 20, 16, 4, 5, 6, 30, 26, 3)
giant_spider = Monster("Giant Spider", 400, "-", "bite + 2 (1d6 + poison)", 11, 17, 12, 0, 10, 2, 0, 2, 15, 14, 4, 4, 1, 30, 16, 1)
goblin = Monster("Goblin", 135, "short bow + 4 (1d4/x3)", "short sword + 2 (1d4/19-20)", 11, 15, 12, 10, 9, 6, 1, 0, 12, 16, 3, 2, -1, 30, 6, 1/3)
lizard = Monster("Lizard", 65, "-", "bite + 4 (1d4 - 4)", 3, 15, 8, 1, 12, 2, 2, 0, 6, 14, 1, 4, 1, 20, 3, 1/6)
orc = Monster("Orc", 135, "javelin + 1 (1d4/x3)", "falchion + 5 (2d4 + 4/18 - 20)", 17, 11, 12, 7, 8, 6, 0, 4, 14, 13, 3, 0, -1, 30, 6, 1/3)
oread = Monster("Oread", 200, "longbow + 4 (1d8 + 2/ x3)", "longsword +3 (1d8 +3/19-20)", 15, 15, 14, 8, 14, 8, 0, 3, 15, 14, 4, 2, 4, 20, 12, 1/2)
rat = Monster("Rat", 100, "-", "bite + 4 (1d3 - 4)", 2, 15, 11, 2, 13, 2, 2, 0, 6, 14, 2, 4, 1, 15, 4, 1/4)
wolf = Monster("Wolf", 400, "-", "bite + 2 (1d6 + 1 + trip)", 13, 15, 15, 2, 12, 6, 0, 2, 14, 14, 5, 5, 1, 50, 13, 1)
young_mist_dragon = Monster("Young Mist Dragon", 3200, "-", "bite + 14(2d6 + 7); 2 claws + 14(1d8 + 5); 2 wings + 12(1d6 + 2); tail slap + 12(1d8 + 7)", 21, 12, 17, 16, 17, 16, -1, 16, 27, 21, 10, 8, 10, 40, 95, 7)
asrai = Monster("Asrai", 1600, "-", "touch + 7(1d4 cold)", 5, 18, 13, 10, 13, 14, 2, 3, 10, 18, 1, 7, 4, 20, 9, 5)
phoenix = Monster("Phoenix", 51200, "-", "2 talons + 24(2d6 + 8/ 19 - 20 + 1d6 fire); bite + 24(2d8 + 8 + 1d6 fire)", 27, 25, 20, 23, 22, 22, -4, 32, 50, 28, 17, 19, 14, 30, 210, 15)
greater_shedu = Monster("Greater Shedu", 9600, "-", "2 hooves + 20(1d6 + 7)", 24, 12, 20, 18, 18, 20, -1, 22, 33, 18, 14, 10, 10, 40, 147, 10)
witchfire = Monster("Witchfire", 6400, "witchfire bolt + 13(8d6 fire + witchfire)", "incorporeal touch + 13(8d6 fire + witchfire)", 0, 22, 0, 17, 16, 25, 0, 13, 31, 24, 10, 11, 10, 50, 115, 9)
satyr = Monster("Satyr", 1200, "short bow + 6(1d6/x3)", "dagger + 6 (1d4 + 2/19 - 20); horns + 1 (1d6 + 1)", 14, 15, 15, 12, 14, 19, 0, 6, 18, 18, 4, 8, 8, 40, 44, 4)
dire_tiger = Monster("Dire Tiger", 4800, "-", "2 claws + 18(2d4 + 8 + grab); bite + 18(2d6 + 8/19 - 20 + grab)", 27, 15, 17, 2, 12, 10, -1, 19, 31, 17, 12, 11, 5, 40, 105, 8)
tentamort = Monster("Tentamort", 1200, "-", "string + 6(1d6 + 2 + poison); tentacle + 2(1d6 + 1 + grab)", 15, 13, 14, 1, 14, 6, 0, 6, 17, 17, 4, 5, 7, 20, 39, 4)
spine_dragon = Monster("Spine Dragon", 76800, "4 spines + 14(2d8 + 11)", "bite + 23(2d8 + 11); claws + 23(2d6 + 11); tail slap + 18(2d8 + 16)", 32, 15, 29, 16, 22, 19, -4, 31, 44, 31, 19, 12, 16, 30, 248, 16)
warcat = Monster("Warcat", 25600, "-", "bite + 22(2d6 + 12 + grab); 2 claw + 22(1d8 + 12/19 - 20 + rend)", 35, 18, 24, 2, 11, 5, -2, 26, 40, 28, 17, 14, 7, 50, 184, 13)
giant_fire = Monster("Giant Fire", 9600, "rock + 10(1d8 + 15 + 1d6 fire)", "greatsword + 21/+16/+11(3d6 + 15) OR 2 slams + 20(1d8 + 10)", 31, 9, 21, 10, 14, 10, -1, 22, 31, 24, 14, 4, 9, 40, 142, 10)
dragonkin = Monster("Dragonkin", 6400, "-", "mwk glaive + 16/+11(2d8 + 9/x3); bite + 16(1d8  =6) OR bite + 16(1d8 + 6); 2 claws + 15(1d6 + 6)", 22, 15, 20, 11, 12, 17, -1, 17, 29, 23, 12, 9, 8, 40, 115, 9)
t_rex = Monster("T-Rex", 6400, "-", "bite + 20(4d6 + 22/19 - 20 + grab)", 32, 13, 19, 2, 15, 10, -4, 28, 39, 21, 15, 12, 10, 40, 153, 9)
blodeuwedd = Monster("Blodeuwedd", 2400, "mwk sling + 11(1d4 + 6)", "2 claws + 10(1d8 + 6)", 18, 21, 21, 14, 17, 18, 0, 7, 23, 20, 7, 10, 8, 30, 66, 6)
nogitsune = Monster("Nogitsune", 3200, "mwk dart + 15/+10(1d4 + 4 + poison)", "bite  +14(1d6 + 4); 2 claws + 14(1d4 + 2 + poison)", 18, 25, 22, 17, 16, 19, 0, 11, 29, 21, 8, 12, 8, 50, 80, 7)
darakhul_ogre = Monster("Darakhul Ogre", 1600, "javelin + 3(1d8 + 8)", "bite +10 (2d6+8 + paralysis + disease); 2 claws +10 (1d6+4 + paralysis) OR greatclub +10 (2d8+12); bite +8 (1d10+8 + paralysis + disease)", 27, 12, 0, 10, 14, 13, -1, 12, 23, 23, 5, 2, 5, 30, 22, 5)

monsters = [dire_bat, doppelganger, ghoul, giant_spider, goblin, lizard, orc, oread, rat, wolf, young_mist_dragon, asrai, phoenix, greater_shedu, witchfire, satyr, dire_tiger, tentamort, spine_dragon, warcat, giant_fire, dragonkin, t_rex, blodeuwedd, nogitsune, darakhul_ogre]
