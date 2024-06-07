

class JustLine:

    def __init__(self, length):

        self.length = length
        self.state_tile = 1
        self.state_finished = False

    def step(self, num_steps):

        if self.state_finished:
            print("The game has already finished.")

        predicted_state = self.state_tile + num_steps

        if predicted_state <= self.length:
            self.state_tile = predicted_state
            print(f"You stepped to tile {self.state_tile}")
        else:
            print(f"You wanted to step too much, and stay in place.")

        if self.state_tile == self.length:
            print(f"You arrived at the final tile. The game has finished.")
            self.state_finished = True

