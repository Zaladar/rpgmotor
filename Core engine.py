from random import *
dices = {}

class Dice:
    def __init__(self, name, sides):
        self.name = name
        self.sides = int(sides)


    def rolling(self, t):
        print("rolling your dice!")
        res = 0
        i = 0
        while i < t:
            res += randint(1, self.sides)
        return res

    # what die exists
    def storeddie(self):
        if self.name in dices:
            print("name: " + str(self.name))
            print("sides: " + str(self.sides))

    # to create new dies if there is a need for it
    def DiceCreator(self):
        print('       =[Dice Creator]=')
        print('=[used to create dice]=')
        print(' ')
        sides = input('how many sides does your dice have?:')
        rn = input("want to name them? default name is d" + sides)
        if rn.lower() == "yes":
            name = input("name:")
        elif rn.lower() == "no":
            print("ok")
            name = rn
        else:
            print("invalid input")
        #dices[name] = Dice(name, sides) dettak anske inte ska vara kvar som så, eftersom funktionen borde returnera en variand av Dice
        print("dices:" + ",".join([x for x in dices.keys()]))


    def sides(self, name):
        sidesqq = int(input("what do you wish to set your sides to?"))
        if isinstance(sidesqq, int):
            dices[name] = Dice(name, sidesqq)
        else:
            print("incvalid input")
            bootupseq()

    def rename(self, name):
        qq = input("This will change the name of the dice proceed?")
        if qq == "yes":
            nameqq = input(" what do you want to call these dice?")
            dices[name] = Dice(nameqq, self.sides)
        elif qq == "no":
            print("okay, rebootinng")
            bootupseq()
        else:
            print("invalid input")
            bootupseq()


def DiceBase():
    pd = [3, 4, 6, 8, 10, 12, 20, 100]
    for i in pd:
        dice = {
            "name": 'd' + str(i),
            "sides": i,
        }
        dices[dice["name"]] = Dice(**dice)
    print("db done")


# en ny funktion spel kontrol ska skapas och där ska man kunna initiera spel boot up ska bara kunna kalla på spelinitiering karaktärs och tärnings förändringar och information.
def Gameinit():
    type = input("what kind of game do you wish to play, pathfinder or dark heresy?")
    if type.lower() == "pathfinder":
        print("pathfinder is being setup!")

    elif type.lower() == "dark heresy":
        print("dark heresy is being setup!")

    else:
        print("invalid input,returning to boot up sequence!")
        bootupseq()


def bootupseq():
    while True:
        ans = input('what function do you want to start? type help for... help...:').lower()
        if ans == 'dice creator':
            Dice.DiceCreator()
        elif ans == 'rolling':
            name = input("what dice do you wish to use?")
            if name in dices.keys():
                Dice.rolling(dices[name])
            else:
                print("invalid input, dices doesn't exist! use dice creator")
        elif ans == "existing die":
            print("dices: " + ",".join([x for x in dices.keys()]))
            req = input("do you want to look at any of the dice? yes/no:")
            req = req.lower()
            if req == "yes":
                name = input("what dice?")
                if name.lower() in dices.keys():
                    Dice.storedie(dices[name])
                else:
                    print("not in dice")
        elif ans == "game init":
            qq = input("what game? Pathfinder or Dark heresy").lower()
            if qq == ("pathfinder"|"dark heresy"):
                Gameinit(qq)
        elif ans == 'help':
            print('lol noob')
            print('functions available: Dice creator, Existing die, Game init and Rolling')
        elif ans == 'break':
            break
        else:
            print('invalid input')
            print("input:" + ans)


DiceBase()
bootupseq()