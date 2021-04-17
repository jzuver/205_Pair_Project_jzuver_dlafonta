#Represents an instance of a pokemon storage pc
import Pokemon
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
            self.pokemonList.pop(pokemon)
        return 0;


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

    def sortAttack(self):

    def sortType(self):

    def sortHealth(self):

    def sortExp(self):








