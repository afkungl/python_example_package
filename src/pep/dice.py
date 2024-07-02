"""
This module provides a DiceSimulator class for simulating dice throws.
"""

import logging

import numpy as np

logger = logging.getLogger(__name__)


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
        logger.info("DiceSimulator initialized with %s sides", sides)

    def throw(self) -> int:
        """
        Simulate a dice throw.

        Returns:
            int: A random integer between 1 and the number of sides on the dice.
        """
        throw_res = np.random.randint(self.sides) + 1
        logger.info("Throw result: %s", throw_res)
        return throw_res
