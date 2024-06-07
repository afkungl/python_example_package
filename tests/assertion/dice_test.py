import pytest
from pep import dice

thow_dice_params = [(4, [1, 2, 3, 4]),
                    (6, [1, 2, 3, 4, 5, 6]),
                    (20, list(range(1, 21)))]


@pytest.mark.assertion
@pytest.mark.parametrize('sides, results', thow_dice_params)
def test_throw_dice(sides, results):
    a_dice = dice.DiceSimulator(sides)
    for _ in range(20):
        assert (a_dice.throw() in results)
