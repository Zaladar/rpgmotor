#1 standard livraries
#2 Third party
#3 Local

class Skills:
    def __init__(self, skname, stat, rnk, mod, clss):
        self.skn = skname
        self.stat = int(stat)
        self.rnk = int(rnk)
        self.mod = int(mod)
        self.clss = bool

    def Skills_mod(self, charachter, sn, what, var):
        charachter.skills[sn].what = var
        return charachter.skills[sn].what

    def summary(self, skn):
        sum = self.skn.stat + self.skn.rnk + self.skn.mod
        if int(self.skn.clss) + (self.skn.rnk / self.skn.rnk) > 1:
            sum += 3
            return sum
        else:
            return sum
