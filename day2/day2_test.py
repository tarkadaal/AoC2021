from day2 import solve_part_1, solve_part_2

data = """forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


def test_one():
    result = solve_part_1(data.splitlines())
    assert result == 150


def test_two():
    result = solve_part_2(data.splitlines())
    assert result == 900
