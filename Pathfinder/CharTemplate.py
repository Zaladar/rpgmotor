#1 standard livraries
#2 Third party
#3 Local
from Core import CoreEngine
#this is a generic template usable by both Characters and monsters.
class Character:
    def __init__(self, name, cls, level, skills, stats, saves, die):
        self.name = name
        self.cls = cls
        self.level = level
        self.skills = skills
        self.stats = stats
        self.saves = saves
        self.die = die

    #saves, the saves should be a list with several pieces like list of lists.
    def char_saves_mod(self):
        sq = input("which save are you changing? (fort, will, ref")
        if sq in self.saves.keys():
            print("you can only change modifiers( base, racial etc.")
            fort = input("enter the fort saves gained from classes, no racial bonuses or similar")
            ref = input("enter the ref saves gained from classes, no racial bonuses or similar")
            will = input("enter the will saves gained from classes, no racial bonuses or similar")
            fm = input("enter all your fort bonuses, no stat mods")
            rm = input("enter all your fort bonuses, no stat mods")
            wm = input("enter all your fort bonuses, no stat mods")
            self.name.saves = {
                "fort": int(fort) + self.name.stats["CON"] + int(fm),
                "ref": int(ref) + self.name.stats["DEX"] + int(rm),
                "will": int(will) + self.name.stats["WIZ"] + int(wm)
            }

    #char held dices// should this relly exist?
    def char_dices_mod(self, character):
        print("this holds the dice for your character,the dice must already exist")
        q = "yes"
        while q.lower() == "yes":
            d = input("how many sides does your dice have?")
            if d.lower() in character.die.keys():
                x = input("give them a name")
                character.die[x] = CoreEngine.Dice(x, d)
            else:
                print("not in player die")
            q = input("add/change more character dices?")

    #skills
    def char_skills_mod(self, character, q):
        return character.skills.Skills_mod(character, q)

    def char_stats_mod(self, character, stat, score):
        if stat in character.stats.keys():
            character.stats[stat] = score
            return character.stats[stat]
        else:
            return "not in stats"
