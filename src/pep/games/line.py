"""A module for playing the JustLine game."""

class JustLine:
    """
    A class representing the JustLine game.

    Attributes:
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

    def step(self, num_steps: int) -> None:
        """
        Moves the player a specified number of steps forward.

        Args:
            num_steps: The number of steps to take.
        """
        if self.state_finished:
            print("The game has already finished.")
            return

        predicted_state = self.state_tile + num_steps

        if predicted_state <= self.length:
            self.state_tile = predicted_state
            print(f"You stepped to tile {self.state_tile}")
        else:
            print("You wanted to step too much, and stay in place.")

        if self.state_tile == self.length:
            print("You arrived at the final tile. The game has finished.")
            self.state_finished = True
