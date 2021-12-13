from day1 import solve_part_1, solve_part_2


def test_one():
    data = [1, 2, 3, 3, 2, 4, 90]
    result = solve_part_1(data)
    assert result == 4


def test_two():
    data = [1, 2, 3, 3, 2, 4, 90]
    result = solve_part_2(data)
    assert result == 3
