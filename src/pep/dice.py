import numpy as np

class DiceSimulator:


    def __init__(self, sides):

        self.sides = sides

    def throw_dice(self):

        return np.random.randint(self.sides) + 1