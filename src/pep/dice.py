"""
This module provides a DiceSimulator class for simulating dice throws.
"""

import numpy as np

class DiceSimulator:
    """
    A class for simulating dice throws.

    Attributes:
        sides (int): The number of sides on the dice.
    """

    def __init__(self, sides: int) -> None:
        """
        Initialize the DiceSimulator.

        Args:
            sides (int): The number of sides on the dice.
        """
        self.sides = sides

    def throw(self) -> int:
        """
        Simulate a dice throw.

        Returns:
            int: A random integer between 1 and the number of sides on the dice.
        """
        return np.random.randint(self.sides) + 1
