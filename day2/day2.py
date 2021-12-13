from collections import namedtuple

FORWARD = "forward"
DOWN = "down"
UP = "up"

NavCommand = namedtuple("NavCommand", ["direction", "distance"])
Location = namedtuple("Location", ["depth", "length"])
Navigation = namedtuple("Navigation", ["location", "aim"])


def split_data_into_commands(data):
    return [
        NavCommand(direction, int(distance))
        for direction, distance in [x.split() for x in data]
    ]


def solve_part_1(data):
    commands = split_data_into_commands(data)
    funcs = {}
    funcs["forward"] = lambda x, y: Location(y.depth, y.length + x)
    funcs["down"] = lambda x, y: Location(y.depth + x, y.length)
    funcs["up"] = lambda x, y: Location(y.depth - x, y.length)

    location = Location(0, 0)
    for command in commands:
        location = funcs[command.direction](command.distance, location)

    return location.depth * location.length


def solve_part_2(data):
    commands = split_data_into_commands(data)
    funcs = {}
    funcs["forward"] = lambda x, y: Navigation(
        Location(y.location.depth + y.aim * x, y.location.length + x), y.aim
    )
    funcs["down"] = lambda x, y: Navigation(y.location, y.aim + x)
    funcs["up"] = lambda x, y: Navigation(y.location, y.aim - x)

    navigation = Navigation(Location(0, 0), 0)
    for command in commands:
        navigation = funcs[command.direction](command.distance, navigation)

    return navigation.location.depth * navigation.location.length


if __name__ == "__main__":
    import os

    script_directory = os.path.dirname(__file__)
    input_path = os.path.join(script_directory, "input")

    data = None
    with open(input_path) as input:
        data = input.readlines()

    result = solve_part_1(data)
    print(f"Part 1: {result}")

    result = solve_part_2(data)
    print(f"Part 2: {result}")
