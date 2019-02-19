import unittest

from ObjectModeling.SnakeAndLadder.SankeAndLadder.Dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_class_initialises_dice_with_six_faces(self):
        self.assertEqual(6, len(self.dice.sides))

    def test_dice_gives_a_random_integer_on_rolling(self):
        self.assertGreaterEqual(6, self.dice.roll())
