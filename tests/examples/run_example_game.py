"""
This module runs a game of JustLine using a dice simulator.

Dependencies:
- pep.dice
- pep.games.line
"""

from pep import dice
from pep.games import line


def run_a_game() -> None:
    """
    Runs a game of JustLine using a dice simulator.

    Returns:
        None.
    """
    # Get a dice
    a_dice: dice.DiceSimulator = dice.DiceSimulator(6)

    # Get a board
    a_board: line.JustLine = line.JustLine(20)

    max_throws: int = 10
    for _ in range(max_throws):
        throw_res: int = a_dice.throw()
        a_board.step(throw_res)

        if a_board.state_finished:
            print("We won the game")
            break
    else:
        print(f"We did not win in {max_throws} steps. We stop.")


if __name__ == "__main__":
    run_a_game()
