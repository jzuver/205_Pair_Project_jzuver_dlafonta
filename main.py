import Pokemon
import Battle
import Team

# quick team and battle test
p = Pokemon.Pokemon("Charizard", 15, "Fire", 100, 150, 50)
p2 = Pokemon.Pokemon("Pikachu", 1, "Electric", 50, 50, 25)
p3 = Pokemon.Pokemon("Squirtle", 23, "Grass", 75, 85, 30)
p4 = Pokemon.Pokemon("Machamp", 5, "Fighting", 50, 75, 45)
p5 = Pokemon.Pokemon("Charmander", 177, "Fire", 50, 100, 40)
p6 = Pokemon.Pokemon("Digglet", 454, "Earth", 50, 75, 35)

p7 = Pokemon.Pokemon("Ghastly", 125, "Fire", 100, 150, 50)
p8 = Pokemon.Pokemon("Raichu", 12, "Electric", 50, 50, 25)
p9 = Pokemon.Pokemon("Bulbasaur", 233, "Grass", 75, 85, 30)
p10 = Pokemon.Pokemon("Machop", 55, "Fighting", 50, 75, 45)
p11 = Pokemon.Pokemon("Charmander", 17, "Fire", 50, 100, 40)
p12 = Pokemon.Pokemon("Dugtrio", 45, "Earth", 50, 75, 35)

t = Team.Team(p, p2, p3, p4, p5, p6)
t2 = Team.Team(p7, p8, p9, p10, p11, p12)

b = Battle.Battle(t, t2)
print(b.toString())

#select fighters for battle
b.setFighterOne(t.chooseRandomFighter())
b.setFighterTwo(t2.chooseRandomFighter())
print(b.toString())

print("After Battle: ")
b.createBattle()
print(b.toString())

print("Team one: ")
print(t.toString())
print("Team Two: ")
print(t2.toString())


