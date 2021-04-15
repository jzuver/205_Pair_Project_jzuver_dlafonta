# Represents an instance of a single pokemon battle


class Battle:

    def __init__(self, fighterOne, fighterTwo):
        self.fighterOne = fighterOne
        self.fighterTwo = fighterTwo
        self.battleComplete = False
        self.winner = None
        self.loser = None

    def getFighterOne(self):
        return self.fighterOne

    def getFighterTwo(self):
        return self.fighterTwo

    def getBattleCompletionStatus(self):
        return self.battleComplete

    def getWinner(self):
        return self.winner

    def getLoser(self):
        return self.loser

    def toString(self):
        if not self.battleComplete:
            s = "Battle has not started yet.\nFighter one: " + self.fighterOne.toString() + "\nFighter two: " + self.fighterTwo.toString()
        else:
            s = "Battle complete!\nWinner: " + self.winner.getName() + "\nLoser: " + self.loser.getName()
        return s

    def createBattle(self):
        # have pokemon attack each other until one is knocked out,
        # set winner and loser accordingly
        while self.fighterOne.getHealth() > 0 and self.fighterTwo.getHealth() > 0:
            self.fighterOne.attack(self.fighterTwo)
            self.fighterTwo.attack(self.fighterOne)

        if self.fighterOne.getHealth() > 0:
            self.winner = self.fighterOne
            self.loser = self.fighterTwo
        else:
            self.winner = self.fighterTwo
            self.loser = self.fighterOne

        self.battleComplete = True
