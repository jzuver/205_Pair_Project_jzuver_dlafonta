import unittest
import Arena
import Pokemon
import Team


class testBattle(unittest.TestCase):
    arena = None

    @classmethod
    def setUpClass(cls):
        print("setUpClass()")
        cls.arena = Arena.Arena().get()

        # create some pokemon and teams
        cls.p1 = Pokemon.Pokemon("Charizard", 15, "Fire", 100, 150, 50)
        cls.p2 = Pokemon.Pokemon("Pikachu", 1, "Electric", 50, 50, 25)
        cls.p3 = Pokemon.Pokemon("Squirtle", 23, "Grass", 75, 85, 30)
        cls.p4 = Pokemon.Pokemon("Machamp", 5, "Fighting", 50, 75, 45)
        cls.p5 = Pokemon.Pokemon("Charmander", 13, "Fire", 50, 100, 40)
        cls.p6 = Pokemon.Pokemon("Digglet", 151, "Earth", 50, 75, 35)

        cls.p7 = Pokemon.Pokemon("Ghastly", 150, "Fire", 100, 150, 50)
        cls.p8 = Pokemon.Pokemon("Raichu", 12, "Electric", 50, 50, 25)
        cls.p9 = Pokemon.Pokemon("Bulbasaur", 24, "Grass", 75, 80, 30)
        cls.p10 = Pokemon.Pokemon("Machop", 50, "Fighting", 55, 75, 45)
        cls.p11 = Pokemon.Pokemon("Charmander", 17, "Fire", 50, 100, 40)
        cls.p12 = Pokemon.Pokemon("Dugtrio", 78, "Earth", 50, 75, 35)

        cls.p13 = Pokemon.Pokemon("Ghastly", 150, "Fire", 100, 150, 50)
        cls.p14 = Pokemon.Pokemon("Raichu", 12, "Electric", 50, 50, 25)
        cls.p15 = Pokemon.Pokemon("Bulbasaur", 24, "Grass", 75, 80, 30)
        cls.p16 = Pokemon.Pokemon("Machop", 50, "Fighting", 55, 75, 45)
        cls.p17 = Pokemon.Pokemon("Charmander", 17, "Fire", 50, 100, 40)
        cls.p18 = Pokemon.Pokemon("Dugtrio", 78, "Earth", 50, 75, 35)

        cls.teamOne = Team.Team(cls.p1, cls.p2, cls.p3, cls.p4, cls.p5, cls.p6)
        cls.teamTwo = Team.Team(cls.p7, cls.p8, cls.p9, cls.p10, cls.p11, cls.p12)
        cls.teamThree = Team.Team(cls.p13, cls.p14, cls.p15, cls.p16, cls.p17, cls.p18)

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass()")

    def setUp(self):
        print('setUp()')

    def tearDown(self):
        print('tearDown()')
        self.arena.resetClass()

    def testHasBeenInBattleIncorrect(self):
        # Note: this test will failed, because it uses an incorrect implementation
        # of the hasBeenInbattle() method

        # check if team has been in battle, should return True
        self.arena.doBattle(self.teamOne, self.teamTwo)
        rc = self.arena.hasBeenInBattleIncorrect(self.teamOne)
        self.assertTrue(rc)

        # check if team has been in battle, should return False
        rc = self.arena.hasBeenInBattleIncorrect(self.teamThree)
        self.assertFalse(rc)

    def testHasBeenInBattleCorrect(self):
        # check if team has been in battle, should return True
        self.arena.doBattle(self.teamOne, self.teamTwo)
        rc = self.arena.hasBeenInBattleCorrect(self.teamOne)
        self.assertTrue(rc)

        # check if team has been in battle, should return False
        rc = self.arena.hasBeenInBattleCorrect(self.teamThree)
        self.assertFalse(rc)

    def testBattleOne(self):
        # test to make sure there is always a winner in a battle
        # and that battles are being stored in the arena

        #before battle, there should not be a winner
        winner = self.arena.getWinners()
        self.assertEqual(len(winner), 0)

        # check that the arena is not storing a battle yet
        # as the battle hasn't been completed
        self.assertEqual(len(self.arena.getBattles()), 0)
        
        # perform a battle, check that there is 1 winner
        self.arena.doBattle(self.teamOne, self.teamTwo)
        winners = self.arena.getWinners()
        self.assertEqual(len(winners), 1)

        # check that the battle was stored in the arena
        self.assertEqual(len(self.arena.getBattles()), 1)

    def testBattleTwo(self):
        # test to ensure that the battles a team has been in
        # are properly recorded

        # before team has fought in battle, should not have
        # any battles recorded
        battleList = self.arena.getBattlesForTeam(self.teamOne)
        self.assertEqual(len(battleList), 0)

        # perform the battle, check that the team's participation
        # has been recorded
        self.arena.doBattle(self.teamOne, self.teamTwo)
        battleList = self.arena.getBattlesForTeam(self.teamOne)
        self.assertEqual(len(battleList), 1)

        # do it again, check that the team has been a part of two battles
        self.arena.doBattle(self.teamOne, self.teamTwo)
        battleList = self.arena.getBattlesForTeam(self.teamOne)
        self.assertEqual(len(battleList), 2)

    def testPokemon(self):
        # test that pokemon are stored in the arena, and
        # that they can be found by name

        # check that the 5 pokemon are stored in the arena
        self.arena.addPokemon(self.p1)
        self.arena.addPokemon(self.p2)
        self.arena.addPokemon(self.p3)
        self.arena.addPokemon(self.p4)
        self.arena.addPokemon(self.p5)
        self.assertEqual(len(self.arena.getPokemon()), 5)

        # check for a pokemon not in there, should return False
        self.assertFalse(self.arena.findPokemonByName(self.p15))
        
        # check for a pokemon that is stored, should return true
        name = self.p1.getName()
        self.assertTrue(self.arena.findPokemonByName(name))

        # remove the pokemon, check to see that they are removed, should return false
        self.arena.removePokemon(self.p1)
        self.assertFalse(self.arena.findPokemonByName(name))


if __name__ == "__main__":
    unittest.main()
