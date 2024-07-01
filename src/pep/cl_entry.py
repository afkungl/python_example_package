"""
This module contains a simple game that can be played in the console.
"""

import logging

from pep.dice import DiceSimulator
from pep.games.line import JustLine
from pep.applogger import setup_logging


logger = logging.getLogger("PlayApp")

def play_a_game():
    """
    Play a game with one player moving along a line of specified length.
    The player moves along the line by throwing a dice and advancing the
    number of steps equal to the result of the throw.
    The game ends when the player reaches the end of the line.
    """
    setup_logging()
    print("Let us play a simple game.")
    print("You start at the first field.")
    dice_size = input("Choose a dice size!\n")
    logger.info("Chosen dice size: %s", dice_size)
    a_dice = DiceSimulator(int(dice_size))
    length = input("How long should be the playing field?\n")
    a_board = JustLine(int(length))
    logger.info("Chosen board length: %s", length)
    while not a_board.state_finished:
        user_inp = input(f"You are on tile {a_board.state_tile}. Throw dice? (Q, Y)\n")
        logger.info("User input: %s", user_inp)
        if user_inp not in ["Q", "Y"]:
            print("Provide valid input!")
            continue
        if user_inp == "Q":
            print("Abort game")
            return
        if user_inp == "Y":
            throw_res: int = a_dice.throw()
            logger.info("Throw result: %s", throw_res)
            print(f"You throw: {throw_res}")
            a_board.step(throw_res)
            if a_board.state_finished:
                print("We won the game")
                logger.info("Game won")
                break
    print("The game has finished! Good bye!")
    logger.info("Game finished")


if __name__ == "__main__":
    play_a_game()
