from pep import dice
from pep.games import line


def run_a_game():
    # get a dice
    a_dice = dice.DiceSimulator(6)

    # get a board
    a_board = line.JustLine(20)

    max_throws = 10
    for _ in range(max_throws):
        throw_res = a_dice.throw()
        a_board.step(throw_res)

        if a_board.state_finished:
            print("We won the game")
            break
    else:
        print(f"We did not win in {max_throws} steps. We stop.")


if __name__ == "__main__":
    run_a_game()
