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

    def testHasBeenInBattleIncorrect(self):
        # Note: this test will failed, because it uses an incorrect implementation
        # of the hasBeenIn
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

if __name__ == "__main__":
    unittest.main()
