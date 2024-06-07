from pep import dice


def test_throw_dice():
    # throw 6-sided dice
    print("Throw 6-sided dice")
    six_sided = dice.DiceSimulator(6)
    for _ in range(5):
        res_number = six_sided.throw()
        print(f"Dice thrown: {res_number}")
        assert res_number in [1, 2, 3, 4, 5, 6]

    # throw DnD-sided dice
    print("Throw 20-sided dice")
    twenty_sided = dice.DiceSimulator(20)
    for _ in range(5):
        res_number = twenty_sided.throw()
        print(f"Dice thrown: {res_number}")
        assert res_number in list(range(1, 21))


if __name__ == "__main__":
    test_throw_dice()
