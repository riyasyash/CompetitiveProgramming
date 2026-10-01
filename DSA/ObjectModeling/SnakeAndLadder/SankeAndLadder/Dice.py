from random import choice


class Dice:
    """
    class to emulate the behaviour of a dice
    """

    def __init__(self, sides=6):
        self.sides = range(1, sides + 1)

    def roll(self):
        return choice(self.sides)
