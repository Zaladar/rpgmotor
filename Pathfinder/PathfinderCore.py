#1 Standard library
from math import *
#2 Third party
#3 Local
from Pathfinder import CharTemplate, CharTemplate
from Pathfinder import Skills
from Core import CoreEngine

#needs a DB
classdict = {"Barbarian": False,
             "Bard": False,
             "Cleric": False,
             "Druid": False,
             "Fighter": False,
             "Monk": False,
             "Paladin": False,
             "Ranger": False,
             "Rogue": False,
             "Sorcerer": False,
             "Wizard": False}

csl = {
    "acrobatics": ["barbarian", "bard", "monk", "rogue"],
    "appraise": ["bard", "cleric", "rogue", "sorcerer"],
    "bluff": ["bard", "rogue", "sorcerer"],
    "climb": ["barbarian", "bard", "druid",
              "fighter", "monk", "ranger", "rogue"],
    "craft alch": ["barbarian", "bard", "cleric",
                   "druid", "fighter", "monk",
                   "paladin", "ranger", "rogue",
                   "sorcerer", "wizard"],
    "craft arm": ["barbarian", "bard", "cleric",
                  "druid", "fighter", "monk",
                  "paladin", "ranger", "rogue",
                  "sorcerer", "wizard"],
    "craft bows": ["barbarian", "bard", "cleric",
                   "druid", "fighter", "monk",
                   "paladin", "ranger", "rogue",
                   "sorcerer", "wizard"],
    "craft trap": ["barbarian", "bard", "cleric",
                   "druid", "fighter", "monk",
                   "paladin", "ranger", "rogue",
                   "sorcerer", "wizard"],
    "craft wep": ["barbarian", "bard", "cleric",
                  "druid", "fighter", "monk",
                  "paladin", "ranger", "rogue",
                  "sorcerer", "wizard"],
    "diplomacy": ["bard", "cleric", "paladin", "rogue"],
    "disable device": ["rogue"],
    "disguise": ["bard", "rogue"],
    "escape artist": ["bard", "monk", "rogue"],
    "fly": ["druid", "sorcerer", "wizard"],
    "handle animal": ["barbarian", "druid", "fighter",
                      "paladin", "ranger"],
    "heal": ["cleric", "druid", "paladin", "ranger"],
    "intimidate": ["barbarian", "bard", "fighter",
                   "monk", "ranger", "rogue", "sorcerer"],
    "knowledge arcana": ["bard", "cleric", "sorcerer", "wizard"],
    "knowledge dungeoneering": ["bard", "fighter", "ranger",
                                "rogue", "wizard"],
    "knowledge engineering": ["bard", "fighter", "wizard"],
    "knowledge geography": ["bard", "druid", "ranger", "wizard"],
    "knowledge history": ["bard", "cleric", "monk", "wizard"],
    "knowledge local": ["bard", "rogue", "wizard"],
    "knowledge nature": ["barbarian", "bard", "druid",
                         "ranger", "wizard"],
    "knowledge nobility": ["bard", "cleric", "paladin", "wizard"],
    "knowledge planes": ["bard", "cleric", "wizard"],
    "knowledge religion": ["bard", "cleric", "monk",
                           "paladin", "wizard"],
    "linguistics": ["bard", "cleric", "rogue", "wizard"],
    "perception": ["barbarian", "bard", "druid",
                   "monk", "ranger", "rogue"],
    "perform act": ["bard", "monk", "rogue"],
    "perform comedy": ["bard", "monk", "rogue"],
    "perform dance": ["bard", "monk", "rogue"],
    "perform keyboard": ["bard", "monk", "rogue"],
    "perform oratory": ["bard", "monk", "rogue"],
    "perform percussion": ["bard", "monk", "rogue"],
    "perform string": ["bard", "monk", "rogue"],
    "perform sing": ["bard", "monk", "rogue"],
    "perform wind": ["bard", "monk", "rogue"],
    "profession": ["bard", "cleric", "druid",
                   "fighter", "monk", "paladin",
                   "ranger", "rogue", "sorcerer",
                   "wizard"],
    "ride": ["barbarian", "druid", "fighter",
             "monk", "paladin", "ranger", "sorcerer"],
    "sense motive": ["bard", "cleric", "monk",
                     "paladin", "rogue"],
    "sleight of hand": ["bard", "rogue"],
    "spellcraft": ["bard", "cleric", "druid",
                   "paladin", "ranger", "sorcerer",
                   "wizard"],
    "stealth": ["bard", "monk", "ranger", "rogue"],
    "survival": ["barbarian", "druid", "fighter", "ranger"],
    "track": ["barbarian", "druid", "fighter", "ranger"],
    "swim": ["barbarian", "druid", "fighter",
             "monk", "ranger", "rogue"],
    "use magic device": ["bard", "rogue", "sorcerer"],
}

def char_setup(name):
    check = "yes"
    while check.lower() != "no":
        q = input("are you importing or creating a character? answer importing or creating")
        if q.lower() == "importing":
            print("not ready")
        elif q.lower() == "creating":
            CharTemplate.Character(name, class_setup(classdict.copy()), 1, skills_setup({}), stat_setup([], name), saves_setup({}, name), [])
            cd = input("a character can hold dices that are unique to them, such as class specific abilities or such."
                       " want to create any?")
            if cd.lower() == "yes":
                nerm = input("what doy ouy wnat to name them to?")
                side = input("how many sides?")
                CharTemplate.die.append(CoreEngine.Dice(nerm, side))
        else:
            print("invalid input")
        check = input("create more?")

