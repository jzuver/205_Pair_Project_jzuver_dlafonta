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

    def doBattle(self, teamOne, teamTwo):

