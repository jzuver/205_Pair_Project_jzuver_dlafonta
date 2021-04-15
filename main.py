import Pokemon
import Battle

# quick attack and experience test
p = Pokemon.Pokemon("Charizard", 15, "Fire", 100, 150, 50)
p2 = Pokemon.Pokemon("Pikachu", 1, "Electric", 50, 75, 50)
b = Battle.Battle(p, p2)

print(b.toString())

print("\nAfter battle: ")
b.createBattle()

print(b.toString())