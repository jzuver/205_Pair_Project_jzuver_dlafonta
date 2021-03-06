import Battle


# we're using the singleton design pattern for this
# container class.
#
# when two teams decide to battle in the arena, an instance of battle
# is created. A random pokemon from each team is chosen to battle.
# this shows the association between teams and pokemon

class Arena:
    s_arena = None

    @classmethod
    def get(self):
        if self.s_arena is None:
            self.s_arena = Arena()
        return self.s_arena

    def __init__(self):
        self.battles = set()
        self.teams = set()
        self.pokemon = set()
        self.PC = set()

    # getters
    def getBattles(self):
        return self.battles

    def getTeams(self):
        return self.teams

    def getPokemon(self):
        return self.pokemon

    def getPC(self):
        return self.PC

    # methods to add instance of model objects to arena
    def addBattle(self, battle):
        self.battles.add(battle)

    def addTeam(self, team):
        self.teams.add(team)

    def addPokemon(self, pokemon):
        self.pokemon.add(pokemon)

    def addPC(self, pc):
        self.PC.add(pc)

    def removeBattle(self, battle):
        self.battles.remove(battle)

    def removeTeam(self, team):
        self.battles.remove(team)

    def removePokemon(self, pokemon):
        self.pokemon.remove(pokemon)

    def removePC(self, pc):
        self.battles.remove(pc)

    def doBattle(self, teamOne, teamTwo):
        # create instance of battle, pick a random pokemon from each team,
        # and have them fight
        battle = Battle.Battle(teamOne, teamTwo)
        battle.setFighterOne(battle.getTeamOne().chooseRandomFighter())
        battle.setFighterTwo(battle.getTeamTwo().chooseRandomFighter())

        # perform battle, print results.
        battle.startBattle()
        self.addBattle(battle)
        #print(battle.toString())

    def getWinners(self):
        winners = []
        for b in self.battles:
            if b.getWinner() == None:
                continue
            else:
                winners.append(b.getWinner())

        return winners

    def showBattles(self):
        counter = 1
        for b in self.battles:
            print("Battle: " + str(counter))
            print(b.toString())
            counter += 1

    def getBattlesForTeam(self, team):
        # correct version
        battleList = []
        for b in self.battles:
            if b.getTeamOne() == team or b.getTeamTwo == team:
                battleList.append(b)
        if len(battleList) == 0:
            print("Team has not been in any battles.")
            return battleList
        else:
            return battleList

    def findPokemonByName(self, name):
        for p in self.pokemon:
            if p.getName() == name:
                return True
        else:
            print("Pokemon not currently in the arena.")
            return False

    def hasBeenInBattleCorrect(self, t):
        for b in self.battles:
            for p in t.team:
                if p == b.getWinner() or p == b.getLoser():
                    return True
        return False

    def hasBeenInBattleIncorrect(self, t):
        for b in self.battles:
            for p in t.team:
                if p == b.getWinner() or p == b.getLoser():
                    return False
        return True

    def resetClass(self):
        self.battles = set()
        self.teams = set()
        self.pokemon = set()
        self.PC = set()