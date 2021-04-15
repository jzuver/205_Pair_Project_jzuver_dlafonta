# Represents a single Pokemon

class Pokemon:

    def __init__(self, name, id, type, experience, health, attackPower):
        self.name = name
        self.id = id
        self.type = type
        self.experience = experience
        self.health = health
        self.attackPower = attackPower

    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getType(self):
        return self.type

    def getExperience(self):
        return self.experience

    def getHealth(self):
        return self.health

    def getAttackPower(self):
        return self.attackPower

    def toString(self):
        if self.health <= 0:
            s = "KNOCKED OUT: Name: " + self.name + " | ID: " + str(
                self.id) + " | Type: " + self.type + " | Experience: " + str(self.experience) + " | Health: " + str(
                self.health) + " | Attack Power: " + str(self.attackPower)
        else:
            s = "Name: " + self.name + " | ID: " + str(self.id) + " | Type: " + self.type + " | Experience: " + str(
                self.experience) + " | Health: " + str(self.health) + " | Attack Power: " + str(self.attackPower)
        return s

    def attack(self, defendingPokemon):
        # decrease health of defending pokemon and return experience if applicable
        defendingPokemon.health = defendingPokemon.getHealth() - self.attackPower

        if defendingPokemon.getHealth() <= 0:
            self.experience += defendingPokemon.getExperience()
