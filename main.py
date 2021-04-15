import Pokemon

# quick attack and experience test
p = Pokemon.Pokemon("Charizard", 15, "Fire", 100, 150, 50)
p2 = Pokemon.Pokemon("Pikachu", 1, "Electric", 50, 75, 50)

print(p.toString())
print(p2.toString())

print("After attack 1")
p.attack(p2)
print(p.toString())
print(p2.toString())

print("After attack 2")
p.attack(p2)
print(p.toString())
print(p2.toString())