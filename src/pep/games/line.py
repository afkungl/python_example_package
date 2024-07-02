"""A module for playing the JustLine game."""

from pep.games import logger


class JustLine:
    """
    A class representing the JustLine game.

        length (int): The length of the line.
        state_tile (int): The current state of the player's tile.
        state_finished (bool): Whether the game has finished or not.
    """

    def __init__(self, length: int) -> None:
        """
        Initializes a new instance of the JustLine class.

        Args:
            length: The length of the line.
        """
        self.length = length
        self.state_tile = 1
        self.state_finished = False
        logger.info("JustLine game initialized with length %s", length)

    def step(self, num_steps: int) -> None:
        """
        Moves the player a specified number of steps forward.

        Args:
            num_steps: The number of steps to take.
        """
        if self.state_finished:
            print("The game has already finished.")
            logger.warning("Game already finished")
            return

        predicted_state = self.state_tile + num_steps

        if predicted_state <= self.length:
            self.state_tile = predicted_state
            print(f"You stepped to tile {self.state_tile}")
            logger.info("Stepped to tile %s", self.state_tile)
        else:
            print("You wanted to step too much, and stay in place.")
            logger.info("Tried to step too much")

        if self.state_tile == self.length:
            print("You arrived at the final tile. The game has finished.")
            self.state_finished = True
            logger.info("Game finished")
