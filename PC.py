#Represents an instance of a pokemon storage pc

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

    def bubbleSort(arr):
        n = len(arr)

        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

