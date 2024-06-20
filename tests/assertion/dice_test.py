"""
This module provides a DiceSimulator class for simulating the rolling of a dice.

Usage:
    a_dice = DiceSimulator(6)
    a_dice.throw()

"""

import pytest
from pep import dice

thow_dice_params = [(4, [1, 2, 3, 4]),
                    (6, [1, 2, 3, 4, 5, 6]),
                    (20, list(range(1, 21)))]


@pytest.mark.assertion
@pytest.mark.parametrize('sides, results', thow_dice_params)
def test_throw_dice(sides: int, results: list) -> None:
    """
    Test function for the DiceSimulator class in the dice module.

    Args:
        sides: An integer representing the number of sides on the dice.
        results: A list of possible results from rolling the dice.

    Returns:
        None.
    """
    a_dice = dice.DiceSimulator(sides)
    for _ in range(20):
        assert a_dice.throw() in results


if __name__ == '__main__':
    pytest.main()