def stat_setup(ls):
    i = 0
    qq = input("random or point buy?")
    if qq == "random":
        ls = {
            "STR": 0,
            "DEX": 0,
            "CON": 0,
            "INT": 0,
            "WIS": 0,
            "CHA": 0
        }
        tmp = []
        d = True
        while d:
            t = True
            del tmp[:]
            while t:
                modifi = []
                for x in range(0, 6):  # random generator producing 6 4d6 rolls
                    col = [d6.rolling(1), d6.rolling(1), d6.rolling(1), d6.rolling(1)]
                    col = sorted(col)  # sorting them and then printing the 3 highest results
                    col.reverse()
                    score = sum(col[0:3:])
                    tmp.append(score)
                    modif = floor((score - 10) / 2)
                    modifi.append(modif)
                    print(str(col[0:3:]) + "score:" + str(score) + ", modifier:" + str(modif))
                print("total bonus:" + str(sum(modifi)))
                tmp = sorted(tmp)
                tmp.reverse()
                qq = "n"
                while qq not in ["yes", "no"]:
                    qq = input("reroll? yes/no")
                    if qq == "yes":
                        print("rerolling")
                        t = False
                    elif qq == "no":
                        print("assigning stats")
                        t = False
                        d = False
        while i < 6:
            print(tmp)
            print(ls)
            assign = input("which stat has: " + str(tmp[i]) + "?")
            assign = assign.upper()
            if (assign in ls.keys()) and ls[assign] == 0:
                ls[assign] = tmp[i]
                tmp[i] = 0
                i += 1
            else:
                print("not an valid ability score!")

    elif qq == "point buy":
        p1 = input("what type of fantasy? low, std, high, epic or odd?")
        if p1 == "low":
            p1 = 10
        elif p1 == "std":
            p1 = 15
        elif p1 == "high":
            p1 = 20
        elif p1 == "epic":
            p1 = 25
        elif p1 == "odd":
            p1 = int(input("how many points can you buy?"))
        else:
            print("points set tup 10")
            p1 = 10
        ls = {
            "STR": 10,
            "DEX": 10,
            "CON": 10,
            "INT": 10,
            "WIS": 10,
            "CHA": 10
        }
        while True:
            print(ls)
            print("points left: " + str(p1))
            q1 = input("add or sub?")
            while q1 in ["add", "sub"]:
                q2 = input("what stat do you wish to " + q1 + " too?")
                if q2.upper() in ls.keys() and q1 == "add":
                    ls[q2.upper()] += 1
                    if ls[q2.upper()] == 11:
                        count = 1
                        p1 -= count
                        break
                    else:
                        count = ((ls[q2.upper()] - 10) // 2)
                        p1 -= count
                        break
                elif q2.upper() in ls.keys() and q1 == "sub":
                    ls[q2.upper()] -= 1
                    count = ((ls[q2.upper()] - 10) // 2)
                    if ls[q2.upper()] > 10:
                        p1 += count
                    else:
                        p1 -= count
                    break
            if p1 <= 0:
                done = input("are you done? yes/no")
                if done.lower() == "yes":
                    break
                else:
                    print("ok")
    print("")
    print("-----~~~~~=====~~~~~-----")
    print("ability scores are set!")
    print(ls)
    return ls

def class_setup(cls):
    print(classdict.keys())
    q = "yes"
    while q.lower() == "yes":
        cq = input("pick one of the classes from above")
        if cq.lower() in cls:
            cls[cq.lower()] = True
            print("added " + cq.lower() + " to classes!")
        else:
            print("not an available class")
        q = input("add more classes?")
    return cls

def skills_setup(skills, name):
    # Needs a DB
    skilldct = {
        "acrobatics": "DEX",
        "appraise": "INT",
        "bluff": "CHA",
        "climb": "STR",
        "craft alch": "INT",
        "craft arm": "INT",
        "craft bows": "INT",
        "craft trap": "INT",
        "craft wep": "INT",
        "diplomacy": "CHA",
        "disable device": "DEX",
        "disguise": "CHA",
        "escape artist": "DEX",
        "fly": "DEX",
        "handle animal": "CHA",
        "heal": "WIS",
        "intimidate": "CHA",
        "knowledge arcana": "INT",
        "knowledge dungeoneering": "INT",
        "knowledge engineering": "INT",
        "knowledge geography": "INT",
        "knowledge history": "INT",
        "knowledge local": "INT",
        "knowledge nature": "INT",
        "knowledge nobility": "INT",
        "knowledge planes": "INT",
        "knowledge religion": "INT",
        "linguistics": "INT",
        "perception": "WIS",
        "perform act": "CHA",
        "perform comedy": "CHA",
        "perform dance": "CHA",
        "perform keyboard": "CHA",
        "perform oratory": "CHA",
        "perform percussion": "CHA",
        "perform string": "CHA",
        "perform sing": "CHA",
        "perform wind": "CHA",
        "profession": "WIS",
        "ride": "DEX",
        "sense motive": "WIS",
        "sleight of hand": "DEX",
        "spellcraft": "INT",
        "stealth": "DEX",
        "survival": "WIS",
        "track": "WIS",
        "swim": "STR",
        "use magic device": "CHA",
    }
    for (x, y,) in skilldct.items():
        sfx = {
            "skn": x,
            "stat": int((name.stats[y] - 10) / 2),
            "rnk": 0,
            "mod": 0,
            "clss": name.cls in csl[x]
        }
        skills[sfx["skn"]] = Skills(**sfx)
    return skills

def saves_setup(saves, name):
    fort = input("enter the fort saves gained from classes, no bonuses")
    ref = input("enter the ref saves gained from classes, no bonuses")
    will = input("enter the will saves gained from classes, no bonuses")
    saves = {
        "fort": int(fort) + name.stats["CON"],
        "ref": int(ref) + name.stats["DEX"],
        "will": int(will) + name.stats["WIZ"]
    }
    return saves
