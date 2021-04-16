import random

# represents a team of pokemon. Each team consists of 6 pokemon
class Team:

    def __init__(self, first=None, second=None, third=None, fourth=None, fifth=None, sixth=None):
        self.team = [first, second, third, fourth, fifth, sixth]

    def getfirst(self):
        return self.team[0]

    def getSecond(self):
        return self.team[1]

    def getThird(self):
        return self.team[2]

    def getFourth(self):
        return self.team[3]

    def getFifth(self):
        return self.team[4]

    def getSixth(self):
        return self.team[5]

    def toString(self):
        s = "First: " + self.getfirst().toString() + "\nSecond: " + self.getSecond().toString() + "\nThird: " + self.getThird().toString() \
            + "\nFourth: " + self.getFourth().toString() + "\nFifth: " + self.getFifth().toString() + "\nSixth: " + self.getSixth().toString()
        return s

    def addToTeam(self, pokemon, index):
        if self.team[index] is None:
            self.team[index] = pokemon
        else:
            print("That spot in the team is full.")

    def withdrawFromTeam(self, index):
        p = self.team[index]
        self.team[index] = None

    def chooseRandomFighter(self):
        index = random.randint(0, 5)
        return self.team[index]

