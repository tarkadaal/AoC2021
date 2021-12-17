from collections import namedtuple

FORWARD = "forward"
DOWN = "down"
UP = "up"

NavCommand = namedtuple("NavCommand", ["direction", "distance"])


class Location:
    def __init__(self, depth=0, length=0):
        self.depth = depth
        self.length = length

    def total_distance(self):
        return self.length * self.depth


class Navigation(Location):
    def __init__(self, depth=0, length=0, aim=0):
        super().__init__(depth, length)
        self.aim = aim


def split_data_into_commands(data):
    return [
        NavCommand(direction, int(distance))
        for direction, distance in [x.split() for x in data]
    ]


def process_commands(commands, functions, start_state):
    state = start_state
    for command in commands:
        state = functions[command.direction](command.distance, state)

    return state


def split_and_process(data, functions, start_state):
    commands = split_data_into_commands(data)
    return process_commands(commands, functions, start_state)


def solve_part_1(data):
    funcs = {}
    funcs[FORWARD] = lambda x, y: Location(y.depth, y.length + x)
    funcs[DOWN] = lambda x, y: Location(y.depth + x, y.length)
    funcs[UP] = lambda x, y: Location(y.depth - x, y.length)

    start_state = Location()
    result = split_and_process(data, funcs, start_state)
    return result.total_distance()


def solve_part_2(data):
    funcs = {}
    funcs[FORWARD] = lambda x, y: Navigation(y.depth + y.aim * x, y.length + x, y.aim)
    funcs[DOWN] = lambda x, y: Navigation(y.depth, y.length, y.aim + x)
    funcs[UP] = lambda x, y: Navigation(y.depth, y.length, y.aim - x)

    start_state = Navigation()
    result = split_and_process(data, funcs, start_state)
    return result.total_distance()


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
