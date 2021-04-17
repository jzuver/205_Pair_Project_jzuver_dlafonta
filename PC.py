#Represents an instance of a pokemon storage pc
import operator
class PC:

    MAX_SIZE = 30

    def __init__(self, pokemonList, maxSize):
        self.pokemonList = pokemonList
        self.maxSize = maxSize
        pokemonList = []
        self.numStored = len(pokemonList)


    def search(self, id):
        for x in self.pokemonList:
            if self.pokemonList[x].id == id:
                return x;

    def search(self, name):
        for x in self.pokemonList:
            if self.pokemonList[x].name == name:
                return x;

    def withdraw(self, pokemon):
        if pokemon in self.pokemonList:
            self.pokemonList.remove(pokemon)


    def deposit(self, pokemon):
        if len(self.pokemonList) >= 30:
            pass;
            print("Box is full!")
        else:
            self.pokemonList.append(pokemon)


    def getPokemonList(self):
        return self.pokemonList

    def getNumStored(self):
        return self.numStored

    def getMaxSize(self):
        return self.maxSize

    def sortID(self):
        self.pokemonList.sort(key=operator.attrgetter('id'))

    def sortName(self):
        self.pokemonList.sort(key=operator.attrgetter('name'))

    def sortType(self):
        self.pokemonList.sort(key=operator.attrgetter('type'))

    def sortExperience(self):
        self.pokemonList.sort(key=operator.attrgetter('experience'))

    def sortAttack(self):
        self.pokemonList.sort(key=operator.attrgetter('attackPower'))

    def sortHealth(self):
        self.pokemonList.sort(key=operator.attrgetter('health'))

    def toString(self):
        s = "Pc Box Contents: ["

        # traverse in the string
        for p in self.pokemonList:
            s += p.name
            s += ","
        s+= "]"

            # return string
        return s



