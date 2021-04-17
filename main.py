import Pokemon
import Team
import Arena
import PC


def runtimeTest(arena):
    # create pokemon to populate the teams
    p = Pokemon.Pokemon("Charizard", 15, "Fire", 100, 150, 50)
    p2 = Pokemon.Pokemon("Pikachu", 1, "Electric", 50, 50, 25)
    p3 = Pokemon.Pokemon("Squirtle", 23, "Grass", 75, 85, 30)
    p4 = Pokemon.Pokemon("Machamp", 5, "Fighting", 50, 75, 45)
    p5 = Pokemon.Pokemon("Charmander", 13, "Fire", 50, 100, 40)
    p6 = Pokemon.Pokemon("Digglet", 151, "Earth", 50, 75, 35)

    p7 = Pokemon.Pokemon("Ghastly", 150, "Fire", 100, 150, 50)
    p8 = Pokemon.Pokemon("Raichu", 12, "Electric", 50, 50, 25)
    p9 = Pokemon.Pokemon("Bulbasaur", 24, "Grass", 75, 80, 30)
    p10 = Pokemon.Pokemon("Machop", 50, "Fighting", 55, 75, 45)
    p11 = Pokemon.Pokemon("Charmander", 17, "Fire", 50, 100, 40)
    p12 = Pokemon.Pokemon("Dugtrio", 78, "Earth", 50, 75, 35)

    p13 = Pokemon.Pokemon("Blastoise", 64, "Fire", 100, 150, 50)
    p14 = Pokemon.Pokemon("Gyrados", 12, "Electric", 50, 50, 25)
    p15 = Pokemon.Pokemon("Mewtwo", 28, "Grass", 75, 85, 30)
    p16 = Pokemon.Pokemon("Onix", 55, "Fighting", 50, 105, 45)
    p17 = Pokemon.Pokemon("Vulpix", 3, "Fire", 50, 110, 40)
    p18 = Pokemon.Pokemon("Flareon", 45, "Earth", 50, 75, 35)

    p19 = Pokemon.Pokemon("Cubone", 107, "Fighting", 100, 150, 50)
    p20 = Pokemon.Pokemon("Bellsprout", 93, "Electric", 50, 50, 25)
    p21 = Pokemon.Pokemon("Voltorb", 18, "Grass", 75, 85, 30)
    p22 = Pokemon.Pokemon("Zubat", 58, "Fighting", 50, 75, 45)
    p23 = Pokemon.Pokemon("Snorlax", 32, "Fire", 50, 120, 70)
    p24 = Pokemon.Pokemon("Dragonite", 78, "Earth", 50, 75, 35)

    teamOne = Team.Team(p, p2, p3, p4, p5, p6)
    teamTwo = Team.Team(p7, p8, p9, p10, p11, p12)
    teamThree = Team.Team(p13, p14, p15, p16, p17, p18)
    teamFour = Team.Team(p19, p20, p21, p22, p23, p24)

    # put pokemon from one team into the PC
    # sort by name, print console
    pc = PC.PC()
    for p in teamFour.team:
        pc.deposit(p)
    print("Unsorted: " + pc.toString())
    pc.sortName()
    print("Sorted: " + pc.toString())







def main():
    arena = Arena.Arena().get()
    runtimeTest(arena)

main()